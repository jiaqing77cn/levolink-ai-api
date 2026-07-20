# 🚀 国内 AI API 中转站完全指南

> 帮国内开发者无需翻墙、稳定低延迟地调用 Claude / GPT / Gemini / DeepSeek 等 500+ 全球顶尖 AI 模型。
> 
> 最后更新：2026-07-20 23:05 (UTC+8) | [🌐 官网](https://ai.levolink.com) | [📋 实时价格](#-实时模型价格) | [📖 API 文档](https://levolink.apifox.cn/)

[English](./README_EN.md) | 中文

---

## 📋 目录

- [🔍 中转站选购指南](#-中转站选购指南)
- [💰 实时模型价格](#-实时模型价格)
- [🛠️ 接入教程](#-接入教程)
- [📊 竞品对比](#-竞品对比)
- [❓ FAQ](#-faq)
- [🤝 贡献](#-贡献)

---

## 🔍 中转站选购指南

选择 AI API 中转站，看这 6 个维度：

| 维度 | 说明 | 警惕信号 |
|------|------|---------|
| **稳定性** | 是否经常宕机、延迟高 | 频繁断线、无公告 |
| **速度** | 响应延迟是否可接受 | >5s 首 token 延迟 |
| **模型覆盖** | 是否支持最新模型 | 上新慢、缺热门模型 |
| **价格透明** | 计费是否清晰、可查账单 | 无调用记录、不透明 |
| **掺水风险** | 是否用低价模型冒充高价模型 | 价格异常低、效果差 |
| **跑路风险** | 是否公司运营、有售后 | 个人运营、无客服 |

### ⚠️ 避坑清单

1. **缓存价格陷阱**：正常缓存价格应为 10%，部分站收 15%-30%
2. **掺水检测**：用相同 prompt 对比官方和中转站输出，质量差异大 = 掺水
3. **Token 计数造假**：发送已知 token 数请求，检查计费是否虚高
4. **低价陷阱**：价格远低于市场价，大概率用 GLM 冒充 GPT
5. **充值跑路**：不要大额充值！用多少充多少

### 🔬 如何检测中转站是否掺水

```python
# 方法1：能力测试 - 用需要推理的 prompt
prompt = "A farmer has 17 sheep. All but 9 die. How many are left?"
# GPT/Claude 正确答案: 9
# 低端模型经常答错: 8

# 方法2：长上下文测试
# 发送 50K+ token 的长文本，问结尾的细节
# 低端模型会丢失上下文

# 方法3：代码能力测试
prompt = "用 Python 实现一个 LRU 缓存，带 TTL 过期"
# 对比官方和中转站的代码质量
```

---

## 💰 实时模型价格

> 以下价格由 GitHub Actions 自动从 [Levolink API](https://ai.levolink.com/api/pricing) 拉取，每小时更新。
> 
> 价格单位：USD / 百万 Token | 出入倍率 = 输出价格 / 输入价格

### OpenAI GPT 系列

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

### Anthropic Claude 系列

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

### Google Gemini 系列

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

### DeepSeek 系列

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

### 国产模型（通义/豆包/智谱/Kimi/MiniMax）

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

> 💡 完整价格请前往 [Levolink AI 定价页面](https://ai.levolink.com/pricing) 查看，支持 33 个分组、228 个模型、500+ 价格组合。

### 分组说明

| 分组类型 | 倍率范围 | 适合场景 |
|---------|---------|---------|
| 限时特价 | 0.6x | 测试、低成本场景 |
| Codex 专属 | 0.8x | GPT 编程、日常使用 |
| default | 1.0x | 标准质量、平衡选择 |
| anti/kiro | 1.2x | 性价比 Claude |
| Claude Code 专属 | 2.4x | Claude Code 编程 |
| Azure 渠道 | 3.0x | 稳定 GPT |
| AWS 企业级 | 4.0x | 企业级 Claude |
| Vertex/官方直连 | 6.0x | 最高质量 |
| 正价官转 | 16.0x | 完全官方品质 |

---

## 🛠️ 接入教程

### 快速开始

1. 前往 [Levolink AI](https://ai.levolink.com) → 注册 → 控制台创建 Key
2. 充值（最低 1 元起充）
3. 选择代码示例接入：

### Python (OpenAI SDK)

```python
from openai import OpenAI

client = OpenAI(
    api_key="你的API Key",
    base_url="https://ai.levolink.com/v1"
)

# GPT-5.6 Sol
resp = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": "用Python写一个快速排序"}]
)

# Claude Sonnet 4.6
resp = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": "解释量子计算"}],
    extra_body={"anthropic_version": "vertex-2023-10-01"}
)

# DeepSeek R1
resp = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[{"role": "user", "content": "用Python实现一个web服务器"}]
)
```

### Node.js / curl

```bash
curl https://ai.levolink.com/v1/chat/completions \
  -H "Authorization: Bearer 你的API Key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.6-sol",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

完整示例见 [examples/](./examples/) 目录。

### Claude Code

```bash
npm install -g @anthropic-ai/claude-code

echo 'export ANTHROPIC_AUTH_TOKEN="你的API Key"' >> ~/.bash_profile
echo 'export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"' >> ~/.bash_profile
source ~/.bash_profile

cd your-project && claude
```

### OpenAI Codex

```bash
npm install -g @openai/codex

export OPENAI_API_KEY="你的API Key"
export OPENAI_API_BASE="https://ai.levolink.com/v1"
```

### Gemini CLI

```bash
npm install -g @google/gemini-cli

export GEMINI_API_KEY="你的API Key"
export GEMINI_API_BASE="https://ai.levolink.com/v1"
```

### 工具集成

| 工具 | 配置方式 |
|------|---------|
| Dify / FastGPT | API 设置填入 Key + Base URL: `https://ai.levolink.com/v1` |
| n8n | HTTP Request → URL: `https://ai.levolink.com/v1/chat/completions` |
| LangChain | `ChatOpenAI(openai_api_key="Key", openai_api_base="https://ai.levolink.com/v1")` |
| NextChat | 设置 → 自定义 API → URL: `https://ai.levolink.com/v1` |
| OpenClaw | `openai_api_key: Key` + `openai_api_base: https://ai.levolink.com/v1` |

### 使用场景

- **AI 编程** - Claude Code / Codex 配置后，直接用 Claude 4.8 / GPT-5.6 做代码重构、Bug 修复
- **长文本处理** - 10 万字文档分析、合同审核、论文总结
- **自动化 Agent** - 一个 Key 调度所有模型，支持多 Agent 并行
- **RAG 知识库** - DeepSeek / GPT 对接向量数据库，企业知识库问答
- **自动化工作流** - n8n / FastGPT / Dify 接入，全流程自动化

---

## 📊 竞品对比

| 维度 | Levolink AI | 硅基流动 | 神马中转 | 自建代理 |
|------|------------|---------|---------|---------|
| 模型数量 | 500+ | 较少 | 较少 | 需手动维护 |
| 分组选择 | 33 个分组 | 无 | 少 | - |
| 国内 CDN 加速 | ✅ | 一般 | ✅ | ❌ |
| 最低充值 | 1 元 | 较高 | 较高 | - |
| 按量计费 | ✅ | ✅ | ✅ | ❌ |
| Claude Code 兼容 | ✅ | ✅ | ✅ | ❌ |
| OpenAI 格式 | ✅ | ✅ | ✅ | 需适配 |
| 价格透明 | ✅ 33分组可选 | 单一价格 | 单一价格 | - |
| 支持发票 | ✅ | - | - | - |

---

## ❓ FAQ

**响应内容和官方一致吗？**

完全一致。Levolink AI 仅做请求转发，底层调用官方模型，响应内容与官方 API 完全相同。

**会被封号吗？**

不会。你使用的是 Levolink AI 的 Key，不走官方账号体系，无封号风险。

**不同分组有什么区别？**

不同分组对应不同的后端渠道（Azure/AWS/Vertex/官方直连等），质量和价格不同。低价分组性价比高，高价分组质量最稳定。建议先用 default 分组测试，再根据需求调整。

**支持 streaming 吗？**

支持，所有模型均支持流式输出，延迟低，实时性好。

**国内访问速度如何？**

采用国内 CDN 节点加速，延迟通常在 40-200ms，远低于直连官方的数百毫秒。

**有免费额度吗？**

新用户注册赠送体验额度，可先试用再决定是否充值。

**可以开发票吗？**

可以。个人设置 → 实名认证 → 钱包 → 选择开票，电子发票 5 个工作日内开出。

**如何选择分组？**

- 省钱：限时特价(0.6x) / Codex专属(0.8x)
- 平衡：default(1.0x)
- 高质量：Claude Code专属(2.4x) / Azure(3.0x)
- 最高质量：Vertex(6.0x) / 正价官转(16.0x)

---

## 🤝 贡献

- 🐛 发现 Bug → 提交 [Issue](https://github.com/jiaqing77cn/levolink-ai-api/issues)
- 📝 优化文档 → 直接提交 PR
- 💡 新功能建议 → 发起 [Discussion](https://github.com/jiaqing77cn/levolink-ai-api/discussions)
- 📄 贡献指南 → 见 [CONTRIBUTING.md](./CONTRIBUTING.md)

---

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=jiaqing77cn/levolink-ai-api&type=Date)](https://star-history.com/#jiaqing77cn/levolink-ai-api&Date)

---

## License

MIT License · Copyright (c) 2026 [Levolink AI](https://ai.levolink.com)
