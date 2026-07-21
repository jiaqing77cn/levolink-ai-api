# Cursor IDE 接入教程

> 在 Cursor IDE 中使用 Levolink AI 调用 GPT-5.6 / Claude 4.8 / Gemini 3.5。

## 配置步骤

### 1. 打开 Cursor 设置

`Cmd/Ctrl + ,` -> 搜索 "OpenAI" -> 找到 "OpenAI API Key"

### 2. 填入配置

- **API Key**: 你的 Levolink API Key
- **Base URL**: `https://ai.levolink.com/v1`

### 3. 修改 ~/.cursor/settings.json

```json
{
  "openai.apiKey": "你的 Levolink API Key",
  "openai.baseUrl": "https://ai.levolink.com/v1",
  "openai.model": "gpt-5.6-sol"
}
```

### 4. 使用 Claude 模型

在 Cursor 的模型选择中输入自定义模型名：
- `claude-sonnet-4-6` - 日常编程
- `claude-opus-4-8` - 复杂任务
- `gpt-5.6-sol` - GPT 编程

## 推荐配置

| 用途 | 模型 | 分组 |
|------|------|------|
| 代码补全 | gpt-5.6-luna | Codex 专属 (0.8x) |
| 对话 | claude-sonnet-4-6 | 默认 (1.0x) |
| 复杂重构 | claude-opus-4-8 | CC 专属 (2.4x) |
