# Dify 接入教程

> 将 Dify 对接 Levolink AI，一个 Key 调用 500+ AI 模型。

## 什么是 Dify

Dify 是开源的 LLM 应用开发平台，支持知识库管理、Agent 编排、工作流自动化。通过对接 Levolink AI，Dify 可以调用 GPT-5.6、Claude 4.8、Gemini、DeepSeek 等全部模型。

## 配置步骤

### 1. 获取 Levolink API Key

前往 [Levolink AI](https://ai.levolink.com) -> 注册 -> 控制台 -> 创建 Key

### 2. 在 Dify 中配置模型供应商

进入 Dify -> 设置 -> 模型供应商 -> 选择 **OpenAI API 兼容**：

| 配置项 | 值 |
|--------|-----|
| API Key | 你的 Levolink API Key |
| API endpoint | `https://ai.levolink.com/v1` |
| 模型名称 | `gpt-5.6-sol` / `claude-sonnet-4-6` / `deepseek-reasoner` 等 |

### 3. 添加多个模型

在 Dify 的「模型」页面，依次添加你需要的模型：

**推荐配置：**

| 用途 | 模型 | 分组建议 |
|------|------|---------|
| 对话助手 | `claude-sonnet-4-6` | 默认 (1.0x) |
| 编程助手 | `gpt-5.6-sol` | Codex 专属 (0.8x) |
| 长文本处理 | `gemini-2.5-pro` | Gemini-CLI 混合 (1.0x) |
| 推理任务 | `deepseek-reasoner` | 限时特价 (0.6x) |
| 日常对话 | `gpt-5.6-luna` | Codex 专属 (0.8x) |

### 4. 在应用中使用

创建应用时，在「模型」下拉框中选择已添加的模型即可。

## RAG 知识库配置

Dify 的知识库功能配合 Levolink AI 使用：

1. **Embedding 模型**：使用 `text-embedding-3-large`（Levolink 支持）
2. ** rerank 模型**：暂不支持，可关闭 rerank
3. **对话模型**：推荐 `claude-sonnet-4-6` 或 `gpt-5.6-sol`

### 知识库成本估算

| 文档量 | Embedding 费用 | 对话费/次 |
|--------|---------------|----------|
| 100 篇 | ~$0.02 | ~$0.01 |
| 1000 篇 | ~$0.20 | ~$0.01 |
| 10000 篇 | ~$2.00 | ~$0.02 |

## Agent 工作流配置

Dify Agent + Levolink AI 的典型工作流：

```
用户输入 -> Claude Sonnet 4.6（意图识别）
         -> DeepSeek R1（推理分析）
         -> GPT-5.6 Sol（生成回复）
```

一个 API Key 即可调度所有模型，无需多个账号。

## Docker 部署的 Dify

如果你用 Docker 部署 Dify，在 `docker-compose.yml` 中设置环境变量：

```yaml
services:
  api:
    environment:
      - OPENAI_API_KEY=你的Levolink Key
      - OPENAI_API_BASE=https://ai.levolink.com/v1
```

## 常见问题

### Q: Dify 报错 "model not found"

确保模型名称完全匹配。Levolink 支持的模型列表见 [README 价格表](../README.md#-实时模型价格)。

### Q: 流式输出不工作

在 Dify 模型设置中开启「流式输出」选项。Levolink 所有模型都支持 streaming。

### Q: 如何控制成本

1. 使用限时特价分组（0.6x 倍率）
2. 长文本用 Gemini 2.5 Flash（$0.30/M 输入）
3. 日常对话用 GPT-5.6 Luna（$0.80/M 输入）
4. 在 Dify 中设置 token 限制

## 相关链接

- [Levolink AI 官网](https://ai.levolink.com)
- [Dify 官方文档](https://docs.dify.ai)
- [API 文档](https://levolink.apifox.cn/)
- [模型选择指南](./model-selection-guide.md)
- [成本计算器](./cost-calculator-guide.md)
