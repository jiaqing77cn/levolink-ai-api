# OpenCode Setup Guide

> Use Levolink AI with OpenCode to access 500+ AI models without a VPN.

## What is OpenCode

OpenCode is an open-source AI coding assistant (160K+ Stars), available as a terminal app, desktop app, and IDE plugin. By configuring an OpenAI-compatible API endpoint, you can connect it to Levolink AI.

## Configuration Steps

### 1. Install OpenCode

```bash
# Recommended installation method
curl -fsSL https://opencode.ai/install | bash

> ⚠️ Consider reviewing the script before installation

# Or via npm
npm install -g opencode-ai
```

### 2. Configure Levolink AI as Provider

Create `opencode.json` in your project root:

```json
{
  "provider": {
    "levolink": {
      "name": "Levolink AI",
      "api_key": "your Levolink API Key",
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

### 3. Or Configure via TUI

```bash
cd your-project
opencode
```

Run the following in the OpenCode TUI:

```
/connect
```

Select "Custom OpenAI Compatible" and fill in:
- **API Key**: your Levolink API Key
- **Base URL**: `https://ai.levolink.com/v1`

### 4. Initialize Project

```
/init
```

OpenCode will analyze the project structure and generate an `AGENTS.md` file.

## Recommended Models

| Use Case | Model | Group Suggestion |
|----------|-------|-----------------|
| Daily coding | `gpt-5.6-luna` | Codex Exclusive (0.8x) |
| Complex coding | `claude-sonnet-4-6` | Default (1.0x) |
| Deep reasoning | `claude-opus-4-8` | Default (1.0x) |
| Long context | `gemini-2.5-pro` | gemini-cli (1.0x) |
| Best value | `deepseek-reasoner` | Limited-time discount (0.6x) |

## Usage Examples

```
# Plan mode (press Tab to switch)
> Refactor the authentication logic in src/api/index.ts

# Build mode
> Execute the changes according to the plan

# Undo changes
/undo
```

## FAQ

### Q: OpenCode reports "provider not found"

Check that `opencode.json` is in the project root directory and the JSON format is correct.

### Q: How do I switch models?

Type `/model levolink/claude-sonnet-4-6` in the TUI to switch models.

### Q: Does it support Plan mode?

Yes. Press `Tab` to switch between Build and Plan modes.

### Q: How do I configure multiple providers?

Add multiple providers in `opencode.json` and switch using `/model provider/model`.

## Related Links

- [Levolink AI Official Site](https://ai.levolink.com)
- [OpenCode Official Documentation](https://opencode.ai/docs/)
- [API Documentation](https://levolink.apifox.cn/)
- [Model Selection Guide](./model-selection-guide.md)
