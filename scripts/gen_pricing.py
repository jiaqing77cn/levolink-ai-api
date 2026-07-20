#!/usr/bin/env python3
"""
Levolink AI Pricing Generator
从 API 拉取实时价格，生成 Markdown 表格写入 README.md
"""

import json
import urllib.request
import sys
import os
import re
from datetime import datetime, timezone, timedelta

API_URL = "https://ai.levolink.com/api/pricing"
README_PATH = os.environ.get("README_PATH", "README.md")


def fetch_pricing():
    """Fetch pricing data from API"""
    req = urllib.request.Request(API_URL)
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)
    return data.get("data", {})


def shorten_name(name):
    """Shorten group display name for table readability"""
    # Map known long names to short names
    short_map = {
        "支持所有模型;GPT、Claude 它们由Azure+mj快速+其他模型官方": "默认(Azure+MJ)",
        "严选国内顶尖 AI 引擎，具备 99.9% 生产级稳定性。专为核心业务与高频使用设计，为您提供最稳健、最专业的智能支持。": "企业级高可用",
        "首调aws，有少量vertex企业级和azure的claude": "AWS企业级",
        "gemini-cli 和anti 混合": "Gemini-CLI混合",
        "限时体验分组": "限时体验",
        "限时特价系列": "限时特价",
        "优质官转OpenAI": "官转OpenAI",
        "优质官转gemini": "官转Gemini",
        "优质官转gemini2": "官转Gemini2",
        "优质官方Gemini": "优质Gemini",
        "正价充值anthropic 官方克劳德": "正价官转Claude",
        "anti和kiro渠道": "anti/kiro",
        "Claude Code专属特供": "CC专属",
        "Codex专属特供": "Codex专属",
        "awsb+awsp": "AWS-B+P",
        "官+aws渠道": "官+AWS",
        "直连Gemini 资源为Vertex ai": "直连Vertex",
    }
    return short_map.get(name, name[:12] + "…" if len(name) > 12 else name)


def fmt_ratio(r):
    """Format ratio number cleanly"""
    if isinstance(r, float):
        if r == int(r):
            return str(int(r))
        return f"{r:.2f}".rstrip('0').rstrip('.')
    return str(r)


def gen_table(data, model_ids, category_name):
    """Generate markdown price table for given models"""
    groups = data.get("model_group", {})
    ratios = data.get("model_completion_ratio", {})

    # Collect all group names that have any of these models
    model_to_groups = {}
    for mid in model_ids:
        model_to_groups[mid] = []
        for gname, gval in groups.items():
            mp = gval.get("ModelPrice", {})
            if mid in mp:
                gr = gval.get("GroupRatio", 1)
                price = mp[mid].get("price", 0)
                cr = ratios.get(mid, 1)
                actual_in = price * gr * 2  # 前端公式: 2 × model_ratio × group_ratio
                cr_num = cr if isinstance(cr, (int, float)) else 1
                actual_out = actual_in * cr_num  # 输出 = 输入 × completion_ratio
                display = shorten_name(gval.get("DisplayName", gname))
                model_to_groups[mid].append({
                    "group": display,
                    "group_key": gname,
                    "ratio": gr,
                    "input": actual_in,
                    "output": actual_out,
                    "cr": cr_num,
                })

    if not any(model_to_groups.values()):
        return f"*暂无{category_name}模型数据*\n"

    lines = []
    lines.append("| 模型 | 最低价分组 | 倍率 | 输入($/M) | 输出($/M) | 标准分组 | 倍率 | 输入($/M) | 输出($/M) | 出入比 |")
    lines.append("|------|-----------|------|-----------|-----------|---------|------|-----------|-----------|--------|")

    for mid in model_ids:
        entries = model_to_groups[mid]
        if not entries:
            continue

        # Sort by input price
        sorted_entries = sorted(entries, key=lambda x: x["input"])
        cheapest = sorted_entries[0]

        # Find default group
        default_entry = None
        for e in entries:
            if "default" in e["group_key"].lower() or e["group_key"] == "default":
                default_entry = e
                break
        if not default_entry:
            # fallback to the one with ratio closest to 1
            default_entry = min(entries, key=lambda x: abs(x["ratio"] - 1))

        lines.append(
            f"| `{mid}` | {cheapest['group']} | {fmt_ratio(cheapest['ratio'])}x | "
            f"${cheapest['input']:.2f} | ${cheapest['output']:.2f} | "
            f"{default_entry['group']} | {fmt_ratio(default_entry['ratio'])}x | "
            f"${default_entry['input']:.2f} | ${default_entry['output']:.2f} | "
            f"{fmt_ratio(cheapest['cr'])}x |"
        )

    return "\n".join(lines) + "\n"


