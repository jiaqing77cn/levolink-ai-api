# CC Switch 接入教程

> 使用 CC Switch 统一管理 Claude Code、Codex、Gemini CLI、OpenCode、OpenClaw 等工具的 Levolink AI 配置。

## 什么是 CC Switch

CC Switch 是跨平台桌面工具，用于统一管理多个 AI 编程工具的 API 配置。支持 Claude Code、Claude Desktop、Codex、Gemini CLI、Grok Build、OpenCode、OpenClaw 和 Hermes，一键切换 API Provider，无需手动编辑配置文件。

## 安装

### macOS

```bash
# Homebrew
brew install --cask cc-switch
```

### Windows

从 [ccswitch.io](https://ccswitch.io) 下载安装包。

### Linux

从 [GitHub Releases](https://github.com/farion1231/cc-switch/releases) 下载 AppImage。

## 配置 Levolink AI

### 1. 添加 Provider

打开 CC Switch -> 点击「添加 Provider」-> 选择「自定义」：

| 配置项 | 值 |
|--------|-----|
| 名称 | Levolink AI |
| API Key | 你的 Levolink API Key |
| Base URL | `https://ai.levolink.com/v1` |
| 格式 | OpenAI Compatible |

### 2. 配置各工具

CC Switch 会自动为每个工具生成配置：

**Claude Code：**
```bash
export ANTHROPIC_AUTH_TOKEN="你的Key"
export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"
```

**Codex：**
```bash
export OPENAI_API_KEY="你的Key"
export OPENAI_API_BASE="https://ai.levolink.com/v1"
```

**Gemini CLI：**
```bash
export GEMINI_API_KEY="你的Key"
export GEMINI_API_BASE="https://ai.levolink.com/v1"
```

**OpenCode：**
```json
{
  "provider": {
    "levolink": {
      "api_key": "你的Key",
      "base_url": "https://ai.levolink.com/v1"
    }
  }
}
```

### 3. 一键切换

在 CC Switch 界面中选择目标工具 -> 选择「Levolink AI」-> 点击「应用」。CC Switch 会自动修改对应工具的配置文件。

## 推荐配置

| 工具 | 推荐模型 | 分组 |
|------|---------|------|
| Claude Code | `claude-sonnet-4-6` | 默认 (1.0x) |
| Codex | `gpt-5.6-sol` | Codex 专属 (0.8x) |
| Gemini CLI | `gemini-2.5-pro` | gemini-cli (1.0x) |
| OpenCode | `gpt-5.6-luna` | Codex 专属 (0.8x) |
| OpenClaw | `claude-opus-4-8` | 默认 (1.0x) |

## 多 Provider 管理

CC Switch 支持同时配置多个 Provider，方便对比测试：

1. 添加「Levolink AI - 限时特价」(0.6x)
2. 添加「Levolink AI - 默认」(1.0x)
3. 添加「Levolink AI - CC 专属」(2.4x)

在界面中一键切换，无需修改代码或环境变量。

## 常见问题

### Q: CC Switch 修改配置后工具没生效

确保目标工具已完全退出并重新启动。Claude Code 需要重新 source 环境变量。

### Q: 支持同时为不同工具配置不同 Provider 吗

支持。CC Switch 可以为每个工具独立配置 Provider 和模型。

### Q: CC Switch 是免费的吗

CC Switch 是开源工具，免费使用。

## 相关链接

- [Levolink AI 官网](https://ai.levolink.com)
- [CC Switch 官网](https://ccswitch.io)
- [CC Switch GitHub](https://github.com/farion1231/cc-switch)
- [API 文档](https://levolink.apifox.cn/)
