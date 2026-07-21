#!/usr/bin/env python3
"""
Levolink AI Cost Calculator
估算 API 调用成本

Usage:
    python scripts/cost_calculator.py --model gpt-5.6-sol --group codex --input-tokens 1000000 --output-tokens 500000
    python scripts/cost_calculator.py --model claude-opus-4-8 --group default --input-tokens 500000 --output-tokens 250000
"""

import json
import urllib.request
import argparse
import sys

API_URL = "https://ai.levolink.com/api/pricing"

# Group name aliases (user-friendly -> API key)
GROUP_ALIASES = {
    "flash": "限时特价",
    "codex": "Codex专属",
    "default": "default",
    "cc": "Claude Code专属",
    "anti": "特价 Claude Code",
    "azure": "纯AZ",
    "aws": "官转克劳德1",
    "vertex": "Vertex  claude",
    "premium": "直连克劳德",
    "official": "official_Claude",
}


def fetch_pricing():
    req = urllib.request.Request(API_URL)
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)
    return data.get("data", {})


def calculate_cost(data, model, group_alias, input_tokens, output_tokens):
    groups = data.get("model_group", {})
    ratios = data.get("model_completion_ratio", {})

    # Resolve group alias
    group_key = GROUP_ALIASES.get(group_alias.lower(), group_alias)

    # Find the group
    group_data = None
    for gname, gval in groups.items():
        if group_alias.lower() in gname.lower() or gname == group_key:
            group_data = gval
            group_key = gname
            break
        display = gval.get("DisplayName", "")
        if group_alias.lower() in display.lower():
            group_data = gval
            group_key = gname
            break

    if not group_data:
        print(f"❌ 未找到分组: {group_alias}")
        print(f"可用分组: {', '.join(groups.keys())}")
        sys.exit(1)

    # Find model price
    mp = group_data.get("ModelPrice", {})
    if model not in mp:
        print(f"❌ 分组 '{group_data.get('DisplayName', group_key)}' 中未找到模型: {model}")
        print(f"该分组可用模型: {', '.join(list(mp.keys())[:20])}...")
        sys.exit(1)

    price = mp[model].get("price", 0)
    group_ratio = group_data.get("GroupRatio", 1)
    cr = ratios.get(model, 1)
    cr_num = cr if isinstance(cr, (int, float)) else 1

    # Calculate: 2 × model_ratio × group_ratio (per million tokens)
    input_price_per_m = price * group_ratio * 2
    output_price_per_m = input_price_per_m * cr_num

    # Cost = price per million × (tokens / million)
    input_cost = input_price_per_m * (input_tokens / 1_000_000)
    output_cost = output_price_per_m * (output_tokens / 1_000_000)
    total_cost = input_cost + output_cost

    display_name = group_data.get("DisplayName", group_key)
    short_name = display_name[:20] + "…" if len(display_name) > 20 else display_name

    print(f"\n{'='*50}")
    print(f"📊 Levolink AI 费用估算")
    print(f"{'='*50}")
    print(f"模型: {model}")
    print(f"分组: {short_name} ({group_ratio}x)")
    print(f"出入倍率: {cr_num}x")
    print(f"")
    print(f"输入: {input_tokens:,} tokens = ${input_cost:.4f}")
    print(f"输出: {output_tokens:,} tokens = ${output_cost:.4f}")
    print(f"{'─'*50}")
    print(f"总计: ${total_cost:.4f}")
    print(f"{'='*50}")
    print(f"\n💡 价格: 输入 ${input_price_per_m:.2f}/M | 输出 ${output_price_per_m:.2f}/M")
    print(f"公式: 2 × ${price:.2f} × {group_ratio} = ${input_price_per_m:.2f}/M (输入)")

    return total_cost


def main():
    parser = argparse.ArgumentParser(description="Levolink AI 费用计算器")
    parser.add_argument("--model", required=True, help="模型名 (如 gpt-5.6-sol)")
    parser.add_argument("--group", required=True, help="分组名 (flash/codex/default/cc/anti/azure/aws)")
    parser.add_argument("--input-tokens", type=int, default=1000000, help="输入 token 数 (默认 1M)")
    parser.add_argument("--output-tokens", type=int, default=500000, help="输出 token 数 (默认 500K)")

    args = parser.parse_args()

    print("正在获取最新价格...")
    data = fetch_pricing()
    calculate_cost(data, args.model, args.group, args.input_tokens, args.output_tokens)


if __name__ == "__main__":
    main()
