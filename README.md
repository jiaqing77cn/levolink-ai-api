<!--
SEO Keywords: AI API proxy, Claude API, GPT API, OpenAI compatible, China API access,
LLM gateway, API middleware, 500+ models, DeepSeek API, Gemini API, Claude Code,
API中转站, 国内直连, AI代理, Claude中转, GPT中转, OpenAI代理
Description: AI API proxy for China — access 500+ models (Claude/GPT/Gemini/DeepSeek) without VPN. OpenAI-compatible, low latency, Claude Code ready.
-->

<h1 align="center">AI API Proxy — Claude/GPT/Gemini/DeepSeek 中转站 | 乐沃联 Levolink AI</h1>

<p align="center">
  <a href="README_EN.md">📖 English README</a> ·
  <a href="https://levolink.apifox.cn/">📖 API 文档</a> ·
  <a href="https://ai.levolink.com/pricing">📋 价格</a>
</p>

<div align="center">

![Stars](https://img.shields.io/github/stars/jiaqing77cn/levolink-ai-api?style=social)
![Forks](https://img.shields.io/github/forks/jiaqing77cn/levolink-ai-api?style=social)
![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Models](https://img.shields.io/badge/500%2B-Models-34d399?style=flat)
![CDN](https://img.shields.io/badge/CDN-国内加速-3b82f6?style=flat)
![OpenAI Compatible](https://img.shields.io/badge/OpenAI-Compatible-10a37f?style=flat)

**国内稳定直连 · 500+模型聚合 · OpenAI兼容格式 · Claude Code即插即用**

[🌐 Levolink AI 官网](https://ai.levolink.com) · [📋 价格表](https://ai.levolink.com/pricing) · [📖 API文档](https://levolink.apifox.cn/) · [💬 加入交流](https://ai.levolink.com)

</div>

---

## 🌐 产品预览

![Levolink AI 首页 — 500+ AI 模型 API 中转站控制台](https://raw.githubusercontent.com/jiaqing77cn/levolink-ai-api/main/assets/homepage.jpg)

---

## 🔥 一句话说明

帮国内开发者**无需翻墙、稳定低延迟**地调用 Claude / GPT / Gemini / DeepSeek 等 500+ 全球顶尖 AI 模型。只需一行配置，立即接入。

---

## 📡 支持的模型

| 厂商 | 热门模型 |
|------|---------|
| **OpenAI** | GPT-5、GPT-4o、GPT-4o-mini、GPT-4、GPT-3.5 Turbo |
| **Anthropic** | Claude Opus 4.7、Claude Sonnet 4.6、Claude Haiku 4.6 |
| **Google** | Gemini 2.5 Pro、Gemini 2.0 Flash、Gemini 1.5 Pro |
| **DeepSeek** | DeepSeek-V4、DeepSeek-Coder、DeepSeek-R1 |
| **国产** | Qwen3、豆包、智谱GLM、Kimi、MiniMax、硅基流动 |
| **图/视频/音乐** | Midjourney、Suno、Sora、Flux、Veo 3 |

---

## 🚀 快速开始

前往 [Levolink AI 平台](https://ai.levolink.com) → 注册 → 控制台创建 Key → 充值（最低 1 元起充）

### Python 接入（通用）

```python
from openai import OpenAI

client = OpenAI(
    api_key="你的API Key",
    base_url="https://ai.levolink.com/v1"
)

# GPT-4o
resp = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "用Python写一个快速排序"}]
)

# Claude Sonnet 4.6
resp = client.chat.completions.create(
    model="claude-sonnet-4-20250514",
    messages=[{"role": "user", "content": "解释量子计算"}],
    extra_body={"anthropic_version": "vertex-2023-10-01"}
)

# DeepSeek R1
resp = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[{"role": "user", "content": "用Python实现一个web服务器"}]
)
```

> 💡 完整示例代码见 [`examples/`](examples/) 目录，包含 Python、Node.js、curl 示例。

---

## 🛠️ 支持的工具（全部兼容）

### Claude Code / Claude Desktop

```bash
# Claude Code — 安装并配置环境变量
npm install -g @anthropic-ai/claude-code

echo 'export ANTHROPIC_AUTH_TOKEN="你的API Key"' >> ~/.bash_profile
echo 'export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"' >> ~/.bash_profile
source ~/.bash_profile

# 启动
cd your-project && claude
```

> Claude Desktop 用户：设置 → Advanced Settings → 填入 `ANTHROPIC_API_KEY` 和 `ANTHROPIC_BASE_URL=https://ai.levolink.com/v1`

### Codex（ChatGPT / Cursor CLI）

```bash
# 安装 Codex
npm install -g @openai/codex

# 配置环境变量
export OPENAI_API_KEY="你的API Key"
export OPENAI_API_BASE="https://ai.levolink.com/v1"

# 或配置 ~/.config/codex/config.json：
# { "api_key": "xxx", "base_url": "https://ai.levolink.com/v1" }
```

### Gemini CLI

```bash
# 安装 Gemini CLI
npm install -g @google/gemini-cli

# 配置（通过 --api-key 和 --base-url 参数或环境变量）
export GEMINI_API_KEY="你的API Key"
export GEMINI_API_BASE="https://ai.levolink.com/v1"
```

> 注意：Gemini CLI 部分版本需通过 `--endpoint` 参数指定自定义端点

### OpenClaw / Hermes Agent

OpenClaw 和 Hermes Agent 均基于 OpenAI 兼容格式，配置方式相同：

```bash
# OpenClaw — 在配置中设置
# openclaw.yaml 或环境变量：
openai_api_key: 你的API Key
openai_api_base: https://ai.levolink.com/v1

# Hermes Agent — 同样适用
hermes config set api_key 你的API Key
hermes config set base_url https://ai.levolink.com/v1
```

### OpenCode

```bash
# 安装 OpenCode
pip install opencode

# 配置
export OPENAI_API_KEY="你的API Key"
export OPENAI_API_BASE="https://ai.levolink.com/v1"
```

### Cursor IDE

设置 → 环境变量添加：
```
ANTHROPIC_API_KEY=你的API Key
ANTHROPIC_BASE_URL=https://ai.levolink.com/v1
```

---

## 🖥️ 主流工作流工具接入

| 工具 | 配置方式 |
|------|---------|
| **Dify / FastGPT** | API 设置填入 Key + Base URL：`https://ai.levolink.com/v1` |
| **n8n** | HTTP Request → URL：`https://ai.levolink.com/v1/chat/completions`，Header：`Authorization: Bearer 你的Key` |
| **LangChain** | `ChatOpenAI(openai_api_key="Key", openai_api_base="https://ai.levolink.com/v1")` |
| **NextChat** | 设置 → 自定义 API → URL：`https://ai.levolink.com/v1` |

---

## 💡 典型使用场景

**AI 编程** — Claude Code / Codex / OpenCode 配置后，直接用 Claude 4.7 / GPT-4o 做代码重构、Bug 修复、长上下文分析，响应快，不掉线。

**长文本处理** — 10 万字文档分析、合同审核、论文总结。Claude Opus 4.7 的 200K 上下文，官方中转延迟高，[Levolink AI](https://ai.levolink.com) 国内 CDN 加速后快 3-10 倍。

**自动化 Agent** — OpenClaw / Hermes Agent / Gemini CLI 一个 Key 调度所有模型，支持多 Agent 并行，适用复杂任务拆解。

**RAG 与知识库** — DeepSeek / GPT-4o 对接向量数据库，企业知识库问答，一个 Key 按需切换模型。

**自动化工作流** — n8n / FastGPT / Dify 接入后，客服机器人、数据分析、内容生成全流程自动化。

---

## 📊 对比同类方案

| | [Levolink AI](https://ai.levolink.com) | 硅基流动 | 神马中转 | 自建代理 |
|--|---------|---------|---------|---------|
| 模型数量 | **500+** | 较少 | 较少 | 需手动维护 |
| 国内 CDN 加速 | ✅ | 一般 | ✅ | ❌ |
| 最低充值 | **1 元** | 较高 | 较高 | — |
| 按量计费 | ✅ | ✅ | ✅ | ❌（服务器成本） |
| Claude Code 兼容 | ✅ | ✅ | ✅ | ❌ |
| OpenAI 格式 | ✅ | ✅ | ✅ | 需适配 |

完整价格：[Levolink AI 定价页面](https://ai.levolink.com/pricing)

---

## 📸 价格页面

![Levolink AI 价格页面 — 按 token 量计费，最低 1 元起充](https://raw.githubusercontent.com/jiaqing77cn/levolink-ai-api/main/assets/pricing.jpg)

## 🖥️ 控制台界面

![Levolink AI 控制台 — 创建 API Key、查看用量、账户充值](https://raw.githubusercontent.com/jiaqing77cn/levolink-ai-api/main/assets/console.jpg)

---

## ❓ 常见问题

**响应内容和官方一致吗？**  
完全一致。[Levolink AI](https://ai.levolink.com) 仅做请求转发，底层调用官方模型，响应内容与官方 API 完全相同。

**会被封号吗？**  
不会。你使用的是 Levolink AI 的 Key，不走官方账号体系，无封号风险。

**支持 streaming 吗？**  
支持，所有模型均支持流式输出，延迟低，实时性好。

**国内访问速度如何？**  
采用国内 CDN 节点加速，延迟通常在 40-200ms，远低于直连官方的数百毫秒。

**有免费额度吗？**  
新用户注册赠送体验额度，可先试用再决定是否充值。

**可以开发票吗？**  
可以。个人设置→实名认证→钱包→选择开票，电子发票5个工作日内开出发送到电子邮箱。

---

## 🤝 如何贡献

- 🐛 发现 Bug → 提交 [Issue](https://github.com/jiaqing77cn/levolink-ai-api/issues)
- 📝 优化文档 → 直接提交 PR
- 💡 新功能建议 → 发起 [Discussion](https://github.com/jiaqing77cn/levolink-ai-api/discussions)

---

## 📈 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=jiaqing77cn/levolink-ai-api&type=Date)](https://star-history.com/#jiaqing77cn/levolink-ai-api&Date)

---

## 💰 赞助

*如果您或您的公司使用此项目，欢迎[联系 Levolink AI](https://ai.levolink.com)赞助支持。*

---

## 📜 License

MIT License · Copyright (c) 2026 [Levolink AI](https://ai.levolink.com)

---

<div align="center">

⭐ 如果对你有帮助，请点个 Star 支持一下！

📦 官网：[Levolink AI](https://ai.levolink.com)  
📂 仓库：[levolink-ai-api on GitHub](https://github.com/jiaqing77cn/levolink-ai-api)  
📖 文档：[Levolink API Docs](https://levolink.apifox.cn/)

</div>
