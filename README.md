# 乐沃联AI API中转站

<div align="center">

[![Stars](https://img.shields.io/github/stars/jiaqing77cn/levolink-ai-api?style=social)](https://github.com/jiaqing77cn/levolink-ai-api/stargazers)
[![Fork](https://img.shields.io/github/forks/jiaqing77cn/levolink-ai-api?style=social)](https://github.com/jiaqing77cn/levolink-ai-api/network/members)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Model Count](https://img.shields.io/badge/500%2B-Models-34d399?style=flat)](#500-模型)](https://ai.levolink.com/pricing)
[![CN CDN](https://img.shields.io/badge/CDN-国内加速-3b82f6?style=flat)](#为什么选择乐沃联ai)

**国内稳定直连 · 500+模型聚合 · OpenAI兼容格式 · Claude Code即插即用**

[🌐 官网](https://ai.levolink.com) · [📋 价格表](https://ai.levolink.com/pricing) · [📖 API文档](https://levolink.apifox.cn/) · [💬 加入交流](https://ai.levolink.com)

> 适用于：Claude Code / Cursor / Dify / FastGPT / n8n / LangChain / NextChat / Cherry Studio / Open Interpreter 等所有兼容 OpenAI API 的工具。

</div>

---

## 🎯 一句话说明

**乐沃联AI API中转站** — 帮国内开发者无需翻墙、稳定低延迟地调用 **Claude / GPT / Gemini / DeepSeek** 等 500+ 全球顶尖 AI 模型，一行配置即可接入。

---

## ✅ 500+ 模型，覆盖所有主流厂商

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

### 1. 获取 API Key

访问 [ai.levolink.com](https://ai.levolink.com) → 注册账号 → 控制台创建 Key → 充值（最低 1 元）

### 2. Python 一行代码接入

```python
from openai import OpenAI

client = OpenAI(
    api_key="你的Key",           # 👈 替换这里
    base_url="https://ai.levolink.com/v1"  # 👈 替换这里
)

# 调用 GPT-4o
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "用Python写一个快速排序"}]
)
print(response.choices[0].message.content)
```

### 3. Claude 模型调用

```python
response = client.chat.completions.create(
    model="claude-sonnet-4-20250514",
    messages=[{"role": "user", "content": "解释量子计算"}],
    extra_body={"anthropic_version": "vertex-2023-10-01"}
)
print(response.choices[0].message.content)
```

### 4. 实际输出示例

```
输入：帮我用Python写一个快速排序

输出：
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# 时间复杂度：平均 O(n log n)，最坏 O(n²)
# 空间复杂度：O(n)
# 使用示例：
print(quicksort([3, 6, 8, 10, 1, 2, 1]))  # [1, 1, 2, 3, 6, 8, 10]
```

---

## 💻 Claude Code 配置（ macOS / Linux ）

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

---

## 🖥️ 主流工具接入

| 工具 | 配置方式 |
|------|---------|
| **Cursor IDE** | 设置 → 环境变量：<br>`ANTHROPIC_API_KEY=xxx`<br>`ANTHROPIC_BASE_URL=https://ai.levolink.com/v1` |
| **Dify / FastGPT** | API设置填入 Key + URL：<br>`https://ai.levolink.com/v1` |
| **n8n** | HTTP Request 节点：<br>URL `https://ai.levolink.com/v1/chat/completions`<br>Header `Authorization: Bearer xxx` |
| **LangChain** | `langchain.chat_models.ChatOpenAI`<br>`openai_api_key=xxx`<br>`openai_api_base=https://ai.levolink.com/v1` |
| **NextChat** | 自定义 API：<br>API 地址填 `https://ai.levolink.com/v1`<br>填入 Key 即可 |

---

## 📊 为什么选乐沃联AI？

### 与同类中转站对比

| 维度 | 乐沃联AI | 硅基流动 | 神马中转 | 自建代理 |
|------|---------|---------|---------|---------|
| 模型数量 | **500+** | 较少 | 较少 | 需手动维护 |
| 国内CDN加速 | ✅ | 一般 | ✅ | ❌ |
| 按量计费 | ✅ | ✅ | ✅ | ❌（服务器成本） |
| Claude Code 兼容 | ✅ | ✅ | ✅ | ❌ |
| 新人福利 | ✅ | 有限 | 有限 | ❌ |
| 最低充值 | **1元** | 较高 | 较高 | — |

### 核心优势

- 🇨🇳 **国内CDN加速** — 延迟低至 40-200ms，比直连官方快 3-10 倍
- 🔐 **安全合规** — 全链路 HTTPS 加密，不存储对话内容，仅做请求转发
- 🔄 **OpenAI 兼容** — 替换 base_url 即可，SDK 代码零改动
- 💰 **按量计费** — 用多少充多少，无月费，无订阅压力
- ⚡ **模型同步** — 官方新模型上线后快速跟进，无需等待

---

## ❓ 常见问题

**Q：响应内容和官方一致吗？**  
A：完全一致。乐沃联AI仅做请求转发，底层调用的就是官方模型，响应内容与官方 API 完全相同。

**Q：会被封号吗？**  
A：不会。你使用的是乐沃联AI的 Key，不走官方账号体系，无封号风险。

**Q：支持流式输出（streaming）吗？**  
A：支持，所有模型均支持 `stream: true` 流式响应，实时性好。

**Q：国内访问速度如何？**  
A：采用国内 CDN 节点加速，延迟通常在 40-200ms，远低于直连官方的数百毫秒。

**Q：有免费额度吗？**  
A：新用户注册赠送体验额度，可先试用再决定是否充值。

**Q：如何查看账单？**  
A：登录 [ai.levolink.com](https://ai.levolink.com) 控制台，实时查看各模型用量明细。

---

## 🔧 完整调用示例

### GPT-4o / GPT-4 Turbo

```python
models = ["gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo"]
for model in models:
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": "Hello"}]
    )
    print(f"{model}: {resp.choices[0].message.content[:50]}")
```

### Claude Opus 4.7 / Sonnet 4.6 / Haiku 4.6

```python
models = [
    "claude-opus-4-7-20250514",  # 最强模型，复杂任务
    "claude-sonnet-4-20250514",  # 均衡之选
    "claude-haiku-4-20250514",    # 快速响应
]
for model in models:
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": "Hello"}],
        extra_body={"anthropic_version": "vertex-2023-10-01"}
    )
    print(f"{model}: {resp.choices[0].message.content[:50]}")
```

### DeepSeek-R1 / V4

```python
resp = client.chat.completions.create(
    model="deepseek-reasoner",  # R1 推理模型
    messages=[{"role": "user", "content": "用Python实现一个web服务器"}]
)
```

### Gemini 2.0 Flash

```python
resp = client.chat.completions.create(
    model="gemini-2.0-flash",
    messages=[{"role": "user", "content": "什么是函数式编程"}]
)
```

---

## 🗺️ Roadmap

- [x] 500+ 模型支持
- [x] OpenAI 兼容格式
- [x] Claude Code 即插即用
- [x] 国内 CDN 加速
- [x] 按量计费
- [ ] Claude 4.5 Max 接口
- [ ] 企业套餐 / API 用量告警
- [ ] SDK 官方对接

---

## 📈 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=jiaqing77cn/levolink-ai-api&type=Date)](https://star-history.com/#jiaqing77cn/levolink-ai-api&Date)

---

<div align="center">

**如果对你有帮助，请点个 ⭐ 并推荐给需要的朋友！**

📦 官网：[ai.levolink.com](https://ai.levolink.com)  
📂 仓库：[github.com/jiaqing77cn/levolink-ai-api](https://github.com/jiaqing77cn/levolink-ai-api)  
📖 文档：[levolink.apifox.cn](https://levolink.apifox.cn/)

</div>