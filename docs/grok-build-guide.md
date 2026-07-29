# Grok Build 接入教程

> 在 Grok Build 中使用 Levolink AI 中转调用 GPT/Claude/Gemini 等模型。

## 什么是 Grok Build

Grok Build 是 xAI 推出的终端 AI 编程助手，支持交互式 TUI、无头模式和 ACP 协议。通过自定义模型配置，可以让 Grok Build 调用 Levolink AI 上的任意模型。

## 配置步骤

### 1. 安装 Grok Build

**macOS / Linux：**

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
```

**Windows (PowerShell)：**

```powershell
irm https://x.ai/cli/install.ps1 | iex
```

### 2. 配置自定义模型

编辑 `~/.grok/config.toml`（Windows: `%USERPROFILE%\.grok\config.toml`）：

```toml
# 使用 Levolink AI 作为后端
[model.levolink-gpt]
model = "gpt-5.6-sol"
base_url = "https://ai.levolink.com/v1"
name = "GPT-5.6 Sol (Levolink)"
env_key = "LEVOLINK_API_KEY"

[model.levolink-claude]
model = "claude-sonnet-4-6"
base_url = "https://ai.levolink.com/v1"
name = "Claude Sonnet 4.6 (Levolink)"
env_key = "LEVOLINK_API_KEY"

[model.levolink-gemini]
model = "gemini-2.5-pro"
base_url = "https://ai.levolink.com/v1"
name = "Gemini 2.5 Pro (Levolink)"
env_key = "LEVOLINK_API_KEY"

[models]
default = "levolink-gpt"
```

### 3. 设置 API Key

```bash
export LEVOLINK_API_KEY="你的 Levolink API Key"
```

### 4. 开始使用

```bash
cd your-project
grok
```

在 TUI 中使用 `/model` 切换模型：

```
/model levolink-claude
```

## 推荐模型配置

| 用途 | 模型 | 分组建议 |
|------|------|---------|
| 日常编程 | `gpt-5.6-luna` | Codex 专属 (0.8x) |
| 复杂编程 | `gpt-5.6-sol` | Codex 专属 (0.8x) |
| 深度推理 | `claude-opus-4-8` | 默认 (1.0x) |
| 长文本 | `gemini-2.5-pro` | gemini-cli (1.0x) |

## 无头模式

```bash
# 使用 Levolink 模型执行任务
grok -p "Explain this codebase" -m levolink-claude

# 输出 JSON
grok -p "Analyze architecture" -m levolink-gpt --output-format streaming-json
```

## 常见问题

### Q: Grok Build 启动时提示 "model not found"

运行 `grok inspect` 检查配置是否正确加载：

```bash
grok inspect
```

### Q: 如何同时使用 Grok 模型和 Levolink 模型？

在 `config.toml` 中添加 xAI 官方模型和 Levolink 模型，通过 `/model` 命令切换。

### Q: 支持流式输出吗

支持。Levolink AI 所有模型均支持流式输出。

## 相关链接

- [Levolink AI 官网](https://ai.levolink.com)
- [Grok Build 官方文档](https://docs.x.ai/build/overview)
- [Grok Build GitHub](https://github.com/xai-org/grok-build)
- [API 文档](https://levolink.apifox.cn/)
