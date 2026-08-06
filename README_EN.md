<h1 align="center">🚀 AI API Proxy in China Without VPN | Claude/GPT/Gemini/DeepSeek | Levolink AI</h1>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License"/>
  <img src="https://img.shields.io/badge/500%2B-Models-34d399?style=flat" alt="Models"/>
  <img src="https://img.shields.io/badge/CDN-China%20Accel-3b82f6?style=flat" alt="CDN"/>
  <img src="https://img.shields.io/badge/OpenAI-Compatible-10a37f?style=flat" alt="OpenAI Compatible"/>
</p>

<div align="center">

**No VPN · Low Latency · 500+ Models · OpenAI Compatible · Claude Code Ready**

[🌐 Website](https://ai.levolink.com) · [📋 Pricing](https://ai.levolink.com/pricing) · [📖 API Docs](https://levolink.apifox.cn/) · [💬 Contact](https://ai.levolink.com)

</div>

> Last updated: 2026-08-06 22:26 (UTC+8)| [中文](./README.md) | [한국어](./README_KO.md) | [日本語](./README_JA.md) | [Español](./README_ES.md) | [Deutsch](./README_DE.md) | English

---

## 📋 Table of Contents

- [🖥️ Product Preview](#-product-preview)
- [🔍 How to Choose an API Proxy](#-how-to-choose-an-api-proxy)
- [💰 Live Model Pricing](#-live-model-pricing)
- [🛠️ Integration Guide](#-integration-guide)
- [📊 Comparison](#-comparison)
- [❓ FAQ](#-faq)
- [📖 In-Depth Guides](#-in-depth-guides)
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
| `gpt-5-codex` | Enterprise Azure 2 | 0.35x | $0.44 | $3.50 | Codex Exclusive | 0.8x | $1.00 | $8.00 | 8x |
| `gpt-5-mini` | Enterprise Azure 2 | 0.35x | $0.09 | $0.70 | Special-Premium GPT | 5.6x | $1.40 | $11.20 | 8x |
| `gpt-5-mini-2025-08-07` | Enterprise Azure 2 | 0.35x | $0.09 | $0.70 | Special-Premium GPT | 5.6x | $1.40 | $11.20 | 8x |
| `gpt-5-nano` | Enterprise Azure 2 | 0.35x | $0.02 | $0.14 | Special-Premium GPT | 5.6x | $0.28 | $2.24 | 8x |
| `gpt-5-nano-2025-08-07` | Enterprise Azure 2 | 0.35x | $0.02 | $0.14 | Special-Premium GPT | 5.6x | $0.28 | $2.24 | 8x |
| `gpt-5-pro` | Enterprise Azure 2 | 0.35x | $5.25 | $42.00 | Special-Premium GPT | 5.6x | $84.00 | $672.00 | 8x |
| `gpt-5.1-codex` | Sale 10% Off | 0.54x | $0.68 | $5.40 | Codex Exclusive | 0.8x | $1.00 | $8.00 | 8x |
| `gpt-5.1-codex-max` | Sale 10% Off | 0.54x | $0.68 | $5.40 | Pure Azure | 1.5x | $1.88 | $15.00 | 8x |
| `gpt-5.1-codex-mini` | Sale 10% Off | 0.54x | $0.14 | $1.08 | Pure Azure | 1.5x | $0.38 | $3.00 | 8x |
| `gpt-5.2-chat` | Enterprise Azure 2 | 0.35x | $0.61 | $4.90 | Special-Premium GPT | 5.6x | $9.80 | $78.40 | 8x |
| `gpt-5.2-chat-latest` | Enterprise Azure 2 | 0.35x | $0.61 | $4.90 | Special-Premium GPT | 5.6x | $9.80 | $78.40 | 8x |
| `gpt-5.2-codex` | Sale 10% Off | 0.54x | $0.95 | $7.56 | Special-Premium GPT | 5.6x | $9.80 | $78.40 | 8x |
| `gpt-5.3-chat-latest` | Enterprise Azure 2 | 0.35x | $0.61 | $4.90 | Special-Premium GPT | 5.6x | $9.80 | $78.40 | 8x |
| `gpt-5.3-codex` | Sale 10% Off | 0.54x | $0.95 | $7.56 | Special-Premium GPT | 5.6x | $9.80 | $78.40 | 8x |
| `gpt-5.3-codex-spark` | Codex Exclusive | 0.8x | $1.40 | $11.20 | Premium OpenAI | 8x | $14.00 | $112.00 | 8x |

<!-- GPT_PRICE_TABLE_END -->

### Anthropic Claude Series

<!-- CLAUDE_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `claude-fable-5` | Default | 1x | $10.00 | $50.00 | Claude Code Exclusive | 2.4x | $24.00 | $120.00 | 5x |
| `claude-haiku-4-5-20251001` | Default | 1x | $1.00 | $5.00 | Claude Code Exclusive | 2.4x | $2.40 | $12.00 | 5x |
| `claude-opus-4-1-20250805` | Default | 1x | $15.00 | $75.00 | Relay Claude 1 | 4x | $60.00 | $300.00 | 5x |
| `claude-opus-4-5-20251101` | Default | 1x | $5.00 | $25.00 | Claude Code Exclusive | 2.4x | $12.00 | $60.00 | 5x |
| `claude-opus-4-6` | Default | 1x | $5.00 | $25.00 | Claude Code Exclusive | 2.4x | $12.00 | $60.00 | 5x |
| `claude-opus-4-7` | Default | 1x | $5.00 | $25.00 | Claude Code Exclusive | 2.4x | $12.00 | $60.00 | 5x |
| `claude-opus-4-8` | Default | 1x | $5.00 | $25.00 | Claude Code Exclusive | 2.4x | $12.00 | $60.00 | 5x |
| `claude-sonnet-4-20250514` | Default | 1x | $3.00 | $15.00 | Relay Claude 1 | 4x | $12.00 | $60.00 | 5x |
| `claude-sonnet-4-5-20250929` | Default | 1x | $3.00 | $15.00 | Claude Code Exclusive | 2.4x | $7.20 | $36.00 | 5x |
| `claude-sonnet-4-6` | Default | 1x | $3.00 | $15.00 | Claude Code Exclusive | 2.4x | $7.20 | $36.00 | 5x |
| `claude-sonnet-5` | Default | 1x | $2.00 | $10.00 | Claude Code Exclusive | 2.4x | $4.80 | $24.00 | 5x |

<!-- CLAUDE_PRICE_TABLE_END -->

### Google Gemini Series

<!-- GEMINI_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `gemini-2.0-flash-lite` | Relay Gemini | 3.6x | $0.27 | $1.08 | Premium Gemini | 6x | $0.45 | $1.80 | 4x |
| `gemini-2.5-flash` | Gemini CLI | 1x | $0.30 | $2.50 | Premium Gemini | 6x | $1.80 | $15.01 | 8.34x |
| `gemini-2.5-flash-image` | Premium Gemini | 2.4x | $0.00 | $0.00 | Premium Gemini | 6x | $0.00 | $0.00 | 0x |
| `gemini-2.5-flash-lite` | Gemini CLI | 1x | $0.10 | $0.40 | Premium Gemini | 6x | $0.60 | $2.40 | 4x |
| `gemini-2.5-pro` | Gemini CLI | 1x | $1.25 | $10.00 | Premium Gemini | 6x | $7.50 | $60.00 | 8x |
| `gemini-3-pro-image` | Premium Gemini | 2.4x | $0.00 | $0.00 | Premium Gemini | 6x | $0.00 | $0.00 | 0x |
| `gemini-3.1-flash-image` | Premium Gemini | 2.4x | $0.00 | $0.00 | Premium Gemini | 6x | $0.00 | $0.00 | 0x |
| `gemini-3.1-flash-lite` | Gemini CLI | 1x | $0.25 | $1.50 | Premium Gemini | 6x | $1.50 | $9.00 | 6x |

<!-- GEMINI_PRICE_TABLE_END -->

### DeepSeek Series

<!-- DEEPSEEK_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `deepseek-r1` | UChat Qwen | 0.6x | $2.40 | $9.60 | Pure Azure | 1.5x | $6.00 | $24.00 | 4x |
| `deepseek-r1-0528` | UChat Qwen | 0.6x | $2.40 | $9.60 | Pure Azure | 1.5x | $6.00 | $24.00 | 4x |
| `deepseek-r1-2025-01-20` | UChat Qwen | 0.6x | $2.40 | $9.60 | Pure Azure | 1.5x | $6.00 | $24.00 | 4x |
| `deepseek-r1-250120` | UChat Qwen | 0.6x | $2.40 | $9.60 | Pure Azure | 1.5x | $6.00 | $24.00 | 4x |
| `deepseek-r1-250528` | UChat Qwen | 0.6x | $2.40 | $9.60 | Pure Azure | 1.5x | $6.00 | $24.00 | 4x |
| `deepseek-r1-distill-qwen-32b` | Special-Domestic 40% | 0.8x | $1.60 | $4.80 | Pure Azure | 1.5x | $3.00 | $9.00 | 3x |
| `deepseek-r1-distill-qwen-7b` | Special-Domestic 40% | 0.8x | $0.40 | $0.80 | Pure Azure | 1.5x | $0.75 | $1.50 | 2x |
| `deepseek-reasoner` | UChat Qwen | 0.6x | $2.40 | $9.60 | Pure Azure | 1.5x | $6.00 | $24.00 | 4x |

<!-- DEEPSEEK_PRICE_TABLE_END -->

### Chinese Models (Qwen/Doubao/GLM/Kimi/MiniMax)

<!-- CN_MODEL_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `qwen3-max` | Flash Sale | 0.6x | $1.50 | $6.00 | Pure Azure | 1.5x | $3.75 | $15.00 | 4x |
| `qwen3-max-2026-01-23` | Alibaba 40% | 0.8x | $2.00 | $8.00 | Pure Azure | 1.5x | $3.75 | $15.00 | 4x |
| `qwen3-coder` | Special-Domestic 40% | 0.8x | $4.80 | $19.20 | Pure Azure | 1.5x | $9.00 | $36.00 | 4x |
| `qwen3-coder-plus` | Flash Sale | 0.6x | $2.40 | $9.60 | Special-HC1 | 1.32x | $5.28 | $21.12 | 4x |
| `qwen3.6-plus` | Default | 1x | $2.00 | $12.00 | Pure Azure | 1.5x | $3.00 | $18.00 | 6x |
| `qwen3.7-max` | Flash Sale | 0.6x | $7.20 | $21.60 | Pure Azure | 1.5x | $18.00 | $54.00 | 3x |
| `glm-4.6` | Flash Sale | 0.6x | $1.20 | $4.80 | Pure Azure | 1.5x | $3.00 | $12.00 | 4x |
| `glm-4.5` | Flash Sale | 0.6x | $0.96 | $3.84 | Pure Azure | 1.5x | $2.40 | $9.60 | 4x |
| `glm-4.5-air` | Flash Sale | 0.6x | $0.48 | $3.60 | Pure Azure | 1.5x | $1.20 | $9.00 | 7.5x |
| `kimi-k2` | Special-Domestic 40% | 0.8x | $3.20 | $12.80 | Special-Premium GPT | 5.6x | $22.40 | $89.60 | 4x |
| `kimi-k2.5` | Special-Domestic 40% | 0.8x | $3.20 | $16.80 | Pure Azure | 1.5x | $6.00 | $31.50 | 5.25x |
| `kimi-k3` | Pure Azure | 1.5x | $30.00 | $150.00 | Official Relay | 3x | $60.00 | $300.00 | 5x |

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
   - Alipay / WeChat Pay / Crypto Pay / Stripe / Global Pay
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

Full examples in [`examples/`](./examples/) directory (incl. [Python](examples/quickstart.py) / [Node.js](examples/quickstart.js) / [Shell](examples/quickstart.sh)).

### Claude Code

```bash
npm install -g @anthropic-ai/claude-code

echo 'export ANTHROPIC_AUTH_TOKEN="***"' >> ~/.bash_profile
echo 'export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"' >> ~/.bash_profile
source ~/.bash_profile

cd your-project && claude
```

📖 Full guide: [Claude Code Setup](docs/en/claude-code-guide.md)

### OpenAI Codex

```bash
npm install -g @openai/codex
export OPENAI_API_KEY="***"
export OPENAI_API_BASE="https://ai.levolink.com/v1"
```

📖 Full guide: [Codex Setup](docs/en/codex-setup.md)

### Gemini CLI

```bash
npm install -g @google/gemini-cli
export GEMINI_API_KEY="***"
export GEMINI_API_BASE="https://ai.levolink.com/v1"
```

📖 Full guide: [Cursor IDE Setup](docs/en/cursor-setup.md) (also applies to Gemini CLI)

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

## 📊 2026 Comparison & Review

> Based on publicly available information as of 2026-07-29. For reference only.

| | [Levolink AI](https://ai.levolink.com) | OpenRouter | SiliconFlow | Other Proxies | Self-Built |
|--|-------------|-----------|-------------|---------------|------------|
| Model count | **228+** | ~400 | ~200 | ~100 | Manual |
| Group options | **33 groups** | None (per-provider) | None | 1-3 | - |
| China CDN | ✅ Multi-node | ❌ No China nodes | ✅ Single | ✅ | ❌ |
| Min top-up | **¥1** | ~¥35 | ¥50 | ¥20 | - |
| Pay-as-you-go | ✅ | ✅ | ✅ | ✅ | ❌ |
| Claude Code ready | ✅ | ✅ | ✅ | ✅ | ❌ |
| OpenAI compatible | ✅ | ✅ | ✅ | ✅ | Needs adapter |
| Price transparency | ✅ 33 groups | Per-model, limited choice | Single price | Single price | - |
| Invoice | ✅ | ❌ No CN invoice | ✅ | ❌ | - |
| GitHub open source | ✅ Auto-pricing | ❌ | ❌ | ❌ | - |

---

## ❓ FAQ

**Are responses identical to the official API?**

Yes. Levolink AI only forwards requests to official models - responses are consistent with the official API.

**Can my account get banned?**

No. You use Levolink AI's key, not the official account system - your official account is not at risk.

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

## 📖 In-Depth Guides

| Guide | Content |
|-------|---------|
| [Claude Code Setup Guide](docs/en/claude-code-guide.md) | Complete Claude Code configuration for China |
| [Claude Desktop Guide](docs/en/claude-desktop-guide.md) | Configure Claude Desktop with Levolink AI |
| [Codex Setup Guide](docs/en/codex-setup.md) | OpenAI Codex CLI configuration for China |
| [Gemini CLI Guide](docs/en/gemini-cli-guide.md) | Gemini CLI with Levolink AI for Gemini models |
| [Cursor IDE Setup](docs/en/cursor-setup.md) | Use GPT-5.6 / Claude 4.8 / Gemini in Cursor |
| [Grok Build Guide](docs/en/grok-build-guide.md) | xAI Grok Build with custom Levolink AI models |
| [OpenCode Guide](docs/en/opencode-guide.md) | OpenCode open-source agent with Levolink AI |
| [OpenClaw Guide](docs/en/openclaw-guide.md) | OpenClaw Agent runtime with Levolink AI |
| [CC Switch Guide](docs/en/cc-switch-guide.md) | Unified config management for multiple AI tools |
| [Dify Integration Guide](docs/en/dify-integration.md) | Connect Dify with Levolink AI |
| [Model Selection Guide](docs/en/model-selection-guide.md) | Which of 228 models to choose? By use case & budget |
| [Fraud Detection Guide](docs/en/fraud-detection-guide.md) | 5 methods to detect model swapping in API proxies |
| [Cost Calculator Guide](docs/en/cost-calculator-guide.md) | Estimate API costs and optimize spending |

---

## 🤝 Contributing

- 🐛 Bug report -> [Open an Issue](https://github.com/jiaqing77cn/levolink-ai-api/issues)
- 📝 Improve docs -> Submit a PR
- 💡 Feature request -> [Start a Discussion](https://github.com/jiaqing77cn/levolink-ai-api/discussions)
- 📄 Contributing guide -> See [CONTRIBUTING.md](./CONTRIBUTING.md)
- 📋 Changelog -> See [CHANGELOG.md](./CHANGELOG.md)

---

## 📜 License

MIT License · Copyright (c) 2026 [Levolink AI](https://ai.levolink.com)

## 📢 Trademark Notice

GPT and OpenAI are trademarks of OpenAI. Claude is a trademark of Anthropic PBC. Gemini is a trademark of Google LLC. DeepSeek is a trademark of DeepSeek. This repository describes compatibility only and does not imply official affiliation with or endorsement by these companies.
