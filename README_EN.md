<!--
SEO Keywords: AI API proxy, Claude API proxy, GPT API proxy, OpenAI proxy,
LLM gateway, LLM API, API middleware, AI forwarding, model gateway,
500+ AI models, DeepSeek API, Gemini API, Anthropic API, Claude Code,
OpenAI compatible, China API access, without VPN, pay-per-token, streaming API,
API中转站, Claude API中转, GPT API中转, 中转API, API转发,
国内直连, 免翻墙API, 大模型API, 聚合API, 大模型聚合,
AI代理, Claude中转, GPT中转, OpenAI代理, 低价API
Description: AI API proxy for China — access 500+ models (Claude/GPT/Gemini/DeepSeek) without VPN. OpenAI-compatible, low latency, Claude Code ready. 大模型聚合API中转站，免翻墙国内直连。
-->

<h1 align="center">AI API Proxy — Claude/GPT/Gemini/DeepSeek for China | Levolink AI</h1>

<div align="center">

![Stars](https://img.shields.io/github/stars/jiaqing77cn/levolink-ai-api?style=social)
![Forks](https://img.shields.io/github/forks/jiaqing77cn/levolink-ai-api?style=social)
![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Models](https://img.shields.io/badge/500%2B-Models-34d399?style=flat)
![CDN](https://img.shields.io/badge/CDN-China%20加速-3b82f6?style=flat)
![OpenAI Compatible](https://img.shields.io/badge/OpenAI-Compatible-10a37f?style=flat)

**Stable China Access · 500+ Models · OpenAI Compatible · Claude Code Ready**

[🌐 Levolink AI Website](https://ai.levolink.com) · [📋 Pricing](https://ai.levolink.com/pricing) · [📖 API Docs](https://levolink.apifox.cn/) · [💬 Contact](https://ai.levolink.com)

> Works with: Claude Code / Cursor / Dify / FastGPT / n8n / LangChain / NextChat / Cherry Studio / Open Interpreter

</div>

---

## 🌐 Product Preview

![Levolink AI homepage — 500+ AI model API proxy dashboard](https://raw.githubusercontent.com/jiaqing77cn/levolink-ai-api/main/assets/homepage.jpg)

---

## 🎯 What Is This?

A **Claude/GPT API proxy** that helps developers in China access Claude, GPT, Gemini, DeepSeek and 500+ other AI models — **without a VPN, at low latency**. One config change, ready to go.

---

## 📡 Supported Models

| Provider | Popular Models |
|----------|---------------|
| **OpenAI** | GPT-5, GPT-4o, GPT-4o-mini, GPT-4, GPT-3.5 Turbo |
| **Anthropic** | Claude Opus 4.7, Claude Sonnet 4.6, Claude Haiku 4.6 |
| **Google** | Gemini 2.5 Pro, Gemini 2.0 Flash, Gemini 1.5 Pro |
| **DeepSeek** | DeepSeek-V4, DeepSeek-Coder, DeepSeek-R1 |
| **Chinese Models** | Qwen3, Doubao, Zhipu GLM, Kimi, MiniMax, SiliconFlow |
| **Image/Video/Audio** | Midjourney, Suno, Sora, Flux, Veo 3 |

---

## 🚀 Quick Start

Get your API key at [Levolink AI platform](https://ai.levolink.com) → Register → Console → Create Key → Top up (min 1 yuan)

### Python

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-api-key",
    base_url="https://ai.levolink.com/v1"
)

# GPT-4o
resp = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Write a Python quicksort"}]
)

# Claude Sonnet 4.6
resp = client.chat.completions.create(
    model="claude-sonnet-4-20250514",
    messages=[{"role": "user", "content": "Explain quantum entanglement"}],
    extra_body={"anthropic_version": "vertex-2023-10-01"}
)

# DeepSeek R1
resp = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[{"role": "user", "content": "Implement a web server in Python"}]
)
```

> 💡 Full code examples in [`examples/`](https://github.com/jiaqing77cn/levolink-ai-api/tree/main/examples) — Python, Node.js, curl.

---

## 🛠️ Compatible Tools

### Claude Code / Claude Desktop

```bash
# Install Claude Code
npm install -g @anthropic-ai/claude-code

# Configure environment variables
echo 'export ANTHROPIC_AUTH_TOKEN="your-api-key"' >> ~/.bash_profile
echo 'export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"' >> ~/.bash_profile
source ~/.bash_profile

# Launch
cd your-project && claude
```

> Claude Desktop: Settings → Advanced → add `ANTHROPIC_API_KEY` and `ANTHROPIC_BASE_URL=https://ai.levolink.com/v1`

### Codex

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

### OpenClaw / Hermes Agent

```bash
# openclaw.yaml
openai_api_key: your-api-key
openai_api_base: https://ai.levolink.com/v1
```

### OpenCode

```bash
pip install opencode
export OPENAI_API_KEY="your-api-key"
export OPENAI_API_BASE="https://ai.levolink.com/v1"
```

### Cursor IDE

Settings → Environment Variables:
```
ANTHROPIC_API_KEY=your-key
ANTHROPIC_BASE_URL=https://ai.levolink.com/v1
```

---

## 🖥️ Workflow Tools

| Tool | Setup |
|------|-------|
| **Dify / FastGPT** | API Key + Base URL: `https://ai.levolink.com/v1` |
| **n8n** | HTTP Request → URL: `https://ai.levolink.com/v1/chat/completions`, Header: `Authorization: Bearer your-key` |
| **LangChain** | `ChatOpenAI(openai_api_key="key", openai_api_base="https://ai.levolink.com/v1")` |
| **NextChat** | Settings → Custom API → URL: `https://ai.levolink.com/v1` |

---

## 💡 Common Use Cases

**AI Coding** — Configure Claude Code / Codex / OpenCode and use Claude 4.7 or GPT-4o for code refactoring, bug fixes, and long-context analysis with stable, fast responses.

**Long Document Processing** — 100K-word document analysis, contract review, paper summarization. Claude Opus 4.7's 200K context window, accelerated by [Levolink AI CDN](https://ai.levolink.com) — 3-10x faster than official proxies.

**AI Agents** — OpenClaw / Hermes Agent / Gemini CLI with one key for all models, supporting multi-agent parallel tasks.

**RAG & Knowledge Bases** — DeepSeek / GPT-4o with vector databases for enterprise knowledge Q&A, one key switches models on demand.

**Automated Workflows** — n8n / FastGPT / Dify integration for customer service bots, data analysis, and content generation.

---

## 📊 Comparison

| | [Levolink AI](https://ai.levolink.com) | SiliconFlow | Other Proxies | Self-Built |
|--|-------------|-------------|---------------|------------|
| Model count | **500+** | Fewer | Fewer | Manual |
| China CDN | ✅ | Average | ✅ | ❌ |
| Min top-up | **1 yuan** | Higher | Higher | — |
| Pay-as-you-go | ✅ | ✅ | ✅ | ❌ (server cost) |
| Claude Code ready | ✅ | ✅ | ✅ | ❌ |
| OpenAI format | ✅ | ✅ | ✅ | Needs adapter |

Full pricing: [Levolink AI pricing page](https://ai.levolink.com/pricing)

---

## 🖥️ Dashboard

![Levolink AI dashboard — create API keys, view usage, top up account](https://raw.githubusercontent.com/jiaqing77cn/levolink-ai-api/main/assets/console.jpg)

---

## ❓ FAQ

**Are responses identical to the official API?**  
Yes. [Levolink AI](https://ai.levolink.com) only forwards requests to the official models — responses are byte-for-byte identical.

**Can my account get banned?**  
No. You use Levolink AI's key, not the official account system — no ban risk.

**Is streaming supported?**  
Yes, all models support `stream: true` with low latency.

**How fast is it from China?**  
China CDN nodes, latency typically 40-200ms — much faster than connecting to official APIs directly.

**Is there a free tier?**  
New users get trial credits. Start free, top up when ready.

**Can I get an invoice?**  
Yes. Settings → Identity Verification → Wallet → Invoice. E-invoice issued within 5 business days.

---

## 🤝 Contributing

- 🐛 Bug report → [Open an Issue](https://github.com/jiaqing77cn/levolink-ai-api/issues)
- 📝 Improve docs → Submit a PR
- 💡 Feature request → [Start a Discussion](https://github.com/jiaqing77cn/levolink-ai-api/discussions)
- 📋 Contributing guide → See [CONTRIBUTING.md](https://github.com/jiaqing77cn/levolink-ai-api/blob/main/CONTRIBUTING.md)
- 📄 Changelog → See [CHANGELOG.md](https://github.com/jiaqing77cn/levolink-ai-api/blob/main/CHANGELOG.md)
- 🔒 Security → See [SECURITY.md](https://github.com/jiaqing77cn/levolink-ai-api/blob/main/SECURITY.md)

---

## 📈 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=jiaqing77cn/levolink-ai-api&type=Date)](https://star-history.com/#jiaqing77cn/levolink-ai-api&Date)

---

## 💰 Sponsorship

*If you or your company uses this project, [contact Levolink AI](https://ai.levolink.com) to sponsor.*

---

## 📜 License

MIT License · Copyright (c) 2026 [Levolink AI](https://ai.levolink.com)

---

<div align="center">

⭐ If this helps you, please give it a Star!

📦 Website: [Levolink AI](https://ai.levolink.com)  
📂 Repo: [levolink-ai-api on GitHub](https://github.com/jiaqing77cn/levolink-ai-api)  
📖 Docs: [Levolink API Docs](https://levolink.apifox.cn/)

</div>
