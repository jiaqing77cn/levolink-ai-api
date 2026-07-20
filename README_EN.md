<!--
SEO Keywords: AI API proxy, Claude API proxy, GPT API proxy, OpenAI proxy,
LLM gateway, LLM API, API middleware, AI forwarding, model gateway,
500+ AI models, DeepSeek API, Gemini API, Anthropic API, Claude Code,
OpenAI compatible, China API access, without VPN, pay-per-token, streaming API,
API中转站, Claude API中转, GPT API中转, 中转API, API转发,
国内直连, 免翻墙API, 大模型API, 聚合API, 大模型聚合,
AI代理, Claude中转, GPT中转, OpenAI代理, 低价API
Description: AI API proxy for China - access 500+ models (Claude/GPT/Gemini/DeepSeek) without VPN. OpenAI-compatible, low latency, Claude Code ready. 大模型聚合API中转站，免翻墙国内直连。
-->

<h1 align="center">🚀 Complete Guide to AI API Proxy Services in China | Levolink AI</h1>

<div align="center">

![Stars](https://img.shields.io/github/stars/jiaqing77cn/levolink-ai-api?style=social)
![Forks](https://img.shields.io/github/forks/jiaqing77cn/levolink-ai-api?style=social)
![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Models](https://img.shields.io/badge/500%2B-Models-34d399?style=flat)
![CDN](https://img.shields.io/badge/CDN-China%20加速-3b82f6?style=flat)
![OpenAI Compatible](https://img.shields.io/badge/OpenAI-Compatible-10a37f?style=flat)

**Access Claude / GPT / Gemini / DeepSeek and 500+ AI models in China without VPN**

[🌐 Website](https://ai.levolink.com) · [📋 Pricing](https://ai.levolink.com/pricing) · [📖 API Docs](https://levolink.apifox.cn/)

</div>

> Last updated: 2026-07-20 22:56 (UTC+8)| [中文版](./README.md)

---

## 📋 Table of Contents

- [🔍 How to Choose an API Proxy](#-how-to-choose-an-api-proxy)
- [💰 Live Model Pricing](#-live-model-pricing)
- [🛠️ Integration Guide](#-integration-guide)
- [📊 Comparison](#-comparison)
- [❓ FAQ](#-faq)
- [🤝 Contributing](#-contributing)

---

## 🔍 How to Choose an API Proxy

Six dimensions to evaluate when choosing an AI API proxy:

| Dimension | What to Check | Red Flags |
|-----------|--------------|-----------|
| **Stability** | Frequent downtime? High latency? | Disconnections, no announcements |
| **Speed** | Is response latency acceptable? | >5s first token delay |
| **Model Coverage** | Latest models available? | Slow to add new models |
| **Price Transparency** | Clear billing? Usage logs? | No call records, opaque |
| **Model Swapping** | Using cheap models to impersonate premium? | Abnormally low prices, poor quality |
| **Exit Risk** | Company-operated? Has support? | Solo operator, no customer service |

### ⚠️ Pitfall Checklist

1. **Cache price trap**: Normal cache price is 10%, some charge 15%-30%
2. **Model swapping detection**: Compare outputs between official and proxy with same prompts
3. **Token count fraud**: Send requests with known token counts, check if billing is inflated
4. **Low price trap**: Prices far below market rate likely mean GLM impersonating GPT
5. **Exit scam risk**: Don't deposit large amounts! Pay as you go

### 🔬 How to Detect Model Swapping

```python
# Method 1: Capability test - use reasoning prompts
prompt = "A farmer has 17 sheep. All but 9 die. How many are left?"
# GPT/Claude correct answer: 9
# Low-end models often get it wrong: 8

# Method 2: Long context test
# Send 50K+ token long text, ask about details at the end
# Low-end models lose context

# Method 3: Code capability test
prompt = "Implement an LRU cache with TTL expiration in Python"
# Compare code quality between official and proxy
```

---

## 💰 Live Model Pricing

> Prices are automatically fetched from [Levolink API](https://ai.levolink.com/api/pricing) by GitHub Actions, updated hourly.
>
> Unit: USD / Million Tokens | Output/Input ratio = output price ÷ input price

### OpenAI GPT Series

<!-- GPT_PRICE_TABLE_START -->
| 模型 | 最低价分组 | 倍率 | 输入($/M) | 输出($/M) | 标准分组 | 倍率 | 输入($/M) | 输出($/M) | 出入比 |
|------|-----------|------|-----------|-----------|---------|------|-----------|-----------|--------|
| `gpt-5-codex` | 限时特价 | 0.6x | $0.75 | $6.00 | 默认(Azure+MJ) | 1x | $1.25 | $10.00 | 8x |
| `gpt-5-mini-2025-08-07` | 限时特价 | 0.6x | $0.15 | $1.20 | 默认(Azure+MJ) | 1x | $0.25 | $2.00 | 8x |
| `gpt-5-nano-2025-08-07` | 限时特价 | 0.6x | $0.03 | $0.24 | 默认(Azure+MJ) | 1x | $0.05 | $0.40 | 8x |
| `gpt-5-pro` | 限时特价 | 0.6x | $9.00 | $72.00 | 默认(Azure+MJ) | 1x | $15.00 | $120.00 | 8x |
| `gpt-5.1-codex` | 限时特价 | 0.6x | $0.75 | $6.00 | 默认(Azure+MJ) | 1x | $1.25 | $10.00 | 8x |
| `gpt-5.3-codex-spark` | Codex专属 | 0.8x | $1.40 | $11.20 | 默认(Azure+MJ) | 1x | $1.75 | $14.00 | 8x |
| `gpt-5.4` | 限时特价 | 0.6x | $1.50 | $9.00 | 默认(Azure+MJ) | 1x | $2.50 | $15.00 | 6x |
| `gpt-5.4-mini` | 限时特价 | 0.6x | $0.45 | $2.70 | 默认(Azure+MJ) | 1x | $0.75 | $4.50 | 6x |
| `gpt-5.5` | Codex专属 | 0.8x | $4.00 | $24.00 | 默认(Azure+MJ) | 1x | $5.00 | $30.00 | 6x |
| `gpt-5.6-luna` | Codex专属 | 0.8x | $0.80 | $4.80 | 默认(Azure+MJ) | 1x | $1.00 | $6.00 | 6x |
| `gpt-5.6-luna-max` | Codex专属 | 0.8x | $0.80 | $4.80 | 默认(Azure+MJ) | 1x | $1.00 | $6.00 | 6x |
| `gpt-5.6-sol` | Codex专属 | 0.8x | $4.00 | $24.00 | 默认(Azure+MJ) | 1x | $5.00 | $30.00 | 6x |
| `gpt-5.6-sol-max` | Codex专属 | 0.8x | $4.00 | $24.00 | 默认(Azure+MJ) | 1x | $5.00 | $30.00 | 6x |
| `gpt-5.6-sol-ultra` | Codex专属 | 0.8x | $4.00 | $24.00 | 默认(Azure+MJ) | 1x | $5.00 | $30.00 | 6x |
| `gpt-5.6-terra` | Codex专属 | 0.8x | $2.00 | $12.00 | 默认(Azure+MJ) | 1x | $2.50 | $15.00 | 6x |

<!-- GPT_PRICE_TABLE_END -->

### Anthropic Claude Series

<!-- CLAUDE_PRICE_TABLE_START -->
| 模型 | 最低价分组 | 倍率 | 输入($/M) | 输出($/M) | 标准分组 | 倍率 | 输入($/M) | 输出($/M) | 出入比 |
|------|-----------|------|-----------|-----------|---------|------|-----------|-----------|--------|
| `claude-haiku-4-5-20251001` | 默认(Azure+MJ) | 1x | $1.00 | $5.00 | 默认(Azure+MJ) | 1x | $1.00 | $5.00 | 5x |
| `claude-opus-4-1-20250805` | 默认(Azure+MJ) | 1x | $15.00 | $75.00 | 默认(Azure+MJ) | 1x | $15.00 | $75.00 | 5x |
| `claude-sonnet-4-20250514` | 默认(Azure+MJ) | 1x | $3.00 | $15.00 | 默认(Azure+MJ) | 1x | $3.00 | $15.00 | 5x |
| `claude-sonnet-4-5-20250929` | 默认(Azure+MJ) | 1x | $3.00 | $15.00 | 默认(Azure+MJ) | 1x | $3.00 | $15.00 | 5x |
| `claude-fable-5` | 默认(Azure+MJ) | 1x | $10.00 | $50.00 | 默认(Azure+MJ) | 1x | $10.00 | $50.00 | 5x |
| `claude-opus-4-5-20251101` | 默认(Azure+MJ) | 1x | $5.00 | $25.00 | 默认(Azure+MJ) | 1x | $5.00 | $25.00 | 5x |
| `claude-opus-4-6` | 默认(Azure+MJ) | 1x | $5.00 | $25.00 | 默认(Azure+MJ) | 1x | $5.00 | $25.00 | 5x |
| `claude-opus-4-7` | 默认(Azure+MJ) | 1x | $5.00 | $25.00 | 默认(Azure+MJ) | 1x | $5.00 | $25.00 | 5x |
| `claude-opus-4-8` | 默认(Azure+MJ) | 1x | $5.00 | $25.00 | 默认(Azure+MJ) | 1x | $5.00 | $25.00 | 5x |
| `claude-sonnet-4-6` | 默认(Azure+MJ) | 1x | $3.00 | $15.00 | 默认(Azure+MJ) | 1x | $3.00 | $15.00 | 5x |
| `claude-sonnet-5` | 默认(Azure+MJ) | 1x | $2.00 | $10.00 | 默认(Azure+MJ) | 1x | $2.00 | $10.00 | 5x |

<!-- CLAUDE_PRICE_TABLE_END -->

### Google Gemini Series

<!-- GEMINI_PRICE_TABLE_START -->
| 模型 | 最低价分组 | 倍率 | 输入($/M) | 输出($/M) | 标准分组 | 倍率 | 输入($/M) | 输出($/M) | 出入比 |
|------|-----------|------|-----------|-----------|---------|------|-----------|-----------|--------|
| `gemini-2.0-flash-lite` | 优质Gemini | 3.6x | $0.27 | $1.08 | 优质Gemini | 3.6x | $0.27 | $1.08 | 4x |
| `gemini-2.5-flash` | Gemini-CLI混合 | 1x | $0.30 | $2.50 | Gemini-CLI混合 | 1x | $0.30 | $2.50 | 8.34x |
| `gemini-2.5-flash-image` | 官方Gemini | 2.4x | $0.72 | $6.00 | 官方Gemini | 2.4x | $0.72 | $6.00 | 8.33x |
| `gemini-2.5-flash-lite` | Gemini-CLI混合 | 1x | $0.10 | $0.40 | Gemini-CLI混合 | 1x | $0.10 | $0.40 | 4x |
| `gemini-2.5-pro` | Gemini-CLI混合 | 1x | $1.25 | $10.00 | Gemini-CLI混合 | 1x | $1.25 | $10.00 | 8x |
| `gemini-3.1-flash-lite` | Gemini-CLI混合 | 1x | $0.25 | $1.50 | Gemini-CLI混合 | 1x | $0.25 | $1.50 | 6x |
| `gemini-3.5-flash` | Gemini-CLI混合 | 1x | $1.50 | $9.00 | Gemini-CLI混合 | 1x | $1.50 | $9.00 | 6x |
| `gemini-3-pro-image` | 官方Gemini | 2.4x | $1.58 | $6.34 | 官方Gemini | 2.4x | $1.58 | $6.34 | 4x |

<!-- GEMINI_PRICE_TABLE_END -->

### DeepSeek Series

<!-- DEEPSEEK_PRICE_TABLE_START -->
| 模型 | 最低价分组 | 倍率 | 输入($/M) | 输出($/M) | 标准分组 | 倍率 | 输入($/M) | 输出($/M) | 出入比 |
|------|-----------|------|-----------|-----------|---------|------|-----------|-----------|--------|
| `deepseek-r1` | 限时特价 | 0.6x | $2.40 | $9.60 | 默认(Azure+MJ) | 1x | $4.00 | $16.00 | 4x |
| `deepseek-r1-2025-01-20` | 限时特价 | 0.6x | $2.40 | $9.60 | 默认(Azure+MJ) | 1x | $4.00 | $16.00 | 4x |
| `deepseek-r1-250528` | 限时特价 | 0.6x | $2.40 | $9.60 | 默认(Azure+MJ) | 1x | $4.00 | $16.00 | 4x |
| `deepseek-r1-distill-qwen-32b` | 默认(Azure+MJ) | 1x | $2.00 | $6.00 | 默认(Azure+MJ) | 1x | $2.00 | $6.00 | 3x |
| `deepseek-r1-distill-qwen-7b` | 默认(Azure+MJ) | 1x | $0.50 | $1.00 | 默认(Azure+MJ) | 1x | $0.50 | $1.00 | 2x |
| `deepseek-reasoner` | 限时特价 | 0.6x | $2.40 | $9.60 | 默认(Azure+MJ) | 1x | $4.00 | $16.00 | 4x |
| `deepseek-v3-1-250821` | 限时特价 | 0.6x | $2.40 | $7.20 | 默认(Azure+MJ) | 1x | $4.00 | $12.00 | 3x |
| `deepseek-v3-1-think-250821` | 默认(Azure+MJ) | 1x | $4.00 | $12.00 | 默认(Azure+MJ) | 1x | $4.00 | $12.00 | 3x |

<!-- DEEPSEEK_PRICE_TABLE_END -->

### Chinese Models (Qwen/Doubao/GLM/Kimi)

<!-- CN_MODEL_PRICE_TABLE_START -->
| 模型 | 最低价分组 | 倍率 | 输入($/M) | 输出($/M) | 标准分组 | 倍率 | 输入($/M) | 输出($/M) | 出入比 |
|------|-----------|------|-----------|-----------|---------|------|-----------|-----------|--------|
| `doubao-seed-1-6-250615` | az渠道 | 1.5x | $1.20 | $12.00 | az渠道 | 1.5x | $1.20 | $12.00 | 10x |
| `doubao-seed-1-6-251015` | az渠道 | 1.5x | $1.20 | $12.00 | az渠道 | 1.5x | $1.20 | $12.00 | 10x |
| `doubao-seed-1-6-flash-250828` | az渠道 | 1.5x | $0.45 | $4.50 | az渠道 | 1.5x | $0.45 | $4.50 | 10x |
| `doubao-seed-1-6-thinking-250615` | az渠道 | 1.5x | $1.20 | $12.00 | az渠道 | 1.5x | $1.20 | $12.00 | 10x |
| `doubao-seed-1-6-thinking-250715` | az渠道 | 1.5x | $1.20 | $12.00 | az渠道 | 1.5x | $1.20 | $12.00 | 10x |
| `doubao-seed-1-6-vision-250815` | az渠道 | 1.5x | $2.40 | $19.20 | az渠道 | 1.5x | $2.40 | $19.20 | 8x |
| `glm-4.5` | 限时特价 | 0.6x | $0.96 | $3.84 | 默认(Azure+MJ) | 1x | $1.60 | $6.40 | 4x |
| `glm-4.5-air` | 限时特价 | 0.6x | $0.48 | $3.60 | 默认(Azure+MJ) | 1x | $0.80 | $6.00 | 7.5x |
| `glm-4.5-airx` | 默认(Azure+MJ) | 1x | $4.00 | $16.00 | 默认(Azure+MJ) | 1x | $4.00 | $16.00 | 4x |
| `glm-4.5-flash` | 默认(Azure+MJ) | 1x | $0.02 | $0.08 | 默认(Azure+MJ) | 1x | $0.02 | $0.08 | 4x |

<!-- CN_MODEL_PRICE_TABLE_END -->

> 💡 Full pricing with all 33 groups and 228 models at [Levolink AI Pricing](https://ai.levolink.com/pricing)

### Group Tiers

| Group Type | Ratio | Best For |
|------------|-------|----------|
| Flash Sale | 0.6x | Testing, low-cost use |
| Codex Exclusive | 0.8x | GPT coding, daily use |
| Default | 1.0x | Standard quality, balanced |
| anti/kiro | 1.2x | Budget Claude |
| Claude Code Exclusive | 2.4x | Claude Code programming |
| Azure Channel | 3.0x | Stable GPT |
| AWS Enterprise | 4.0x | Enterprise-grade Claude |
| Vertex/Direct | 6.0x | Highest quality |
| Official Premium | 16.0x | Full official quality |

---

## 🛠️ Integration Guide

### Quick Start

1. Visit [Levolink AI](https://ai.levolink.com) → Register → Console → Create Key
2. Top up (min 1 yuan)
3. Choose your integration method:

### Python (OpenAI SDK)

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-api-key",
    base_url="https://ai.levolink.com/v1"
)

# GPT-5.6 Sol
resp = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": "Write a Python quicksort"}]
)

# Claude Sonnet 4.6
resp = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": "Explain quantum computing"}],
    extra_body={"anthropic_version": "vertex-2023-10-01"}
)

# DeepSeek R1
resp = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[{"role": "user", "content": "Implement a web server in Python"}]
)
```

### Node.js / curl

```bash
curl https://ai.levolink.com/v1/chat/completions \
  -H "Authorization: Bearer your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.6-sol",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

Full examples in [`examples/`](./examples/) directory.

### Claude Code

```bash
npm install -g @anthropic-ai/claude-code

echo 'export ANTHROPIC_AUTH_TOKEN="your-api-key"' >> ~/.bash_profile
echo 'export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"' >> ~/.bash_profile
source ~/.bash_profile

cd your-project && claude
```

### OpenAI Codex

```bash
npm install -g @openai/codex
export OPENAI_API_KEY="your-api-key"
export OPENAI_API_BASE="https://ai.levolink.com/v1"
```

### Gemini CLI

```bash
npm install -g @google/gemini-cli
export GEMINI_API_KEY="your-api-key"
export GEMINI_API_BASE="https://ai.levolink.com/v1"
```

### Tool Integrations

| Tool | Setup |
|------|-------|
| **Dify / FastGPT** | API Key + Base URL: `https://ai.levolink.com/v1` |
| **n8n** | HTTP Request → URL: `https://ai.levolink.com/v1/chat/completions` |
| **LangChain** | `ChatOpenAI(openai_api_key="key", openai_api_base="https://ai.levolink.com/v1")` |
| **NextChat** | Settings → Custom API → URL: `https://ai.levolink.com/v1` |
| **Cursor IDE** | Settings → Env Vars → `ANTHROPIC_BASE_URL=https://ai.levolink.com/v1` |
| **OpenClaw** | `openai_api_key: key` + `openai_api_base: https://ai.levolink.com/v1` |

### Use Cases

- **AI Coding** — Claude Code / Codex with Claude 4.8 / GPT-5.6 for refactoring, bug fixes
- **Long Document Processing** — 100K+ word analysis, contract review, paper summarization
- **AI Agents** — One key for all models, multi-agent parallel tasks
- **RAG Knowledge Bases** — DeepSeek / GPT with vector databases for enterprise Q&A
- **Automated Workflows** — n8n / FastGPT / Dify integration for full automation

---

## 📊 Comparison

| | [Levolink AI](https://ai.levolink.com) | SiliconFlow | Other Proxies | Self-Built |
|--|-------------|-------------|---------------|------------|
| Model count | **500+** | Fewer | Fewer | Manual |
| Group options | **33 groups** | None | Few | - |
| China CDN | ✅ | Average | ✅ | ❌ |
| Min top-up | **1 yuan** | Higher | Higher | - |
| Pay-as-you-go | ✅ | ✅ | ✅ | ❌ |
| Claude Code ready | ✅ | ✅ | ✅ | ❌ |
| OpenAI compatible | ✅ | ✅ | ✅ | Needs adapter |
| Price transparency | ✅ 33 groups | Single price | Single price | - |
| Invoice | ✅ | - | - | - |

---

## ❓ FAQ

**Are responses identical to the official API?**

Yes. Levolink AI only forwards requests to official models — responses are byte-for-byte identical.

**Can my account get banned?**

No. You use Levolink AI's key, not the official account system — no ban risk.

**What's the difference between groups?**

Different groups correspond to different backend channels (Azure/AWS/Vertex/Official Direct, etc.) with varying quality and price. Lower-cost groups offer better value; higher-priced groups offer maximum stability. Start with the default group, then adjust as needed.

**Is streaming supported?**

Yes, all models support `stream: true` with low latency.

**How fast is it from China?**

China CDN nodes, latency typically 40-200ms — much faster than connecting to official APIs directly.

**Is there a free tier?**

New users get trial credits. Start free, top up when ready.

**Can I get an invoice?**

Yes. Settings → Identity Verification → Wallet → Invoice. E-invoice issued within 5 business days.

**Which group should I choose?**

- Budget: Flash Sale (0.6x) / Codex Exclusive (0.8x)
- Balanced: Default (1.0x)
- High quality: Claude Code Exclusive (2.4x) / Azure (3.0x)
- Maximum quality: Vertex (6.0x) / Official Premium (16.0x)

---

## 🤝 Contributing

- 🐛 Bug report → [Open an Issue](https://github.com/jiaqing77cn/levolink-ai-api/issues)
- 📝 Improve docs → Submit a PR
- 💡 Feature request → [Start a Discussion](https://github.com/jiaqing77cn/levolink-ai-api/discussions)
- 📋 Contributing guide → See [CONTRIBUTING.md](./CONTRIBUTING.md)

---

## 📈 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=jiaqing77cn/levolink-ai-api&type=Date)](https://star-history.com/#jiaqing77cn/levolink-ai-api&Date)

---

## 📜 License

MIT License · Copyright (c) 2026 [Levolink AI](https://ai.levolink.com)
