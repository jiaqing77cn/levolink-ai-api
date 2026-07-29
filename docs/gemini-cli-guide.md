# Gemini CLI 接入教程

> 在 Gemini CLI 中使用 Levolink AI 调用 Gemini 3.5 Pro / Flash 等模型，无需翻墙。

## 什么是 Gemini CLI

Gemini CLI 是 Google 推出的终端 AI 助手，支持代码生成、文档分析、任务自动化等。通过 Levolink AI 中转，国内用户可以直接使用 Gemini 系列模型。

## 配置步骤

### 1. 安装 Gemini CLI

```bash
npm install -g @google/gemini-cli
```

### 2. 配置环境变量

```bash
# 添加到 ~/.bash_profile 或 ~/.zshrc
export GEMINI_API_KEY="你的 Levolink API Key"
export GEMINI_API_BASE="https://ai.levolink.com/v1"

# 生效
source ~/.bash_profile
```

### 3. 开始使用

```bash
cd your-project
gemini
```

## 推荐模型与分组

| 用途 | 模型 | 分组 | 倍率 |
|------|------|------|------|
| 日常使用 | `gemini-2.5-flash` | gemini-cli | 1.0x |
| 轻量任务 | `gemini-2.5-flash-lite` | gemini-cli | 1.0x |
| 复杂任务 | `gemini-2.5-pro` | gemini-cli | 1.0x |
| 图片生成 | `gemini-3-pro-image` | 优质gemini | 2.4x |

## 指定模型

```bash
# 使用特定模型
gemini --model gemini-2.5-pro

# 或在交互模式中切换
> /model gemini-2.5-flash
```

## Windows 配置

```powershell
$env:GEMINI_API_KEY="你的 Levolink API Key"
$env:GEMINI_API_BASE="https://ai.levolink.com/v1"
gemini
```

永久设置：

```powershell
[System.Environment]::SetEnvironmentVariable("GEMINI_API_KEY", "你的Key", "User")
[System.Environment]::SetEnvironmentVariable("GEMINI_API_BASE", "https://ai.levolink.com/v1", "User")
```

## 常见问题

### Q: Gemini CLI 报错 "Invalid API key"

检查环境变量是否正确设置：

```bash
echo $GEMINI_API_KEY
echo $GEMINI_API_BASE
# 确保Base URL末尾有 /v1
```

### Q: 响应速度慢

Gemini-CLI 分组（1.0x 倍率）针对 Gemini 模型做了优化，速度较快。

### Q: 支持 Gemini 3.5 Pro 吗

支持。使用 `--model gemini-3-pro-image` 或在交互模式中切换。

## 相关链接

- [Levolink AI 官网](https://ai.levolink.com)
- [Gemini CLI 官方文档](https://github.com/google-gemini/gemini-cli)
- [API 文档](https://levolink.apifox.cn/)
- [模型选择指南](./model-selection-guide.md)
