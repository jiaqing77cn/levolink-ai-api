# Grok Build Setup Guide

> Use Levolink AI with Grok Build to access GPT/Claude/Gemini and other models.

## What is Grok Build

Grok Build is xAI's terminal AI coding assistant, supporting interactive TUI, headless mode, and the ACP protocol. With custom model configuration, Grok Build can call any model available on Levolink AI.

## Configuration Steps

### 1. Install Grok Build

**macOS / Linux:**

```bash
curl -fsSL https://x.ai/cli/install.sh | bash

> ⚠️ Consider reviewing the script before installation: curl -fsSL https://x.ai/cli/install.sh | less
```

**Windows (PowerShell):**

```powershell
irm https://x.ai/cli/install.ps1 | iex
```

### 2. Configure Custom Models

Edit `~/.grok/config.toml` (Windows: `%USERPROFILE%\.grok\config.toml`):

```toml
# Use Levolink AI as the backend
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

### 3. Set API Key

```bash
export LEVOLINK_API_KEY="your Levolink API Key"
```

### 4. Start Using

```bash
cd your-project
grok
```

Use `/model` in the TUI to switch models:

```
/model levolink-claude
```

## Recommended Model Configuration

| Use Case | Model | Group Suggestion |
|----------|-------|-----------------|
| Daily coding | `gpt-5.6-luna` | Codex Exclusive (0.8x) |
| Complex coding | `gpt-5.6-sol` | Codex Exclusive (0.8x) |
| Deep reasoning | `claude-opus-4-8` | Default (1.0x) |
| Long context | `gemini-2.5-pro` | gemini-cli (1.0x) |

## Headless Mode

```bash
# Execute a task using a Levolink model
grok -p "Explain this codebase" -m levolink-claude

# Output JSON
grok -p "Analyze architecture" -m levolink-gpt --output-format streaming-json
```

## FAQ

### Q: Grok Build shows "model not found" on startup

Run `grok inspect` to check if the configuration is loaded correctly:

```bash
grok inspect
```

### Q: Can I use both Grok models and Levolink models at the same time?

Add both xAI official models and Levolink models in `config.toml`, then switch between them using the `/model` command.

### Q: Does it support streaming output?

Yes. All models on Levolink AI support streaming output.

## Related Links

- [Levolink AI Official Site](https://ai.levolink.com)
- [Grok Build Official Documentation](https://docs.x.ai/build/overview)
- [Grok Build GitHub](https://github.com/xai-org/grok-build)
- [API Documentation](https://levolink.apifox.cn/)
