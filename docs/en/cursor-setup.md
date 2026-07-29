# Cursor IDE Setup Guide

> Use Levolink AI in Cursor IDE to access GPT-5.6 / Claude 4.8 / Gemini 3.5.

## Configuration Steps

### 1. Open Cursor Settings

`Cmd/Ctrl + ,` -> Search for "OpenAI" -> Find "OpenAI API Key"

### 2. Fill in Configuration

- **API Key**: Your Levolink API Key
- **Base URL**: `https://ai.levolink.com/v1`

### 3. Modify ~/.cursor/settings.json

```json
{
  "openai.apiKey": "your Levolink API Key",
  "openai.baseUrl": "https://ai.levolink.com/v1",
  "openai.model": "gpt-5.6-sol"
}
```

### 4. Using Claude Models

Enter a custom model name in Cursor's model selector:
- `claude-sonnet-4-6` - Daily coding
- `claude-opus-4-8` - Complex tasks
- `gpt-5.6-sol` - GPT coding

## Recommended Configuration

| Use Case | Model | Group |
|----------|-------|-------|
| Code completion | gpt-5.6-luna | Codex Dedicated (0.8x) |
| Chat | claude-sonnet-4-6 | Default (1.0x) |
| Complex refactoring | claude-opus-4-8 | CC Dedicated (2.4x) |
