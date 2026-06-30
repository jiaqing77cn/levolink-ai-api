# 乐沃联AI API中转站 | 国内稳定直连Claude/GPT/Gemini/DeepSeek

<div align="center">

[![Stars](https://img.shields.io/github/stars/jiaqing77cn/levolink-ai-api?style=social)](https://github.com/jiaqing77cn/levolink-ai-api/stargazers)
[![Fork](https://img.shields.io/github/forks/jiaqing77cn/levolink-ai-api?style=social)](https://github.com/jiaqing77cn/levolink-ai-api/network/members)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**国内CDN加速 · 500+模型聚合 · OpenAI兼容格式 · Claude Code即插即用**

[🌐 官网](https://ai.levolink.com) · [📋 价格表](https://ai.levolink.com/pricing) · [📖 API文档](https://levolink.apifox.cn/) · [💬 加入交流](https://ai.levolink.com)

> 适用于：Claude Code / Cursor / Dify / FastGPT / n8n / LangChain / NextChat / Cherry Studio / Open Interpreter 等所有兼容 OpenAI API 的工具。

</div>

---

## 📌 什么是 API 中转站？

**API 中转站**（也叫 API 代理/转发站）是一种帮助国内开发者**无需翻墙即可稳定调用海外 AI 模型 API**的服务。通过将你的请求转发到 Anthropic、OpenAI、Google 等官方接口，中转站让 Claude GPT、Gemini、DeepSeek 等全球顶级模型在国内网络环境下也能高速访问。

### 核心痛点 vs 中转站解决方案

| 痛点 | 解决方案 |
|------|---------|
| Anthropic 官方 API 国内无法直连，TLS 握手失败 | ✅ 国内 CDN 专线，延迟低至 40ms |
| 海外信用卡/手机号注册门槛高 | ✅ 国内邮箱即可注册 |
| Claude Code 等工具无法配置代理 | ✅ OpenAI 兼容格式，一行配置即用 |
| 自行搭建代理成本高、不稳定 | ✅ 专业多线路负载，99.9% 可用率 |
| 官方账号容易被封 | ✅ 使用中转站 Key，无封号风险 |

---

## 🎯 为什么选择乐沃联AI？

### ✅ 500+ 模型，一站搞定

| 厂商 | 支持模型 |
|------|---------|
| **OpenAI** | GPT-5、GPT-4o、GPT-4o-mini、GPT-4 Turbo、GPT-4、GPT-3.5 Turbo |
| **Anthropic** | Claude Opus 4.7、Claude Sonnet 4.6、Claude Haiku 4.6、Claude 4.5 系列 |
| **Google** | Gemini 2.5 Pro、Gemini 2.0 Flash、Gemini 1.5 Pro、Gemini 1.5 Flash |
| **DeepSeek** | DeepSeek-V4、DeepSeek-Coder、DeepSeek-R1、DeepSeek-V3 |
| **国产模型** | Qwen3、Qwen2.5、千问、阿里百炼、豆包、智谱 GLM、硅基流动、Kimi、MiniMax |
| **图片/视频/音乐** | Midjourney、Suno、Sora、Flux、Veo 3、DALL-E 3、Stable Diffusion |

### ✅ 全平台兼容，替换一行代码

乐沃联AI采用 **OpenAI 兼容 API 格式**，所有使用 OpenAI SDK 的代码只需修改两处即可切换：

```python
# 官方（无法直连）
from openai import OpenAI
client = OpenAI(api_key="sk-xxx", base_url="https://api.openai.com/v1")

# 乐沃联AI（国内秒连）
from openai import OpenAI
client = OpenAI(api_key="你的API Key", base_url="https://ai.levolink.com/v1")
```

### ✅ 兼容所有主流工具

```
✅ Claude Code      ✅ Cursor / Continue  ✅ Dify / FastGPT
✅ n8n / LangChain  ✅ NextChat           ✅ Cherry Studio
✅ AnythingLLM     ✅ Open Interpreter   ✅ Codeium
✅ Wordware        ✅ Seal                 ✅ Perplexity
✅ CustomGPT       ✅ Vercel AI SDK       ✅ Spring AI
```

---

## 🚀 快速开始

### 第一步：获取 API Key

1. 访问 [ai.levolink.com](https://ai.levolink.com) 注册账号
2. 登录控制台 → 创建 API Key
3. 充值余额（支持支付宝/微信，最低 5 元起充）

### 第二步：Python 调用

```python
from openai import OpenAI

client = OpenAI(
    api_key="LVK-xxxxxxxxxxxx",      # 替换为你的 Key
    base_url="https://ai.levolink.com/v1"
)

# 调用 GPT-4o
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "用Python写一个快速排序"}]
)
print(response.choices[0].message.content)
```

### 第三步：Claude 模型调用

```python
response = client.chat.completions.create(
    model="claude-sonnet-4-20250514",
    messages=[{"role": "user", "content": "解释什么是量子纠缠"}],
    extra_body={"anthropic_version": "vertex-2023-10-01"}
)
```

---

## 💻 Claude Code 配置教程（ macOS / Linux ）

```bash
# 1. 安装 Claude Code
npm install -g @anthropic-ai/claude-code

# 2. 配置环境变量（永久生效）
echo 'export ANTHROPIC_AUTH_TOKEN="你的API Key"' >> ~/.bash_profile
echo 'export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"' >> ~/.bash_profile
source ~/.bash_profile

# 3. 启动 Claude Code
cd your-project
claude
```

> 💡 **提示**：首次启动按回车选择默认配置即可，支持主题选择、安全确认、工作目录信任。

---

## 🖥️ Cursor IDE 配置

在 Cursor 设置中添加环境变量：

```bash
ANTHROPIC_API_KEY=你的API Key
ANTHROPIC_BASE_URL=https://ai.levolink.com/v1
```

或直接在 Cursor 设置 → Models 中填入自定义端点。

---

## 🔧 Dify / FastGPT 配置

在平台 API 设置中填入：

| 配置项 | 值 |
|--------|---|
| API Key | `LVK-xxxxxxxxxxxx` |
| Base URL | `https://ai.levolink.com/v1` |

Dify 示例：
```
curl https://ai.levolink.com/v1/chat/completions \
  -H "Authorization: Bearer LVK-xxx" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-4o","messages":[{"role":"user","content":"Hello"}]}'
```

---

## 📊 价格对比

| 平台 | 模型数量 | 国内优化 | 新人福利 | 计费方式 |
|------|---------|---------|---------|---------|
| **乐沃联AI** | 500+ | ✅ CDN加速 | 注册送体验额度 | 按量计费 |
| 硅基流动 | 较少 | 一般 | 有限 | 按量+套餐 |
| 神马中转 | 较少 | ✅ | 有限 | 按量计费 |

> 📋 查看完整价格表：[ai.levolink.com/pricing](https://ai.levolink.com/pricing)

---

## ❓ 常见问题

### Q：响应内容和官方一致吗？
**A：完全一致。** 乐沃联AI仅做请求转发，底层调用的就是官方模型，响应内容与官方 API 一模一样。

### Q：会被封号吗？
**A：不会。** 你使用的是乐沃联AI的 Key，不走官方账号体系，完全没有封号风险。

### Q：支持流式输出（streaming）吗？
**A：支持。** 所有模型均支持 `stream: true` 流式输出，延迟低，实时性好。

### Q：国内访问速度如何？
**A：很快。** 乐沃联AI采用国内 CDN 节点加速，国内延迟通常在 40-200ms 之间，相比直连官方数百毫秒的延迟体验提升明显。

### Q：有免费额度吗？
**A：有。** 新用户注册赠送体验额度，可先跑通流程再决定是否充值。

### Q：支持 Claude Code 吗？
**A：完全支持。** 乐沃联AI是当前国内最稳定的 Claude Code 中转方案之一，配置简单，稳定性高。

### Q：如何查看账单和用量明细？
**A：登录** [ai.levolink.com](https://ai.levolink.com) **控制台，实时查看各模型的调用次数和费用明细。**

---

## 🔄 国内调用 Claude/GPT 完整指南

### Claude 4.7 / 4.6 调用

```python
from openai import OpenAI
client = OpenAI(api_key="你的Key", base_url="https://ai.levolink.com/v1")

models = [
    "claude-opus-4-7-20250514",   # 最强模型，适合复杂任务
    "claude-sonnet-4-20250514",   # 均衡之选，性价比高
    "claude-haiku-4-20250514",    # 快速响应，适合简单任务
]

for model in models:
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": "Hello"}],
        extra_body={"anthropic_version": "vertex-2023-10-01"}
    )
    print(f"{model}: {resp.choices[0].message.content[:50]}")
```

### DeepSeek 调用

```python
resp = client.chat.completions.create(
    model="deepseek-chat",  # 或 deepseek-coder
    messages=[{"role": "user", "content": "用Python实现一个web服务器"}]
)
```

### Gemini 调用

```python
resp = client.chat.completions.create(
    model="gemini-2.0-flash",
    messages=[{"role": "user", "content": "什么是函数式编程"}]
)
```

---

## 📈 SEO 关键词

> 本仓库致力于为国内开发者提供最稳定的 Claude/GPT/Gemini/DeepSeek API 中转解决方案。相关搜索词包括：Claude API中转站、GPT API中转站、国内Claude API、Gemini API中转、DeepSeek API中转、Claude Code配置、API中转站推荐、AI API代理。

---

<div align="center">

**如果对你有帮助，请点个 ⭐ 并推荐给朋友！**

仓库地址：[github.com/jiaqing77cn/levolink-ai-api](https://github.com/jiaqing77cn/levolink-ai-api)  
官网地址：[ai.levolink.com](https://ai.levolink.com)

</div>