def get_models_by_supplier(data, suppliers):
    """Get model IDs by supplier names"""
    model_info = data.get("model_info", {})
    result = []
    for mid, info in model_info.items():
        if info.get("supplier") in suppliers:
            result.append(mid)
    return sorted(result)


def get_models_by_keyword(data, keywords):
    """Get model IDs by keyword match from model_info"""
    model_info = data.get("model_info", {})
    result = []
    for mid, info in model_info.items():
        mid_lower = mid.lower()
        if any(kw.lower() in mid_lower for kw in keywords):
            result.append(mid)
    return sorted(result)


def extract_models_from_groups(data, keyword):
    """Extract model IDs from model_group pricing that contain keyword"""
    groups = data.get("model_group", {})
    result = []
    for gname, gval in groups.items():
        for mid in gval.get("ModelPrice", {}).keys():
            if keyword in mid.lower() and mid not in result:
                result.append(mid)
    return result


def replace_section(readme, section_id, new_content):
    """Replace content between markers"""
    start_marker = f"<!-- {section_id}_START -->"
    end_marker = f"<!-- {section_id}_END -->"

    start_idx = readme.find(start_marker)
    end_idx = readme.find(end_marker)

    if start_idx == -1 or end_idx == -1:
        print(f"Warning: markers for {section_id} not found, skipping")
        return readme

    before = readme[:start_idx + len(start_marker)]
    after = readme[end_idx:]

    return before + "\n" + new_content + "\n" + after


