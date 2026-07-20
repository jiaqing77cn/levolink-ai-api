#!/usr/bin/env python3
"""
Levolink AI Pricing Generator
从 API 拉取实时价格，生成 Markdown 表格写入 README.md (中英文)
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


# --- Group name shortening ---

SHORT_MAP_CN = {
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

SHORT_MAP_EN = {
    "支持所有模型;GPT、Claude 它们由Azure+mj快速+其他模型官方": "Default(Azure+MJ)",
    "严选国内顶尖 AI 引擎，具备 99.9% 生产级稳定性。专为核心业务与高频使用设计，为您提供最稳健、最专业的智能支持。": "Enterprise",
    "首调aws，有少量vertex企业级和azure的claude": "AWS Enterprise",
    "gemini-cli 和anti 混合": "Gemini-CLI Mix",
    "限时体验分组": "Flash Trial",
    "限时特价系列": "Flash Sale",
    "az渠道": "Azure Channel",
    "官方Gemini": "Official Gemini",
    "优质官转OpenAI": "Premium OpenAI",
    "优质官转gemini": "Premium Gemini",
    "优质官转gemini2": "Premium Gemini2",
    "优质官方Gemini": "Quality Gemini",
    "正价充值anthropic 官方克劳德": "Official Premium",
    "anti和kiro渠道": "anti/kiro",
    "Claude Code专属特供": "CC Exclusive",
    "Codex专属特供": "Codex Exclusive",
    "awsb+awsp": "AWS-B+P",
    "官+aws渠道": "Official+AWS",
    "直连Gemini 资源为Vertex ai": "Direct Vertex",
}


def shorten_name(name, lang="cn"):
    sm = SHORT_MAP_EN if lang == "en" else SHORT_MAP_CN
    short = sm.get(name)
    if short:
        return short
    return name[:12] + "…" if len(name) > 12 else name


def fmt_ratio(r):
    if isinstance(r, float):
        if r == int(r):
            return str(int(r))
        return f"{r:.2f}".rstrip('0').rstrip('.')
    return str(r)


def find_premium_entry(entries, cheapest):
    """Find a premium group entry that's different from cheapest.
    Prefer mid-tier groups (ratio 1.2-4.0) to show a meaningful price comparison."""
    # Preferred premium groups by group_key, in priority order
    premium_keys = [
        "Claude Code专属",      # 2.4x - CC Exclusive
        "Codex专属",           # 0.8x - but won't be picked if it's the cheapest
        "特价 Claude Code",     # 1.2x - anti/kiro
        "限时claude",          # 2x
        "优质gpt",             # 3x
        "官转克劳德1",           # 4x - AWS enterprise
        "纯AZ",               # 1.5x - Azure
        "官转",               # 3x - az channel
        "优质官转OpenAI",        # 8x
        "优质官转gemini",        # 6x
        "官转gemini",          # 3.6x
    ]
    for pk in premium_keys:
        for e in entries:
            if pk in e["group_key"] and e["group_key"] != cheapest["group_key"]:
                return e
    # Fallback: find a mid-ratio entry (1.5x-5x) different from cheapest
    others = [e for e in entries if e["group_key"] != cheapest["group_key"]]
    mid_tier = [e for e in others if 1.5 <= e["ratio"] <= 5]
    if mid_tier:
        return min(mid_tier, key=lambda x: abs(x["ratio"] - 2.5))
    if others:
        return min(others, key=lambda x: abs(x["ratio"] - 2.5))
    return None


def gen_table(data, model_ids, category_name, lang="cn"):
    """Generate markdown price table for given models"""
    groups = data.get("model_group", {})
    ratios = data.get("model_completion_ratio", {})

    model_to_groups = {}
    for mid in model_ids:
        model_to_groups[mid] = []
        for gname, gval in groups.items():
            mp = gval.get("ModelPrice", {})
            if mid in mp:
                gr = gval.get("GroupRatio", 1)
                price = mp[mid].get("price", 0)
                cr = ratios.get(mid, 1)
                actual_in = price * gr * 2
                cr_num = cr if isinstance(cr, (int, float)) else 1
                actual_out = actual_in * cr_num
                display = shorten_name(gval.get("DisplayName", gname), lang)
                model_to_groups[mid].append({
                    "group": display,
                    "group_key": gname,
                    "ratio": gr,
                    "input": actual_in,
                    "output": actual_out,
                    "cr": cr_num,
                })

    if not any(model_to_groups.values()):
        no_data = f"*No {category_name} model data*" if lang == "en" else f"*暂无{category_name}模型数据*"
        return no_data + "\n"

    if lang == "en":
        header = "| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |"
        separator = "|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|"
    else:
        header = "| 模型 | 最低价分组 | 倍率 | 输入($/M) | 输出($/M) | 推荐分组 | 倍率 | 输入($/M) | 输出($/M) | 出入比 |"
        separator = "|------|-----------|------|-----------|-----------|---------|------|-----------|-----------|--------|"

    lines = [header, separator]

    for mid in model_ids:
        entries = model_to_groups[mid]
        if not entries:
            continue

        sorted_entries = sorted(entries, key=lambda x: x["input"])
        cheapest = sorted_entries[0]

        # Find premium entry (different from cheapest)
        premium = find_premium_entry(entries, cheapest)

        if premium:
            lines.append(
                f"| `{mid}` | {cheapest['group']} | {fmt_ratio(cheapest['ratio'])}x | "
                f"${cheapest['input']:.2f} | ${cheapest['output']:.2f} | "
                f"{premium['group']} | {fmt_ratio(premium['ratio'])}x | "
                f"${premium['input']:.2f} | ${premium['output']:.2f} | "
                f"{fmt_ratio(cheapest['cr'])}x |"
            )
        else:
            # Only one group available
            dash = "-"
            lines.append(
                f"| `{mid}` | {cheapest['group']} | {fmt_ratio(cheapest['ratio'])}x | "
                f"${cheapest['input']:.2f} | ${cheapest['output']:.2f} | "
                f"{dash} | {dash} | {dash} | {dash} | "
                f"{fmt_ratio(cheapest['cr'])}x |"
            )

    return "\n".join(lines) + "\n"


def get_models_by_supplier(data, suppliers):
    model_info = data.get("model_info", {})
    result = []
    for mid, info in model_info.items():
        if info.get("supplier") in suppliers:
            result.append(mid)
    return sorted(result)


def get_models_by_keyword(data, keywords):
    model_info = data.get("model_info", {})
    result = []
    for mid, info in model_info.items():
        mid_lower = mid.lower()
        if any(kw.lower() in mid_lower for kw in keywords):
            result.append(mid)
    return sorted(result)


def extract_models_from_groups(data, keyword):
    groups = data.get("model_group", {})
    result = []
    for gname, gval in groups.items():
        for mid in gval.get("ModelPrice", {}).keys():
            if keyword in mid.lower() and mid not in result:
                result.append(mid)
    return result


def extract_exact_models(data, model_names):
    """Extract exact model names from model_group"""
    groups = data.get("model_group", {})
    result = []
    for mid in model_names:
        for gname, gval in groups.items():
            if mid in gval.get("ModelPrice", {}):
                if mid not in result:
                    result.append(mid)
                break
    return result


def replace_section(readme, section_id, new_content):
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
    gpt_models = get_models_by_keyword(data, ["gpt-5", "gpt-4", "o1", "o3", "o4"])
    gpt_from_groups = extract_models_from_groups(data, "gpt-5")
    gpt_all = list(dict.fromkeys(gpt_models + gpt_from_groups))
    gpt_hot = [m for m in gpt_all if any(x in m.lower() for x in
        ["gpt-5.6-sol", "gpt-5.6-luna", "gpt-5.6-terra", "gpt-5.5", "gpt-5.4-mini", "gpt-5.4-nano",
         "gpt-5.4-pro", "gpt-5.4", "gpt-5.3-chat", "gpt-5.3-codex", "gpt-5.2-chat", "gpt-5.2-codex",
         "gpt-5.1-codex", "gpt-5-codex", "gpt-5-chat", "gpt-5-mini", "gpt-5-nano", "gpt-5-pro"])]
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

    # --- CN models - use exact names to avoid missing ---
    cn_exact = extract_exact_models(data, [
        "qwen3-max", "qwen3-max-2026-01-23", "qwen3-coder", "qwen3-coder-plus",
        "qwen3.6-plus", "qwen3.7-max",
        "glm-4.6", "glm-4.5", "glm-4.5-air",
        "kimi-k2", "kimi-k2.5", "kimi-k3",
        "doubao-seed-1-6-250615", "doubao-seed-1-8-251228",
        "doubao-seed-2-0-lite-260215",
        "MiniMax-M3", "MiniMax-M2.7",
    ])
    # Also try keyword-based for any we missed
    cn_from_kw = []
    for kw in ["qwen3-max", "qwen3-coder", "glm-4.6", "glm-4.5", "doubao-seed", "kimi-k"]:
        cn_from_kw += [m for m in extract_models_from_groups(data, kw) if m not in cn_exact]
    cn_all = list(dict.fromkeys(cn_exact + cn_from_kw))
    # Filter to hot models
    cn_hot = [m for m in cn_all if any(x in m.lower() for x in
        ["qwen3-max", "qwen3-coder", "qwen3.6-plus", "qwen3.7-max",
         "glm-4.6", "glm-4.5",
         "kimi-k2", "kimi-k3",
         "doubao-seed-1-6", "doubao-seed-1-8", "doubao-seed-2-0",
         "minimax-m3", "minimax-m2"])]
    cn_hot = list(dict.fromkeys(cn_hot))[:12]

    print(f"  CN hot models found: {cn_hot}")

    # Generate tables - Chinese
    gpt_table_cn = gen_table(data, gpt_hot, "GPT", "cn")
    claude_table_cn = gen_table(data, claude_hot, "Claude", "cn")
    gemini_table_cn = gen_table(data, gemini_hot, "Gemini", "cn")
    deepseek_table_cn = gen_table(data, deepseek_hot, "DeepSeek", "cn")
    cn_table_cn = gen_table(data, cn_hot, "国产", "cn")

    # Generate tables - English
    gpt_table_en = gen_table(data, gpt_hot, "GPT", "en")
    claude_table_en = gen_table(data, claude_hot, "Claude", "en")
    gemini_table_en = gen_table(data, gemini_hot, "Gemini", "en")
    deepseek_table_en = gen_table(data, deepseek_hot, "DeepSeek", "en")
    cn_table_en = gen_table(data, cn_hot, "Chinese", "en")

    # Timestamp
    now = datetime.now(timezone(timedelta(hours=8)))
    new_ts = now.strftime('%Y-%m-%d %H:%M')

    # Read both READMEs
    with open(README_PATH, "r", encoding="utf-8") as f:
        readme_cn = f.read()

    readme_en_path = os.environ.get("README_EN_PATH", "README_EN.md")
    readme_en = None
    try:
        with open(readme_en_path, "r", encoding="utf-8") as f:
            readme_en = f.read()
    except FileNotFoundError:
        print(f"Warning: {readme_en_path} not found, skipping EN update")

    # Replace sections in Chinese README
    readme_cn = replace_section(readme_cn, "GPT_PRICE_TABLE", gpt_table_cn)
    readme_cn = replace_section(readme_cn, "CLAUDE_PRICE_TABLE", claude_table_cn)
    readme_cn = replace_section(readme_cn, "GEMINI_PRICE_TABLE", gemini_table_cn)
    readme_cn = replace_section(readme_cn, "DEEPSEEK_PRICE_TABLE", deepseek_table_cn)
    readme_cn = replace_section(readme_cn, "CN_MODEL_PRICE_TABLE", cn_table_cn)
    readme_cn = re.sub(
        r'最后更新：[\d\-: ]+ \(UTC\+8\)',
        f'最后更新：{new_ts} (UTC+8)',
        readme_cn
    )

    # Replace sections in English README
    if readme_en:
        readme_en = replace_section(readme_en, "GPT_PRICE_TABLE", gpt_table_en)
        readme_en = replace_section(readme_en, "CLAUDE_PRICE_TABLE", claude_table_en)
        readme_en = replace_section(readme_en, "GEMINI_PRICE_TABLE", gemini_table_en)
        readme_en = replace_section(readme_en, "DEEPSEEK_PRICE_TABLE", deepseek_table_en)
        readme_en = replace_section(readme_en, "CN_MODEL_PRICE_TABLE", cn_table_en)
        readme_en = re.sub(
            r'Last updated:[^|\n]*',
            f'Last updated: {new_ts} (UTC+8)',
            readme_en
        )

    # Write back
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(readme_cn)

    if readme_en:
        with open(readme_en_path, "w", encoding="utf-8") as f:
            f.write(readme_en)
        print(f"  EN README also updated")

    print(f"\n✅ README.md updated at {now.strftime('%Y-%m-%d %H:%M:%S')} UTC+8")
    print(f"  GPT models: {len(gpt_hot)}")
    print(f"  Claude models: {len(claude_hot)}")
    print(f"  Gemini models: {len(gemini_hot)}")
    print(f"  DeepSeek models: {len(deepseek_hot)}")
    print(f"  CN models: {len(cn_hot)}")


if __name__ == "__main__":
    main()
