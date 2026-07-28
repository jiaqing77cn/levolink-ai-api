# OpenAI Codex 接入教程

> 国内使用 OpenAI Codex CLI 的最佳方案，无需翻墙，通过 Levolink AI 中转。

## 什么是 Codex CLI

OpenAI Codex CLI 是 OpenAI 推出的终端 AI 编程助手，支持代码生成、重构、Bug 修复、测试编写等。类似 Claude Code，但基于 GPT 模型。

## 配置步骤

### 1. 安装 Codex CLI

```bash
npm install -g @openai/codex
```

### 2. 配置环境变量

```bash
# 添加到 ~/.bash_profile 或 ~/.zshrc
export OPENAI_API_KEY="你的 Levolink API Key"
export OPENAI_API_BASE="https://ai.levolink.com/v1"

# 生效
source ~/.bash_profile
```

### 3. 开始使用

```bash
cd your-project
codex
```

## 推荐分组与模型

| 用途 | 模型 | 分组 | 倍率 | 输入价 |
|------|------|------|------|--------|
| 日常编程 | `gpt-5.6-luna` | Codex 专属 | 0.8x | $0.64/M |
| 复杂编程 | `gpt-5.6-sol` | Codex 专属 | 0.8x | $3.20/M |
| 轻量任务 | `gpt-5.4-mini` | 限时特价 | 0.6x | $0.27/M |
| 代码补全 | `gpt-5-codex` | Codex 专属 | 0.8x | $0.80/M |

## Windows 配置

### PowerShell

```powershell
$env:OPENAI_API_KEY="你的 Levolink API Key"
$env:OPENAI_API_BASE="https://ai.levolink.com/v1"
codex
```

### 永久设置

```powershell
[System.Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "你的Key", "User")
[System.Environment]::SetEnvironmentVariable("OPENAI_API_BASE", "https://ai.levolink.com/v1", "User")
```

## 常见问题

### Q: Codex 报错 "Invalid API key"

检查环境变量是否正确：
```bash
echo $OPENAI_API_KEY
echo $OPENAI_API_BASE
# 确保Base URL末尾有 /v1
```

### Q: 响应速度慢

切换到 Codex 专属分组（0.8x），该分组针对 GPT 编程模型做了优化。

### Q: 支持 GPT-5.6 Sol 吗

支持。在 Codex 中通过 `--model gpt-5.6-sol` 指定模型。

### Q: 和 Claude Code 有什么区别

| 维度 | Codex CLI | Claude Code |
|------|-----------|-------------|
| 模型 | GPT 系列 | Claude 系列 |
| 编程风格 | 直接高效 | 深度推理 |
| 上下文 | 128K | 200K |
| 适合场景 | 快速原型、脚本 | 复杂重构、架构设计 |

两者都通过 Levolink AI 中转使用，一个 Key 即可切换。

## 相关链接

- [Levolink AI 官网](https://ai.levolink.com)
- [Codex CLI 官方文档](https://github.com/openai/codex)
- [API 文档](https://levolink.apifox.cn/)
- [模型选择指南](./model-selection-guide.md)
