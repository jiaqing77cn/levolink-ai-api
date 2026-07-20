#!/usr/bin/env python3
"""
Levolink AI Pricing Generator
从 API 拉取实时价格，生成 Markdown 表格写入 README.md
"""

import json
import urllib.request
import sys
import os
from datetime import datetime, timezone, timedelta

API_URL = "https://ai.levolink.com/api/pricing"
README_PATH = os.environ.get("README_PATH", "README.md")

# 人民币汇率 (approx)
USD_TO_CNY = 7.2

def fetch_pricing():
    """Fetch pricing data from API"""
    req = urllib.request.Request(API_URL)
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)
    return data.get("data", {})

def format_price(price, ratio, group_ratio):
    """Calculate actual input/output prices"""
    actual_input = price * group_ratio
    cr = ratio if isinstance(ratio, (int, float)) else 1
    actual_output = actual_input * cr
    return actual_input, actual_output

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
                actual_in, actual_out = format_price(price, cr, gr)
                display = gval.get("DisplayName", gname)
                model_to_groups[mid].append({
                    "group": display,
                    "group_key": gname,
                    "ratio": gr,
                    "input": actual_in,
                    "output": actual_out,
                    "cr": cr,
                    "base_price": price,
                })
    
    if not any(model_to_groups.values()):
        return f"*暂无{category_name}模型数据*\n"
    
    # Build table: Model | 最低分组 | 最低输入 | 最低输出 | 标准输入 | 标准输出 | 出入倍率
    lines = []
    lines.append("| 模型 | 最低价分组 | 输入($/M) | 输出($/M) | 标准分组 | 输入($/M) | 输出($/M) | 出入倍率 |")
    lines.append("|------|-----------|-----------|-----------|---------|-----------|-----------|---------|")
    
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
            default_entry = entries[0]
        
        lines.append(
            f"| `{mid}` | {cheapest['group']} ({cheapest['ratio']}x) | "
            f"${cheapest['input']:.2f} | ${cheapest['output']:.2f} | "
            f"{default_entry['group']} ({default_entry['ratio']}x) | "
            f"${default_entry['input']:.2f} | ${default_entry['output']:.2f} | "
            f"{cheapest['cr']}x |"
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
    """Get model IDs by keyword match"""
    model_info = data.get("model_info", {})
    result = []
    for mid, info in model_info.items():
        mid_lower = mid.lower()
        if any(kw.lower() in mid_lower for kw in keywords):
            result.append(mid)
    return sorted(result)

def replace_section(readme, section_id, new_content):
    """Replace content between markers"""
    start_marker = f"<!-- {section_id}_START -->"
    end_marker = f"<!-- {section_id}_END -->"
    
    start_idx = readme.find(start_marker)
    end_idx = readme.find(end_marker)
    
    if start_idx == -1 or end_idx == -1:
        print(f"Warning: markers for {section_id} not found, skipping")
        return readme
    
    # Include the markers in the replacement
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
    
    # Define model categories
    gpt_models = get_models_by_keyword(data, ["gpt-5", "gpt-4", "o1", "o3", "o4"])
    # Filter to most relevant
    gpt_hot = [m for m in gpt_models if any(x in m for x in 
        ["gpt-5.6-sol", "gpt-5.5", "gpt-5.4", "gpt-5.4-mini", "gpt-5.3", "gpt-5.2", "gpt-5.1", "gpt-5-", "gpt-5\n", "gpt-image-2"])]
    # Deduplicate and keep clean list
    gpt_hot = list(dict.fromkeys(gpt_hot))[:15]
    
    claude_models = get_models_by_keyword(data, ["claude"])
    # Also extract claude models from model_group pricing (new models not in model_info)
    for gname, gval in groups.items():
        for mid in gval.get("ModelPrice", {}).keys():
            if "claude" in mid.lower() and mid not in claude_models:
                claude_models.append(mid)
    # Pick the hot ones (exclude bare version names that have weird pricing)
    claude_hot = [m for m in claude_models if any(x in m.lower() for x in 
        ["opus-4-8", "opus-4-7", "opus-4-6", "opus-4-5-2025", "sonnet-4-6", "sonnet-5", "fable-5", "haiku-4-5-2025", "opus-4-1", "sonnet-4-5-2025", "sonnet-4-2025"])]
    claude_hot = list(dict.fromkeys(claude_hot))[:12]
    
    gemini_models = get_models_by_keyword(data, ["gemini"])
    gemini_hot = [m for m in gemini_models if "latest" not in m and "preview" not in m][:8]
    
    deepseek_models = get_models_by_keyword(data, ["deepseek"])
    deepseek_hot = [m for m in deepseek_models if any(x in m for x in 
        ["v3.1", "v3-1", "r1", "v3.2", "reasoner"])]
    deepseek_hot = list(dict.fromkeys(deepseek_hot))[:8]
    
    cn_models = get_models_by_supplier(data, ["Aliyun", "zhipuai", "doubao", "Moonshot", "MiniMax"])
    # Filter hot ones
    cn_hot = [m for m in cn_models if any(x in m for x in 
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
    
    # Update timestamp - replace any existing timestamp pattern
    import re
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
