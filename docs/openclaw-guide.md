# OpenClaw 接入教程

> 在 OpenClaw 中使用 Levolink AI 作为后端模型提供商。

## 什么是 OpenClaw

OpenClaw 是开源的 AI Agent 运行时，支持多模型调度、技能系统、定时任务、记忆系统等。通过配置 OpenAI 兼容的 API 端点，可以接入 Levolink AI。

## 配置步骤

### 1. 安装 OpenClaw

```bash
# 使用 npm 安装
npm install -g openclaw

# 或使用 Docker
docker run -d openclaw/openclaw
```

### 2. 配置 Gateway

编辑 OpenClaw 的 Gateway 配置文件（通常在 `~/.openclaw/config.yaml` 或项目目录的 `config.yaml`）：

```yaml
# 模型配置
model:
  # 默认模型
  default: volces/glm-5.2

  # OpenAI 兼容提供商
  providers:
    - name: levolink
      api_key: "你的 Levolink API Key"
      base_url: "https://ai.levolink.com/v1"
      models:
        - gpt-5.6-sol
        - gpt-5.6-luna
        - claude-sonnet-4-6
        - claude-opus-4-8
        - gemini-2.5-pro
        - deepseek-reasoner
```

### 3. 或通过环境变量配置

```bash
# 添加到 ~/.bash_profile 或 ~/.zshrc
export OPENAI_API_KEY="你的 Levolink API Key"
export OPENAI_API_BASE="https://ai.levolink.com/v1"

source ~/.bash_profile
```

### 4. 启动 OpenClaw

```bash
openclaw gateway start

# 检查状态
openclaw status
```

## 推荐模型配置

| 用途 | 模型 | 分组建议 |
|------|------|---------|
| Agent 日常任务 | `gpt-5.6-luna` | Codex 专属 (0.8x) |
| 复杂推理 | `claude-opus-4-8` | 默认 (1.0x) |
| 编程任务 | `claude-sonnet-4-6` | 默认 (1.0x) |
| 长文本处理 | `gemini-2.5-pro` | gemini-cli (1.0x) |
| 性价比选择 | `deepseek-reasoner` | 限时特价 (0.6x) |

## 会话模型切换

OpenClaw 支持为不同会话指定不同模型：

```bash
# 在会话中切换模型
/model claude-opus-4-8

# 查看当前模型
/status
```

## 多模型调度

OpenClaw 支持同时调度多个模型，适合 Agent 并行任务：

```yaml
# 配置多个 provider 同时使用
model:
  providers:
    - name: levolink-gpt
      api_key: "你的Key"
      base_url: "https://ai.levolink.com/v1"
    - name: levolink-claude
      api_key: "你的Key"
      base_url: "https://ai.levolink.com/v1"
```

## 常见问题

### Q: OpenClaw 报错 "model not available"

检查 Gateway 是否已启动，模型名是否正确：

```bash
openclaw status
openclaw models list
```

### Q: 如何设置默认模型

在配置文件中设置 `model.default`，或在会话中使用 `/model` 命令。

### Q: 支持流式输出吗

支持。OpenClaw 默认使用流式输出。

### Q: 如何控制成本

1. 使用限时特价分组（0.6x 倍率）
2. 为不同任务选择合适模型
3. 在配置中设置 token 限制

## 相关链接

- [Levolink AI 官网](https://ai.levolink.com)
- [OpenClaw 官方文档](https://docs.openclaw.ai)
- [OpenClaw GitHub](https://github.com/openclaw/openclaw)
- [API 文档](https://levolink.apifox.cn/)
- [模型选择指南](./model-selection-guide.md)
