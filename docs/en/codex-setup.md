# OpenAI Codex Setup Guide

> The best solution for using OpenAI Codex CLI in China — no VPN required, proxied through Levolink AI.

## What is Codex CLI

OpenAI Codex CLI is a terminal-based AI programming assistant from OpenAI. It supports code generation, refactoring, bug fixing, test writing, and more. Similar to Claude Code, but built on GPT models.

## Configuration Steps

### 1. Install Codex CLI

```bash
npm install -g @openai/codex
```

### 2. Configure Environment Variables

```bash
# Add to ~/.bash_profile or ~/.zshrc
export OPENAI_API_KEY="your Levolink API Key"
export OPENAI_API_BASE="https://ai.levolink.com/v1"

# Apply changes
source ~/.bash_profile
```

### 3. Start Using

```bash
cd your-project
codex
```

## Recommended Groups & Models

| Use Case | Model | Group | Multiplier | Input Price |
|----------|-------|-------|-----------|-------------|
| Daily coding | `gpt-5.6-luna` | Codex Dedicated | 0.8x | $0.64/M |
| Complex coding | `gpt-5.6-sol` | Codex Dedicated | 0.8x | $3.20/M |
| Lightweight tasks | `gpt-5.4-mini` | Limited-time Sale | 0.6x | $0.27/M |
| Code completion | `gpt-5-codex` | Codex Dedicated | 0.8x | $0.80/M |

## Windows Configuration

### PowerShell

```powershell
$env:OPENAI_API_KEY="your Levolink API Key"
$env:OPENAI_API_BASE="https://ai.levolink.com/v1"
codex
```

### Permanent Setup

```powershell
[System.Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "your Key", "User")
[System.Environment]::SetEnvironmentVariable("OPENAI_API_BASE", "https://ai.levolink.com/v1", "User")
```

## FAQ

### Q: Codex reports "Invalid API key"

Check that your environment variables are correct:
```bash
echo $OPENAI_API_KEY
echo $OPENAI_API_BASE
# Make sure the Base URL ends with /v1
```

### Q: Slow response times

Switch to the Codex Dedicated group (0.8x), which is optimized for GPT coding models.

### Q: Does it support GPT-5.6 Sol?

Yes. Specify the model in Codex with `--model gpt-5.6-sol`.

### Q: What's the difference from Claude Code?

| Dimension | Codex CLI | Claude Code |
|-----------|-----------|-------------|
| Models | GPT series | Claude series |
| Coding style | Direct and efficient | Deep reasoning |
| Context | 128K | 200K |
| Best for | Quick prototyping, scripts | Complex refactoring, architecture design |

Both can be used through Levolink AI — one API Key lets you switch between them.

## Related Links

- [Levolink AI Website](https://ai.levolink.com)
- [Codex CLI Official Docs](https://github.com/openai/codex)
- [API Documentation](https://levolink.apifox.cn/)
- [Model Selection Guide](./model-selection-guide.md)
