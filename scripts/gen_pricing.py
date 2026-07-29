#!/usr/bin/env python3
"""
Levolink AI Pricing Generator
从 API 拉取实时价格，生成 Markdown 表格写入所有语言 README (中/英/韩/日/西/德)
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
    """Fetch pricing data from API.
    
    API response format changed: `data` is now a list of model objects
    instead of a dict with model_info/model_group/model_completion_ratio.
    We transform it back to the expected internal structure.
    """
    req = urllib.request.Request(API_URL)
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = json.load(resp)
    
    model_list = raw.get("data", [])
    group_ratio = raw.get("group_ratio", {})
    
    # If data is already a dict (old format), return as-is
    if isinstance(model_list, dict):
        return model_list
    
    # --- Transform new list format to old dict format ---
    
    # model_info: {model_name: model_obj}
    model_info = {}
    # model_completion_ratio: {model_name: ratio}
    completion_ratios = {}
    # Build a mapping: for each group, which models are available and their base price
    # Old format: model_group[gname] = {"DisplayName": ..., "GroupRatio": ..., "ModelPrice": {mid: {"price": ...}}}
    model_group = {}
    
    for gname, gr in group_ratio.items():
        model_group[gname] = {
            "DisplayName": gname,
            "GroupRatio": gr,
            "ModelPrice": {}
        }
    
    for m in model_list:
        mid = m.get("model_name", "")
        if not mid:
            continue
        
        model_info[mid] = m
        cr = m.get("completion_ratio", 1)
        # cr could be None or non-numeric
        if not isinstance(cr, (int, float)):
            cr = 1
        completion_ratios[mid] = cr
        
        # model_ratio is the base price multiplier; model_price is for fixed-price models
        base_price = m.get("model_ratio", 0)
        if not isinstance(base_price, (int, float)):
            base_price = 0
        
        # Add this model to each of its enabled groups
        for gname in m.get("enable_groups", []):
            if gname in model_group:
                model_group[gname]["ModelPrice"][mid] = {"price": base_price}
    
    return {
        "model_info": model_info,
        "model_group": model_group,
        "model_completion_ratio": completion_ratios,
    }


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
    # --- Additional translations for non-CN READMEs ---
    "default": "Default",
    "official": "Official",
    "official_2": "Official 2",
    "official_Claude": "Official Claude",
    "official_seedance": "Official Seedance",
    "enterprise": "Enterprise",
    "enterprise-az": "Enterprise Azure",
    "enterprise-az-224": "Enterprise Azure 224",
    "enterprise-az0.4": "Enterprise Azure 0.4",
    "enterprise-az0.45": "Enterprise Azure 0.45",
    "enterprise-az2": "Enterprise Azure 2",
    "enterprise-claude": "Enterprise Claude",
    "enterprise-deepseek": "Enterprise DeepSeek",
    "enterprise-default": "Enterprise Default",
    "enterprise-gemini": "Enterprise Gemini",
    "enterprise-re": "Enterprise RE",
    "gemini-cli": "Gemini CLI",
    "CN Official": "CN Official",
    "GLB Official": "Global Official",
    "Claude Code专属": "Claude Code Exclusive",
    "Claude独立特供": "Claude Special",
    "Codex专属": "Codex Exclusive",
    "codex专供": "Codex Supply",
    "codex独立特供": "Codex Special",
    "cc max": "CC Max",
    "cc蒸馏": "CC Distill",
    "纯AZ": "Pure Azure",
    "纯aws": "Pure AWS",
    "纯aws_p": "Pure AWS-P",
    "官转": "Official Relay",
    "官转OpenAI": "Relay OpenAI",
    "官转gemini": "Relay Gemini",
    "官转克劳德1": "Relay Claude 1",
    "官转克劳德2": "Relay Claude 2",
    "官转克劳德3": "Relay Claude 3",
    "直连Gemini": "Direct Gemini",
    "直连aws claude": "Direct AWS Claude",
    "直连克劳德": "Direct Claude",
    "逆向": "Reverse",
    "优质gpt": "Premium GPT",
    "优质gemini": "Premium Gemini",
    "优质gemini-vertex": "Premium Gemini Vertex",
    "优质grok": "Premium Grok",
    "优质banana": "Premium Banana",
    "特供-优质gpt": "Special-Premium GPT",
    "特供-优质官转openai": "Special-Premium Relay OpenAI",
    "特供-国产4折": "Special-Domestic 40%",
    "特供-国内": "Special-Domestic",
    "特供-豆包": "Special-Doubao",
    "特供-即梦": "Special-Jimeng",
    "特供-kling": "Special-Kling",
    "特供-vidu": "Special-Vidu",
    "特供-minimax": "Special-MiniMax",
    "特供-kiro": "Special-Kiro",
    "特供-claude-az": "Special-Claude Azure",
    "特供-claude-官": "Special-Claude Official",
    "特供-claude-纯aws": "Special-Claude Pure AWS",
    "特供-awsclaude": "Special-AWS Claude",
    "特供-gemini-Pro": "Special-Gemini Pro",
    "特供-gemini45折": "Special-Gemini 45%",
    "特供-deepseekv4": "Special-DeepSeek V4",
    "特供-deepseek-以梦为马": "Special-DeepSeek",
    "特供-openai 2.5": "Special-OpenAI 2.5",
    "特供-cluade45折": "Special-Claude 45%",
    "特供-鲁大师": "Special-Lumaster",
    "特供-诺言": "Special-Nuoyan",
    "特供-大弗": "Special-Dafo",
    "特供-巨日禄": "Special-Jurilu",
    "特供-高维星辰": "Special-Stars",
    "特供-以梦为马-ge0.75": "Special-Dream",
    "特供-CCMAX-鲁大师": "Special-CCMax-Lumaster",
    "特供-HC-codex": "Special-HC-Codex",
    "特供-HC-default": "Special-HC-Default",
    "特供-HC-纯AZ": "Special-HC-Pure Azure",
    "特供-HC1": "Special-HC1",
    "特供-HC2": "Special-HC2",
    "特供-HC3": "Special-HC3",
    "特供-YC": "Special-YC",
    "特供-Z-claude": "Special-Z-Claude",
    "特供-AIX-veo": "Special-AIX-Veo",
    "特供-AIX-优质gemini": "Special-AIX-Premium Gemini",
    "特供-AIX-官转gemini": "Special-AIX-Relay Gemini",
    "特供-az 0.7": "Special-Azure 0.7",
    "特供-az 1.3": "Special-Azure 1.3",
    "特供-banana0.85": "Special-Banana 0.85",
    "特供-cc0.5": "Special-CC 0.5",
    "特供-cc1": "Special-CC 1",
    "特供-即梦": "Special-Jimeng",
    "特供-豆包": "Special-Doubao",
    "特供HC-优质官转openai": "Special-HC-Premium Relay OpenAI",
    "特供HC-官转": "Special-HC-Relay",
    "特供HC-官转openai": "Special-HC-Relay OpenAI",
    "特供HC-限时体验": "Special-HC-Flash Trial",
    "特供PS-gemini": "Special-PS-Gemini",
    "特供PS-gemini-cli": "Special-PS-Gemini CLI",
    "特供PS-gemini3.1pro": "Special-PS-Gemini 3.1 Pro",
    "特供ZD-claude": "Special-ZD-Claude",
    "特供ZD-claude3": "Special-ZD-Claude 3",
    "特供ZD-高企": "Special-ZD-Enterprise",
    "特供007": "Special-007",
    "特供aws*5.6": "Special-AWS 5.6",
    "特供az *1.36": "Special-Azure 1.36",
    "特供az1.5": "Special-Azure 1.5",
    "特供banan2": "Special-Banana 2",
    "特供cc *1.36": "Special-CC 1.36",
    "特供claude-2.8": "Special-Claude 2.8",
    "特供claude-aws": "Special-Claude AWS",
    "特供claude-官": "Special-Claude Official",
    "特供claude-向量": "Special-Claude Vector",
    "特供kimi3折": "Special-Kimi 30%",
    "特供sora": "Special-Sora",
    "特供星星": "Special-Stars",
    "特供米醋": "Special-Micu",
    "特供飞数-claude": "Special-Feishu-Claude",
    "特供飞数-gemini": "Special-Feishu-Gemini",
    "特供飞数-gpt": "Special-Feishu-GPT",
    "特供-aigc-hailuo": "Special-AIGC-Hailuo",
    "特供-aigc-kling": "Special-AIGC-Kling",
    "特供-aigc-vidu": "Special-AIGC-Vidu",
    "限时claude": "Flash Claude",
    "限时体验": "Flash Trial",
    "限时特价": "Flash Sale",
    "限时特价-vertex": "Flash Sale Vertex",
    "限时特供": "Flash Special",
    "限时福利": "Flash Bonus",
    "特价 Claude Code": "Sale Claude Code",
    "特价9折": "Sale 10% Off",
    "特价banana": "Sale Banana",
    "特价codex": "Sale Codex",
    "特价kling": "Sale Kling",
    "特价vidu": "Sale Vidu",
    "阿里4折": "Alibaba 40%",
    "百度4折": "Baidu 40%",
    "百度4.5折": "Baidu 45%",
    "default9折": "Default 10% Off",
    "分组一": "Group 1",
    "分组二": "Group 2",
    "分组三": "Group 3",
    "国内模型": "Domestic Models",
    "国内模型2": "Domestic Models 2",
    "企业级高可用大模型": "Enterprise HA",
    "阶跃专属": "Step Exclusive",
    "牛顿cc专属特供": "Newton CC Special",
    "huxley1.5倍 专属": "Huxley 1.5x Exclusive",
    "huawei-cc": "Huawei-CC",
    "huawei-ccmax": "Huawei-CCMax",
    "huawei-claude": "Huawei-Claude",
    "huawei-deepseek": "Huawei-DeepSeek",
    "huawei-doubao": "Huawei-Doubao",
    "huawei-gemini": "Huawei-Gemini",
    "huawei-gemini-banana": "Huawei-Gemini-Banana",
    "huawei-gpt": "Huawei-GPT",
    "huawei-grok": "Huawei-Grok",
    "huaweigemini": "Huawei Gemini",
    "MJ慢速": "MJ Slow",
    "gpt-绘图": "GPT-Draw",
    "grok1.3": "Grok 1.3",
    "Ideogram0.9": "Ideogram 0.9",
    "seedance": "Seedance",
    "sora-vip": "Sora VIP",
    "sora2-vip": "Sora2 VIP",
    "0.22az专属": "0.22 Azure Exclusive",
    "154788gemini0.43": "Gemini 0.43",
    "az0.3": "Azure 0.3",
    "az0.4": "Azure 0.4",
    "az  claude": "Azure Claude",
    "Vertex  claude": "Vertex Claude",
    "banana-特供": "Banana Special",
    "momo特供": "Momo Special",
    "dataeyes": "DataEyes",
    "uchat_o3_特供": "UChat O3 Special",
    "uchat_qwen": "UChat Qwen",
    "专供gemini": "Exclusive Gemini",
    "向量-特供生图-低价": "Vector-Special Image-Low",
    "向量-特供生图-高价": "Vector-Special Image-High",
    "向量特供陕西天林-纯awsp": "Vector-Shaanxi Tianlin-AWSP",
    "inferel  special supply": "Inferel Special",
    "inferel special supply-awsp": "Inferel Special-AWSP",
    "billing-test": "Billing Test",
    "billing-test-user": "Billing Test User",
    "技术测试": "Tech Test",
    "测试": "Test",
    "测试424935": "Test 424935",
    "吊毛": "Test-A",
    "大哥": "Test-B",
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
    print(f"  CN README updated")

    if readme_en:
        with open(readme_en_path, "w", encoding="utf-8") as f:
            f.write(readme_en)
        print(f"  EN README updated")

    # Update additional language READMEs (KO/JA/ES/DE) with English price tables
    extra_langs = [
        ("README_KO.md", "KO"),
        ("README_JA.md", "JA"),
        ("README_ES.md", "ES"),
        ("README_DE.md", "DE"),
    ]
    for fname, lang_code in extra_langs:
        try:
            with open(fname, "r", encoding="utf-8") as f:
                content = f.read()
            content = replace_section(content, "GPT_PRICE_TABLE", gpt_table_en)
            content = replace_section(content, "CLAUDE_PRICE_TABLE", claude_table_en)
            content = replace_section(content, "GEMINI_PRICE_TABLE", gemini_table_en)
            content = replace_section(content, "DEEPSEEK_PRICE_TABLE", deepseek_table_en)
            content = replace_section(content, "CN_MODEL_PRICE_TABLE", cn_table_en)
            content = re.sub(
                r'Last updated:[^|\n]*',
                f'Last updated: {new_ts} (UTC+8)',
                content
            )
            with open(fname, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  {lang_code} README updated")
        except FileNotFoundError:
            print(f"  Warning: {fname} not found, skipping")

    print(f"\n✅ All READMEs updated at {now.strftime('%Y-%m-%d %H:%M:%S')} UTC+8")
    print(f"  GPT models: {len(gpt_hot)}")
    print(f"  Claude models: {len(claude_hot)}")
    print(f"  Gemini models: {len(gemini_hot)}")
    print(f"  DeepSeek models: {len(deepseek_hot)}")
    print(f"  CN models: {len(cn_hot)}")


if __name__ == "__main__":
    main()
