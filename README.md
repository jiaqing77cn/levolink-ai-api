# 乐沃联AI API中转站

<div align="center">

<p align="center">
  <img src="https://img.shields.io/github/stars/jiaqing77cn/levolink-ai-api?style=social" alt="Stars"/>
  <img src="https://img.shields.io/github/forks/jiaqing77cn/levolink-ai-api?style=social" alt="Forks"/>
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License"/>
  <img src="https://img.shields.io/badge/Models-500%2B-34d399?style=flat" alt="Models"/>
  <img src="https://img.shields.io/badge/CDN-国内加速-3b82f6?style=flat" alt="CDN"/>
</p>

**国内稳定直连 · 500+模型聚合 · OpenAI兼容格式 · Claude Code即插即用**

[🌐 官网](https://ai.levolink.com) · [📋 价格表](https://ai.levolink.com/pricing) · [📖 API文档](https://levolink.apifox.cn/) · [💬 加入交流](https://ai.levolink.com)

> 适用于：Claude Code / Cursor / Dify / FastGPT / n8n / LangChain / NextChat / Cherry Studio / Open Interpreter 等所有兼容 OpenAI API 的工具。

</div>

---

## 🎯 一句话说明

**乐沃联AI API中转站** — 帮国内开发者无需翻墙、稳定低延迟地调用 **Claude / GPT / Gemini / DeepSeek** 等 500+ 全球顶尖 AI 模型，一行配置即可接入。

---

## 📡 支持模型一览

| 厂商 | 热门模型 | 状态 |
|------|---------|------|
| **OpenAI** | GPT-5、GPT-4o、GPT-4o-mini、GPT-4、GPT-3.5 Turbo | ✅ |
| **Anthropic** | Claude Opus 4.7、Claude Sonnet 4.6、Claude Haiku 4.6 | ✅ |
| **Google** | Gemini 2.5 Pro、Gemini 2.0 Flash、Gemini 1.5 Pro | ✅ |
| **DeepSeek** | DeepSeek-V4、DeepSeek-Coder、DeepSeek-R1 | ✅ |
| **国产** | Qwen3、豆包、智谱GLM、硅基流动、Kimi、MiniMax | ✅ |
| **图/视频/音乐** | Midjourney、Suno、Sora、Flux、Veo 3 | ✅ |

---

## 🚀 快速开始

### 第一步：获取 API Key

访问 [ai.levolink.com](https://ai.levolink.com) → 注册 → 控制台创建 Key → 充值（最低 1 元起）

### 第二步：接入代码

```python
from openai import OpenAI

client = OpenAI(
    api_key="你的API Key",                    # 👈 替换这里
    base_url="https://ai.levolink.com/v1"    # 👈 替换这里
)

# ✅ GPT-4o
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "用Python写一个快速排序"}]
)

# ✅ Claude Sonnet 4.6
response = client.chat.completions.create(
    model="claude-sonnet-4-20250514",
    messages=[{"role": "user", "content": "解释量子纠缠"}],
    extra_body={"anthropic_version": "vertex-2023-10-01"}
)

# ✅ DeepSeek R1 推理模型
response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[{"role": "user", "content": "用Python实现一个web服务器"}]
)

print(response.choices[0].message.content)
```

### 第三步：Claude Code（3 分钟配置）

```bash
# 1. 安装
npm install -g @anthropic-ai/claude-code

# 2. 配置环境变量
echo 'export ANTHROPIC_AUTH_TOKEN="你的API Key"' >> ~/.bash_profile
echo 'export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"' >> ~/.bash_profile
source ~/.bash_profile

# 3. 启动 Claude Code
cd your-project && claude
```

---

## 🖥️ 主流工具接入

| 工具 | 配置要点 |
|------|---------|
| **Cursor IDE** | `ANTHROPIC_API_KEY=xxx` + `ANTHROPIC_BASE_URL=https://ai.levolink.com/v1` |
| **Dify / FastGPT** | API Key + Base URL：`https://ai.levolink.com/v1` |
| **n8n** | HTTP Request → URL：`https://ai.levolink.com/v1/chat/completions` |
| **LangChain** | `ChatOpenAI(openai_api_key=xxx, openai_api_base="https://ai.levolink.com/v1")` |
| **NextChat** | 自定义 API → URL：`https://ai.levolink.com/v1` |

> 💡 所有工具均使用 OpenAI 兼容格式，**只需修改 base_url**，SDK 代码零改动。

---

## 💡 典型使用场景

### 🤖 AI 编程助手

```python
# Claude Code / Cursor 中配置后，直接用 Claude 4.7 进行代码重构
# 代码分析、长上下文处理、注释补全 — 全部稳定流畅
```

### 📊 自动化工作流

```python
# n8n / FastGPT / Dify 中接入，直接调用 GPT-4o / Claude
# 客服机器人、数据分析、内容生成 — 全流程自动化
```

### 📝 长文本处理

```python
# 10 万字文档分析、合同审核、论文总结
# Claude Opus 4.7 超长上下文能力，官方中转速度慢且不稳定
# 乐沃联AI国内CDN加速，响应时间缩短 3-10 倍
```

### 🔬 RAG 与知识库

```python
# DeepSeek / GPT-4o 结合向量数据库
# 企业知识库问答、智能客服、内容检索
# 一个 API Key 搞定所有模型切换
```

---

## 📊 横向对比

| 维度 | 乐沃联AI | 硅基流动 | 神马中转 | 自建代理 |
|------|---------|---------|---------|---------|
| 模型数量 | **500+** | 较少 | 较少 | 需手动维护 |
| 国内CDN | ✅ | 一般 | ✅ | ❌ |
| 最低充值 | **1元** | 较高 | 较高 | — |
| 按量计费 | ✅ | ✅ | ✅ | ❌（服务器成本） |
| Claude Code 兼容 | ✅ | ✅ | ✅ | ❌ |
| OpenAI 格式兼容 | ✅ | ✅ | ✅ | 需适配 |

> 📋 查看完整价格表：[ai.levolink.com/pricing](https://ai.levolink.com/pricing)

---

## ❓ 常见问题

**Q：响应内容和官方一致吗？**  
A：完全一致。乐沃联AI仅做请求转发，底层调用的就是官方模型，响应内容与官方 API 完全相同。

**Q：会被封号吗？**  
A：不会。你使用的是乐沃联AI的 Key，不走官方账号体系，无封号风险。

**Q：支持 streaming 吗？**  
A：支持。所有模型均支持流式输出，实时性好。

**Q：国内访问速度如何？**  
A：采用国内 CDN 节点加速，延迟通常在 40-200ms，远低于直连官方的数百毫秒。

**Q：有免费额度吗？**  
A：新用户注册赠送体验额度，可先试用再决定。

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

- 🐛 发现 Bug → 提交 [Issue](https://github.com/jiaqing77cn/levolink-ai-api/issues)
- 📝 优化文档 → 直接提交 PR
- 💡 新功能建议 → 提交 [Discussion](https://github.com/jiaqing77cn/levolink-ai-api/discussions)

---

## 📈 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=jiaqing77cn/levolink-ai-api&type=Date)](https://star-history.com/#jiaqing77cn/levolink-ai-api&Date)

---

## 📦 赞助商

*如果您或您的公司使用此项目，欢迎[联系我们](https://ai.levolink.com)赞助支持。*

---

## 📜 License

MIT License · Copyright (c) 2026 乐沃联AI

---

<div align="center">

**有帮助的话，点个 ⭐ 支持一下！**

📦 官网：[ai.levolink.com](https://ai.levolink.com)  
📂 仓库：[github.com/jiaqing77cn/levolink-ai-api](https://github.com/jiaqing77cn/levolink-ai-api)  
📖 文档：[levolink.apifox.cn](https://levolink.apifox.cn/)

</div>