def main():
    print("Fetching pricing data...")
    data = fetch_pricing()

    model_info = data.get("model_info", {})
    groups = data.get("model_group", {})
    ratios = data.get("model_completion_ratio", {})

    print(f"  Models: {len(model_info)}")
    print(f"  Groups: {len(groups)}")
    print(f"  Ratios: {len(ratios)}")

    # --- GPT models ---
    # Extract from both model_info and model_group (new models may only be in groups)
    gpt_models = get_models_by_keyword(data, ["gpt-5", "gpt-4", "o1", "o3", "o4"])
    gpt_from_groups = extract_models_from_groups(data, "gpt-5")
    gpt_all = list(dict.fromkeys(gpt_models + gpt_from_groups))
    # Pick hot models
    gpt_hot = [m for m in gpt_all if any(x in m.lower() for x in
        ["gpt-5.6-sol", "gpt-5.6-luna", "gpt-5.6-terra", "gpt-5.5", "gpt-5.4-mini", "gpt-5.4-nano",
         "gpt-5.4-pro", "gpt-5.4", "gpt-5.3-chat", "gpt-5.3-codex", "gpt-5.2-chat", "gpt-5.2-codex",
         "gpt-5.1-codex", "gpt-5-codex", "gpt-5-chat", "gpt-5-mini", "gpt-5-nano", "gpt-5-pro"])]
    # Deduplicate, exclude bare "gpt-5" which maps to old model
    gpt_hot = [m for m in gpt_hot if m not in ("gpt-5", "gpt-5-chat-latest")]
    gpt_hot = list(dict.fromkeys(gpt_hot))[:15]

    # --- Claude models ---
    claude_models = get_models_by_keyword(data, ["claude"])
    claude_from_groups = extract_models_from_groups(data, "claude")
    claude_all = list(dict.fromkeys(claude_models + claude_from_groups))
    claude_hot = [m for m in claude_all if any(x in m.lower() for x in
        ["opus-4-8", "opus-4-7", "opus-4-6", "opus-4-5-2025", "sonnet-4-6", "sonnet-5",
         "fable-5", "haiku-4-5-2025", "opus-4-1", "sonnet-4-5-2025", "sonnet-4-2025"])]
    claude_hot = list(dict.fromkeys(claude_hot))[:12]

    # --- Gemini models ---
    gemini_models = get_models_by_keyword(data, ["gemini"])
    gemini_from_groups = extract_models_from_groups(data, "gemini")
    gemini_all = list(dict.fromkeys(gemini_models + gemini_from_groups))
    gemini_hot = [m for m in gemini_all if "latest" not in m.lower() and "preview" not in m.lower()]
    gemini_hot = list(dict.fromkeys(gemini_hot))[:8]

    # --- DeepSeek models ---
    deepseek_models = get_models_by_keyword(data, ["deepseek"])
    deepseek_from_groups = extract_models_from_groups(data, "deepseek")
    deepseek_all = list(dict.fromkeys(deepseek_models + deepseek_from_groups))
    deepseek_hot = [m for m in deepseek_all if any(x in m.lower() for x in
        ["v3.1", "v3-1", "r1", "v3.2", "reasoner"])]
    deepseek_hot = list(dict.fromkeys(deepseek_hot))[:8]

    # --- CN models ---
    cn_models = get_models_by_supplier(data, ["Aliyun", "zhipuai", "doubao", "Moonshot", "MiniMax"])
    cn_from_groups = []
    for kw in ["qwen3", "glm-4.6", "glm-4.5", "doubao-seed", "kimi-k2"]:
        cn_from_groups += [m for m in extract_models_from_groups(data, kw) if m not in cn_models]
    cn_all = list(dict.fromkeys(cn_models + cn_from_groups))
    cn_hot = [m for m in cn_all if any(x in m.lower() for x in
        ["qwen3-max", "qwen3-coder", "glm-4.6", "glm-4.5", "doubao-seed-1-6", "kimi-k2"])]
    cn_hot = list(dict.fromkeys(cn_hot))[:10]

    # Generate tables
    gpt_table = gen_table(data, gpt_hot, "GPT")
    claude_table = gen_table(data, claude_hot, "Claude")
    gemini_table = gen_table(data, gemini_hot, "Gemini")
    deepseek_table = gen_table(data, deepseek_hot, "DeepSeek")
    cn_table = gen_table(data, cn_hot, "国产")

    # Read README
    with open(README_PATH, "r", encoding="utf-8") as f:
        readme = f.read()

    # Replace sections
    readme = replace_section(readme, "GPT_PRICE_TABLE", gpt_table)
    readme = replace_section(readme, "CLAUDE_PRICE_TABLE", claude_table)
    readme = replace_section(readme, "GEMINI_PRICE_TABLE", gemini_table)
    readme = replace_section(readme, "DEEPSEEK_PRICE_TABLE", deepseek_table)
    readme = replace_section(readme, "CN_MODEL_PRICE_TABLE", cn_table)

    # Update timestamp
    now = datetime.now(timezone(timedelta(hours=8)))
    new_ts = now.strftime('%Y-%m-%d %H:%M')
    readme = re.sub(
        r'最后更新：[\d\-: ]+ \(UTC\+8\)',
        f'最后更新：{new_ts} (UTC+8)',
        readme
    )

    # Write back
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(readme)

    print(f"\n✅ README.md updated at {now.strftime('%Y-%m-%d %H:%M:%S')} UTC+8")
    print(f"  GPT models: {len(gpt_hot)}")
    print(f"  Claude models: {len(claude_hot)}")
    print(f"  Gemini models: {len(gemini_hot)}")
    print(f"  DeepSeek models: {len(deepseek_hot)}")
    print(f"  CN models: {len(cn_hot)}")


if __name__ == "__main__":
    main()
