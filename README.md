# 乐沃联AI API中转站

<div align="center">

[![Stars](https://img.shields.io/github/stars/jiaqing77cn/levolink-ai-api?style=social)](https://github.com/jiaqing77cn/levolink-ai-api/stargazers)
[![Fork](https://img.shields.io/github/forks/jiaqing77cn/levolink-ai-api?style=social)](https://github.com/jiaqing77cn/levolink-ai-api/network/members)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**国内稳定直连 · 500+模型聚合 · OpenAI/Claude/Gemini/DeepSeek**

[🌐 官网](https://ai.levolink.com) · [📋 价格表](https://ai.levolink.com/pricing) · [📖 API文档](https://ai.levolink.com/docs)

</div>

---

## 为什么需要 API 中转站？

近年来，随着大模型在编程、写作、数据分析、Agent 构建等领域的深入应用，Claude、GPT、Gemini 等海外模型已成为众多开发者的核心工具。然而：

- ❌ **Anthropic/OpenAI 官方 API 无法直连** — 国内网络访问极不稳定，TLS 握手失败、请求超时、5xx 错误频发
- ❌ **账号与支付门槛高** — 需要海外手机号、海外信用卡，企业账号审核流程复杂
- ❌ **Claude Code 等工具无法直接配置** — IDE 插件、自动化工具、CLI 工具不支持复杂代理

**API 中转站 = 国内可直连的 AI API 转发服务**，只需一行配置，直接使用。

---

## 为什么选择乐沃联AI？

### 🏆 核心优势

| 维度 | 乐沃联AI | 自建代理 |
|------|---------|---------|
| 稳定性 | ⭐⭐⭐⭐⭐ 专业多线路负载 | ⭐⭐ 依赖跨境网络 |
| 成本 | 可控，按量计费 | 隐性成本高（服务器+维护） |
| 延迟 | 国内CDN加速，低延迟 | 不稳定 |
| 模型更新 | 同步官方最新模型 | 手动维护 |
| 风控 | 专业处理 | 高风险 |

### 📡 模型覆盖

- **OpenAI**: GPT-5、GPT-4o、GPT-4、GPT-3.5 Turbo
- **Claude**: Claude 4.5 / Opus 4.7 / Sonnet 4.6 / Haiku 4.6
- **Gemini**: Gemini 2.5 / Gemini 2.0 / Gemini 1.5
- **DeepSeek**: DeepSeek-V4 / DeepSeek-Coder / DeepSeek-R1
- **国产模型**: Qwen3 / 豆包 / 智谱 / Kimi / 硅基流动
- **图像/视频/音乐**: Midjourney、Suno、Sora、Flux、Veo 3
- **总计**: 500+ 模型，一个平台全搞定

### 🔌 兼容所有主流工具

```
OpenClaw / Claude Code / Cursor / Dify / FastGPT / n8n / 
LangChain / NextChat / Cherry Studio / AnythingLLM / 
Open Interpreter / Continue / Void / Codeium ...
```

OpenAI 兼容 API 格式，**替换一行代码**即可：

```python
# 官方
client = OpenAI(api_key="sk-xxx", base_url="https://api.openai.com/v1")

# 乐沃联AI（只需改这两处）
client = OpenAI(api_key="your-levolink-key", base_url="https://ai.levolink.com/v1")
```

---

## 快速开始

### 1. 获取 API Key

访问 [ai.levolink.com](https://ai.levolink.com) 注册账号，在控制台获取 API Key。

### 2. Python 调用示例

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-api-key",
    base_url="https://ai.levolink.com/v1"
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "Hello, world!"}
    ]
)
print(response.choices[0].message.content)
```

### 3. Claude 模型调用

```python
client = OpenAI(
    api_key="your-api-key",
    base_url="https://ai.levolink.com/v1"
)

response = client.chat.completions.create(
    model="claude-sonnet-4-20250514",
    messages=[
        {"role": "user", "content": "Explain quantum computing in simple terms"}
    ],
    extra_body={
        "anthropic_version": "vertex-2023-10-01"
    }
)
```

### 4. 配置 Claude Code（macOS / Linux）

```bash
# 安装 Claude Code
npm install -g @anthropic-ai/claude-code

# 配置环境变量
echo 'export ANTHROPIC_AUTH_TOKEN="your-api-key"' >> ~/.bash_profile
echo 'export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"' >> ~/.bash_profile
source ~/.bash_profile

# 启动
cd your-project && claude
```

### 5. 配置 Cursor IDE

在 Cursor 设置中添加：

```
ANTHROPIC_API_KEY=your-api-key
ANTHROPIC_BASE_URL=https://ai.levolink.com/v1
```

### 6. 配置 Dify / FastGPT

在平台 API 设置中填入：

- **API Key**: `your-api-key`
- **Base URL**: `https://ai.levolink.com/v1`

---

## 平台对比

| 平台 | 模型数量 | 国内优化 | OpenAI兼容 | 价格 |
|------|---------|---------|-----------|------|
| **乐沃联AI** | 500+ | ✅ CDN加速 | ✅ 完全兼容 | 按量计费 |
| 神马中转 | 较少 | ✅ | ✅ | 略高 |
| 硅基流动 | 一般 | 一般 | ✅ | 稍高 |

---

## 常见问题

### Q: 和官方API有什么区别？
A: 底层调用的就是官方模型，只是通过乐沃联AI的专线进行转发，**响应内容与官方完全一致**，且国内访问更稳定。

### Q: 会被官方封号吗？
A: 不会。您使用的是乐沃联AI的Key，不经过官方账号体系，无封号风险。

### Q: 支持流式输出（streaming）吗？
A: 支持，所有模型均支持 `stream: true` 流式响应。

### Q: 有免费额度吗？
A: 新用户注册送体验额度，可先试用再决定。

### Q: 如何查看账单和用量？
A: 登录 [ai.levolink.com](https://ai.levolink.com) 控制台，实时查看用量明细。

---

## 赞助/合作

如需在 README 中添加您的项目，或有其他合作需求，请提交 Issue。

---

<div align="center">

**如果对你有帮助，请点个 ⭐ 支持一下！**

</div>