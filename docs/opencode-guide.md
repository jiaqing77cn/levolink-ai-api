# OpenCode 接入教程

> 在 OpenCode 中使用 Levolink AI 调用 500+ AI 模型，无需翻墙。

## 什么是 OpenCode

OpenCode 是开源的 AI 编程助手（160K+ Stars），支持终端、桌面和 IDE 插件三种形态。通过配置 OpenAI 兼容的 API 端点，可以接入 Levolink AI。

## 配置步骤

### 1. 安装 OpenCode

```bash
# 推荐安装方式
curl -fsSL https://opencode.ai/install | bash

> ⚠️ 安装前建议先审查脚本内容

# 或通过 npm
npm install -g opencode-ai
```

### 2. 配置 Levolink AI 为 Provider

在项目根目录创建 `opencode.json`：

```json
{
  "provider": {
    "levolink": {
      "name": "Levolink AI",
      "api_key": "你的 Levolink API Key",
      "base_url": "https://ai.levolink.com/v1",
      "models": {
        "gpt-5.6-sol": { "name": "GPT-5.6 Sol" },
        "claude-sonnet-4-6": { "name": "Claude Sonnet 4.6" },
        "gemini-2.5-pro": { "name": "Gemini 2.5 Pro" },
        "deepseek-reasoner": { "name": "DeepSeek R1" }
      }
    }
  },
  "model": "levolink/gpt-5.6-sol"
}
```

### 3. 或通过 TUI 配置

```bash
cd your-project
opencode
```

在 OpenCode TUI 中运行：

```
/connect
```

选择 "Custom OpenAI Compatible"，填入：
- **API Key**: 你的 Levolink API Key
- **Base URL**: `https://ai.levolink.com/v1`

### 4. 初始化项目

```
/init
```

OpenCode 会分析项目结构并生成 `AGENTS.md` 文件。

## 推荐模型

| 用途 | 模型 | 分组建议 |
|------|------|---------|
| 日常编程 | `gpt-5.6-luna` | Codex 专属 (0.8x) |
| 复杂编程 | `claude-sonnet-4-6` | 默认 (1.0x) |
| 深度推理 | `claude-opus-4-8` | 默认 (1.0x) |
| 长文本 | `gemini-2.5-pro` | gemini-cli (1.0x) |
| 性价比 | `deepseek-reasoner` | 限时特价 (0.6x) |

## 使用示例

```
# Plan 模式（按 Tab 切换）
> 重构 src/api/index.ts 中的认证逻辑

# Build 模式
> 按照计划执行修改

# 撤销修改
/undo
```

## 常见问题

### Q: OpenCode 报错 "provider not found"

检查 `opencode.json` 是否在项目根目录，JSON 格式是否正确。

### Q: 如何切换模型

在 TUI 中输入 `/model levolink/claude-sonnet-4-6` 切换模型。

### Q: 支持 Plan 模式吗

支持。按 `Tab` 键在 Build 和 Plan 模式之间切换。

### Q: 如何配置多个 Provider

在 `opencode.json` 中添加多个 provider，通过 `/model provider/model` 切换。

## 相关链接

- [Levolink AI 官网](https://ai.levolink.com)
- [OpenCode 官方文档](https://opencode.ai/docs/)
- [API 文档](https://levolink.apifox.cn/)
- [模型选择指南](./model-selection-guide.md)
