# 乐沃联AI API中转站

<div align="center">

![Stars](https://img.shields.io/github/stars/jiaqing77cn/levolink-ai-api?style=social)
![Forks](https://img.shields.io/github/forks/jiaqing77cn/levolink-ai-api?style=social)
![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Models](https://img.shields.io/badge/500%2B-Models-34d399?style=flat)
![CDN](https://img.shields.io/badge/CDN-国内加速-3b82f6?style=flat)

**国内稳定直连 · 500+模型聚合 · OpenAI兼容格式 · Claude Code即插即用**

[🌐 官网](https://ai.levolink.com) · [📋 价格表](https://ai.levolink.com/pricing) · [📖 API文档](https://levolink.apifox.cn/) · [💬 加入交流](https://ai.levolink.com)

> 适用于：Claude Code / Cursor / Dify / FastGPT / n8n / LangChain / NextChat / Cherry Studio / Open Interpreter

</div>

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

### 获取 API Key

访问 [ai.levolink.com](https://ai.levolink.com) → 注册账号 → 控制台创建 Key → 充值（最低 1 元起充）

### Python 接入

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
print(resp.choices[0].message.content)
```

### Claude 模型

```python
resp = client.chat.completions.create(
    model="claude-sonnet-4-20250514",
    messages=[{"role": "user", "content": "解释量子计算"}],
    extra_body={"anthropic_version": "vertex-2023-10-01"}
)
```

### Claude Code（3 分钟配置）

```bash
# 安装 Claude Code
npm install -g @anthropic-ai/claude-code

# 配置环境变量
echo 'export ANTHROPIC_AUTH_TOKEN="你的Key"' >> ~/.bash_profile
echo 'export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"' >> ~/.bash_profile
source ~/.bash_profile

# 启动
cd your-project && claude
```

---

## 🖥️ 主流工具接入

| 工具 | 配置方式 |
|------|---------|
| **Cursor IDE** | 设置 → 环境变量添加 `ANTHROPIC_API_KEY` 和 `ANTHROPIC_BASE_URL=https://ai.levolink.com/v1` |
| **Dify / FastGPT** | 在 API 设置中填入 Key 和 Base URL：`https://ai.levolink.com/v1` |
| **n8n** | HTTP Request 节点 → URL：`https://ai.levolink.com/v1/chat/completions`，Header 填 `Authorization: Bearer 你的Key` |
| **LangChain** | `ChatOpenAI(openai_api_key="Key", openai_api_base="https://ai.levolink.com/v1")` |
| **NextChat** | 设置 → 自定义 API → API 地址：`https://ai.levolink.com/v1`，填入 Key |

---

## 💡 典型使用场景

**AI 编程** — Claude Code / Cursor 配置后，直接用 Claude 4.7 做代码重构、Bug 修复、长上下文分析，响应速度快，不掉线。

**自动化工作流** — n8n / FastGPT / Dify 接入后，一个 Key 调用所有模型，客服机器人、数据分析、内容生成全部搞定。

**长文本处理** — 10 万字文档分析、合同审核、论文总结。Claude Opus 4.7 的 200K 上下文能力，官方中转延迟高，乐沃联AI国内 CDN 加速后快 3-10 倍。

**RAG 与知识库** — DeepSeek / GPT-4o 对接向量数据库，企业知识库问答、智能客服，一个 Key 按需切换模型。

---

## 📊 对比同类方案

| | 乐沃联AI | 硅基流动 | 神马中转 | 自建代理 |
|--|---------|---------|---------|---------|
| 模型数量 | **500+** | 较少 | 较少 | 需手动维护 |
| 国内 CDN 加速 | ✅ | 一般 | ✅ | ❌ |
| 最低充值 | **1 元** | 较高 | 较高 | — |
| 按量计费 | ✅ | ✅ | ✅ | ❌（服务器成本） |
| Claude Code 兼容 | ✅ | ✅ | ✅ | ❌ |
| OpenAI 格式 | ✅ | ✅ | ✅ | 需适配 |

完整价格：[ai.levolink.com/pricing](https://ai.levolink.com/pricing)

---

## ❓ 常见问题

**响应内容和官方一致吗？**  
完全一致。乐沃联AI仅做请求转发，底层调用官方模型，响应内容与官方 API 完全相同。

**会被封号吗？**  
不会。你使用的是乐沃联AI的 Key，不走官方账号体系，无封号风险。

**支持 streaming 吗？**  
支持，所有模型均支持流式输出，延迟低，实时性好。

**国内访问速度如何？**  
采用国内 CDN 节点加速，延迟通常在 40-200ms，远低于直连官方的数百毫秒。

**有免费额度吗？**  
新用户注册赠送体验额度，可先试用再决定是否充值。

**可以开发票吗？**  
可以，联系 [ai.levolink.com](https://ai.levolink.com) 客服咨询。

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

*如果您或您的公司使用此项目，欢迎[联系我们](https://ai.levolink.com)赞助支持。*

---

## 📜 License

MIT License · Copyright (c) 2026 乐沃联AI

---

<div align="center">

⭐ 如果对你有帮助，请点个 Star 支持一下！

📦 官网：[ai.levolink.com](https://ai.levolink.com)  
📂 仓库：[github.com/jiaqing77cn/levolink-ai-api](https://github.com/jiaqing77cn/levolink-ai-api)  
📖 文档：[levolink.apifox.cn](https://levolink.apifox.cn/)

</div>