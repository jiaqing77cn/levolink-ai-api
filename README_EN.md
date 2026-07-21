<!--
SEO Keywords: AI API proxy, Claude API proxy, GPT API proxy, OpenAI proxy,
GPT-5.6 API, GPT-5.6 Sol, Claude 4.8 API, Claude Opus 4.8, Claude Sonnet 4.6,
Claude Code proxy, Codex proxy, LLM gateway China, API relay service,
OpenAI compatible, China API access, without VPN, pay-per-token, streaming API,
cheapest Claude API, openai api alternative, api forwarding service,
AI API 中转站, Claude API 中转, GPT API 中转, 中转 API, API 转发,
国内直连, 免翻墙 API, 大模型 API, 聚合 API, AI 代理, 低价 API
Description: AI API proxy for China - access 500+ models (GPT-5.6/Claude 4.8/Gemini 3.5/DeepSeek R1) without VPN. OpenAI-compatible, low latency, Claude Code ready. 33 groups, 1 yuan min top-up.
-->

<h1 align="center">🚀 AI API Proxy in China Without VPN | Claude/GPT/Gemini/DeepSeek | Levolink AI</h1>

<div align="center">

![Stars](https://img.shields.io/github/stars/jiaqing77cn/levolink-ai-api?style=social)
![Forks](https://img.shields.io/github/forks/jiaqing77cn/levolink-ai-api?style=social)
![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Models](https://img.shields.io/badge/500%2B-Models-34d399?style=flat)
![CDN](https://img.shields.io/badge/CDN-China%20Accel-3b82f6?style=flat)
![OpenAI Compatible](https://img.shields.io/badge/OpenAI-Compatible-10a37f?style=flat)

**No VPN · Low Latency · 500+ Models · OpenAI Compatible · Claude Code Ready**

[🌐 Website](https://ai.levolink.com) · [📋 Pricing](https://ai.levolink.com/pricing) · [📖 API Docs](https://levolink.apifox.cn/) · [💬 Contact](https://ai.levolink.com)

</div>

> Last updated: 2026-07-21 23:38 (UTC+8)| [Chinese](./README.md) | English

---

## 📋 Table of Contents

- [🖥️ Product Preview](#-product-preview)
- [🔍 How to Choose an API Proxy](#-how-to-choose-an-api-proxy)
- [💰 Live Model Pricing](#-live-model-pricing)
- [🛠️ Integration Guide](#-integration-guide)
- [📊 Comparison](#-comparison)
- [❓ FAQ](#-faq)
- [🤝 Contributing](#-contributing)

---

## 🖥️ Product Preview

![Levolink AI homepage - 500+ AI model API proxy dashboard](https://raw.githubusercontent.com/jiaqing77cn/levolink-ai-api/main/assets/homepage.jpg)

![Levolink AI dashboard - create API keys, view usage, top up account](https://raw.githubusercontent.com/jiaqing77cn/levolink-ai-api/main/assets/console.jpg)

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
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `gpt-5-codex` | enterprise-a… | 0.35x | $0.15 | $1.22 | Codex专属 | 0.8x | $0.35 | $2.80 | 8x |
| `gpt-5-mini` | enterprise-a… | 0.35x | $0.03 | $0.24 | 特供-优质gpt | 5.6x | $0.49 | $3.92 | 8x |
| `gpt-5-mini-2025-08-07` | enterprise-a… | 0.35x | $0.03 | $0.24 | 特供-优质gpt | 5.6x | $0.49 | $3.92 | 8x |
| `gpt-5-nano` | enterprise-a… | 0.35x | $0.01 | $0.05 | 特供-优质gpt | 5.6x | $0.10 | $0.78 | 8x |
| `gpt-5-nano-2025-08-07` | enterprise-a… | 0.35x | $0.01 | $0.05 | 特供-优质gpt | 5.6x | $0.10 | $0.78 | 8x |
| `gpt-5-pro` | enterprise-a… | 0.35x | $1.84 | $14.70 | 特供-优质gpt | 5.6x | $29.40 | $235.20 | 8x |
| `gpt-5.1-codex` | 特价9折 | 0.54x | $0.36 | $2.92 | Codex专属 | 0.8x | $0.54 | $4.32 | 8x |
| `gpt-5.1-codex-max` | 特价9折 | 0.54x | $0.36 | $2.92 | 纯AZ | 1.5x | $1.01 | $8.10 | 8x |
| `gpt-5.1-codex-mini` | enterprise-a… | 0.35x | $0.03 | $0.24 | 纯AZ | 1.5x | $0.13 | $1.05 | 8x |
| `gpt-5.2-chat` | enterprise-a… | 0.35x | $0.21 | $1.71 | 特供-优质gpt | 5.6x | $3.43 | $27.44 | 8x |
| `gpt-5.2-chat-latest` | enterprise-a… | 0.35x | $0.21 | $1.71 | 特供-优质gpt | 5.6x | $3.43 | $27.44 | 8x |
| `gpt-5.2-codex` | 特价9折 | 0.54x | $0.51 | $4.08 | 特供-优质gpt | 5.6x | $5.29 | $42.34 | 8x |
| `gpt-5.3-chat-latest` | enterprise-a… | 0.35x | $0.21 | $1.71 | 特供-优质gpt | 5.6x | $3.43 | $27.44 | 8x |
| `gpt-5.3-codex` | 特价9折 | 0.54x | $0.51 | $4.08 | 特供-优质gpt | 5.6x | $5.29 | $42.34 | 8x |
| `gpt-5.3-codex-spark` | Codex专属 | 0.8x | $1.12 | $8.96 | Premium OpenAI | 8x | $11.20 | $89.60 | 8x |

<!-- GPT_PRICE_TABLE_END -->

### Anthropic Claude Series

<!-- CLAUDE_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `claude-fable-5` | default | 1x | $10.00 | $50.00 | Claude Code专… | 2.4x | $24.00 | $120.00 | 5x |
| `claude-haiku-4-5-20251001` | default | 1x | $1.00 | $5.00 | Claude Code专… | 2.4x | $2.40 | $12.00 | 5x |
| `claude-opus-4-1-20250805` | default | 1x | $15.00 | $75.00 | Claude Code专… | 2.4x | $36.00 | $180.00 | 5x |
| `claude-opus-4-5-20251101` | default | 1x | $5.00 | $25.00 | Claude Code专… | 2.4x | $12.00 | $60.00 | 5x |
| `claude-opus-4-6` | default | 1x | $5.00 | $25.00 | Claude Code专… | 2.4x | $12.00 | $60.00 | 5x |
| `claude-opus-4-7` | default | 1x | $5.00 | $25.00 | Claude Code专… | 2.4x | $12.00 | $60.00 | 5x |
| `claude-opus-4-8` | default | 1x | $5.00 | $25.00 | Claude Code专… | 2.4x | $12.00 | $60.00 | 5x |
| `claude-sonnet-4-20250514` | default | 1x | $3.00 | $15.00 | Claude Code专… | 2.4x | $7.20 | $36.00 | 5x |
| `claude-sonnet-4-5-20250929` | default | 1x | $3.00 | $15.00 | Claude Code专… | 2.4x | $7.20 | $36.00 | 5x |
| `claude-sonnet-4-6` | default | 1x | $3.00 | $15.00 | Claude Code专… | 2.4x | $7.20 | $36.00 | 5x |
| `claude-sonnet-5` | default | 1x | $2.00 | $10.00 | Claude Code专… | 2.4x | $4.80 | $24.00 | 5x |

<!-- CLAUDE_PRICE_TABLE_END -->

### Google Gemini Series

<!-- GEMINI_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `gemini-2.0-flash-lite` | 官转gemini | 3.6x | $0.97 | $3.89 | Premium Gemini | 6x | $1.62 | $6.48 | 4x |
| `gemini-2.5-flash` | gemini-cli | 1x | $0.30 | $2.50 | Premium Gemini | 6x | $1.80 | $15.01 | 8.34x |
| `gemini-2.5-flash-image` | 优质gemini | 2.4x | $0.00 | $0.00 | Premium Gemini | 6x | $0.00 | $0.00 | 0x |
| `gemini-2.5-flash-lite` | gemini-cli | 1x | $0.10 | $0.40 | Premium Gemini | 6x | $0.60 | $2.40 | 4x |
| `gemini-2.5-pro` | gemini-cli | 1x | $1.25 | $10.00 | Premium Gemini | 6x | $7.50 | $60.00 | 8x |
| `gemini-3-pro-image` | 优质gemini | 2.4x | $0.00 | $0.00 | Premium Gemini | 6x | $0.00 | $0.00 | 0x |
| `gemini-3.1-flash-image` | 优质gemini | 2.4x | $0.00 | $0.00 | Premium Gemini | 6x | $0.00 | $0.00 | 0x |
| `gemini-3.1-flash-lite` | gemini-cli | 1x | $0.25 | $1.50 | Premium Gemini | 6x | $1.50 | $9.00 | 6x |

<!-- GEMINI_PRICE_TABLE_END -->

### DeepSeek Series

<!-- DEEPSEEK_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `deepseek-r1` | uchat_qwen | 0.6x | $1.44 | $5.76 | 纯AZ | 1.5x | $3.60 | $14.40 | 4x |
| `deepseek-r1-0528` | uchat_qwen | 0.6x | $1.44 | $5.76 | 纯AZ | 1.5x | $3.60 | $14.40 | 4x |
| `deepseek-r1-2025-01-20` | uchat_qwen | 0.6x | $1.44 | $5.76 | 纯AZ | 1.5x | $3.60 | $14.40 | 4x |
| `deepseek-r1-250120` | uchat_qwen | 0.6x | $1.44 | $5.76 | 纯AZ | 1.5x | $3.60 | $14.40 | 4x |
| `deepseek-r1-250528` | uchat_qwen | 0.6x | $1.44 | $5.76 | 纯AZ | 1.5x | $3.60 | $14.40 | 4x |
| `deepseek-r1-distill-qwen-32b` | 特供-国产4折 | 0.8x | $1.28 | $3.84 | 纯AZ | 1.5x | $2.40 | $7.20 | 3x |
| `deepseek-r1-distill-qwen-7b` | 特供-国产4折 | 0.8x | $0.32 | $0.64 | 纯AZ | 1.5x | $0.60 | $1.20 | 2x |
| `deepseek-reasoner` | uchat_qwen | 0.6x | $1.44 | $5.76 | 纯AZ | 1.5x | $3.60 | $14.40 | 4x |

<!-- DEEPSEEK_PRICE_TABLE_END -->

### Chinese Models (Qwen/Doubao/GLM/Kimi/MiniMax)

<!-- CN_MODEL_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `qwen3-max` | 限时特价 | 0.6x | $0.90 | $3.60 | 纯AZ | 1.5x | $2.25 | $9.00 | 4x |
| `qwen3-max-2026-01-23` | 阿里4折 | 0.8x | $1.60 | $6.40 | 纯AZ | 1.5x | $3.00 | $12.00 | 4x |
| `qwen3-coder` | 特供-国产4折 | 0.8x | $3.84 | $15.36 | 纯AZ | 1.5x | $7.20 | $28.80 | 4x |
| `qwen3-coder-plus` | 限时特价 | 0.6x | $1.44 | $5.76 | 特供-HC1 | 1.32x | $3.17 | $12.67 | 4x |
| `qwen3.6-plus` | default | 1x | $2.00 | $12.00 | 纯AZ | 1.5x | $3.00 | $18.00 | 6x |
| `qwen3.7-max` | 限时特价 | 0.6x | $4.32 | $12.96 | 纯AZ | 1.5x | $10.80 | $32.40 | 3x |
| `glm-4.6` | 限时特价 | 0.6x | $0.72 | $2.88 | 纯AZ | 1.5x | $1.80 | $7.20 | 4x |
| `glm-4.5` | 限时特价 | 0.6x | $0.58 | $2.30 | 纯AZ | 1.5x | $1.44 | $5.76 | 4x |
| `glm-4.5-air` | 限时特价 | 0.6x | $0.29 | $2.16 | 纯AZ | 1.5x | $0.72 | $5.40 | 7.5x |
| `kimi-k2` | enterprise-a… | 0.45x | $0.81 | $3.24 | 特供-优质gpt | 5.6x | $10.08 | $40.32 | 4x |
| `kimi-k2.5` | 特供-国产4折 | 0.8x | $2.56 | $13.44 | 纯AZ | 1.5x | $4.80 | $25.20 | 5.25x |
| `kimi-k3` | 纯AZ | 1.5x | $45.00 | $225.00 | 官转 | 3x | $90.00 | $450.00 | 5x |

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

1. Visit [Levolink AI](https://ai.levolink.com) -> Register -> Console -> Create Key
2. Top up (min 1 yuan)
3. Choose your integration method:

### Python (OpenAI SDK)

```python
from openai import OpenAI

client = OpenAI(
    api_key="***",
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
  -H "Authorization: Bearer ***" \
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

echo 'export ANTHROPIC_AUTH_TOKEN="***"' >> ~/.bash_profile
echo 'export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"' >> ~/.bash_profile
source ~/.bash_profile

cd your-project && claude
```

### OpenAI Codex

```bash
npm install -g @openai/codex
export OPENAI_API_KEY="***"
export OPENAI_API_BASE="https://ai.levolink.com/v1"
```

### Gemini CLI

```bash
npm install -g @google/gemini-cli
export GEMINI_API_KEY="***"
export GEMINI_API_BASE="https://ai.levolink.com/v1"
```

### Tool Integrations

| Tool | Setup |
|------|-------|
| **Dify / FastGPT** | API Key + Base URL: `https://ai.levolink.com/v1` |
| **n8n** | HTTP Request -> URL: `https://ai.levolink.com/v1/chat/completions` |
| **LangChain** | `ChatOpenAI(openai_api_key="key", openai_api_base="https://ai.levolink.com/v1")` |
| **NextChat** | Settings -> Custom API -> URL: `https://ai.levolink.com/v1` |
| **Cursor IDE** | Settings -> Env Vars -> `ANTHROPIC_BASE_URL=https://ai.levolink.com/v1` |
| **OpenClaw** | `openai_api_key: key` + `openai_api_base: https://ai.levolink.com/v1` |

### Use Cases

- **AI Coding** - Claude Code / Codex with Claude 4.8 / GPT-5.6 for refactoring, bug fixes
- **Long Document Processing** - 100K+ word analysis, contract review, paper summarization
- **AI Agents** - One key for all models, multi-agent parallel tasks
- **RAG Knowledge Bases** - DeepSeek / GPT with vector databases for enterprise Q&A
- **Automated Workflows** - n8n / FastGPT / Dify integration for full automation

---

## 📊 Comparison

| | [Levolink AI](https://ai.levolink.com) | SiliconFlow | Other Proxies | Self-Built |
|--|-------------|-------------|---------------|------------|
| Model count | **500+** | ~200 | ~100 | Manual |
| Group options | **33 groups** | None | 1-3 | - |
| China CDN | ✅ Multi-node | ✅ Single | ✅ | ❌ |
| Min top-up | **1 yuan** | 50 yuan | 20 yuan | - |
| Pay-as-you-go | ✅ | ✅ | ✅ | ❌ |
| Claude Code ready | ✅ | ✅ | ✅ | ❌ |
| OpenAI compatible | ✅ | ✅ | ✅ | Needs adapter |
| Price transparency | ✅ 33 groups | Single price | Single price | - |
| Invoice | ✅ | ✅ | ❌ | - |
| GitHub open source | ✅ Auto-pricing | ❌ | ❌ | - |

---

## ❓ FAQ

**Are responses identical to the official API?**

Yes. Levolink AI only forwards requests to official models - responses are byte-for-byte identical.

**Can my account get banned?**

No. You use Levolink AI's key, not the official account system - no ban risk.

**What's the difference between groups?**

Different groups correspond to different backend channels (Azure/AWS/Vertex/Official Direct, etc.) with varying quality and price. Lower-cost groups offer better value; higher-priced groups offer maximum stability. Start with the default group, then adjust as needed.

**Is streaming supported?**

Yes, all models support `stream: true` with low latency.

**How fast is it from China?**

China CDN nodes, latency typically 40-200ms - much faster than connecting to official APIs directly.

**Is there a free tier?**

New users get trial credits. Start free, top up when ready.

**Can I get an invoice?**

Yes. Settings -> Identity Verification -> Wallet -> Invoice. E-invoice issued within 5 business days.

**Which group should I choose?**

- Budget: Flash Sale (0.6x) / Codex Exclusive (0.8x)
- Balanced: Default (1.0x)
- High quality: Claude Code Exclusive (2.4x) / Azure (3.0x)
- Maximum quality: Vertex (6.0x) / Official Premium (16.0x)

---

## 🤝 Contributing

- 🐛 Bug report -> [Open an Issue](https://github.com/jiaqing77cn/levolink-ai-api/issues)
- 📝 Improve docs -> Submit a PR
- 💡 Feature request -> [Start a Discussion](https://github.com/jiaqing77cn/levolink-ai-api/discussions)
- 📄 Contributing guide -> See [CONTRIBUTING.md](./CONTRIBUTING.md)
- 📋 Changelog -> See [CHANGELOG.md](./CHANGELOG.md)

### Recommended GitHub Topics

Add these Topics in repo Settings to improve discoverability:

```
ai-api api-proxy claude gpt openai gemini deepseek api-relay china llm-gateway claude-code
```

---

## 📈 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=jiaqing77cn/levolink-ai-api&type=Date)](https://star-history.com/#jiaqing77cn/levolink-ai-api&Date)

---

## 📜 License

MIT License · Copyright (c) 2026 [Levolink AI](https://ai.levolink.com)
