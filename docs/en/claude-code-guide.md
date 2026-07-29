# Claude Code Setup Guide

> The best solution for using Claude Code in China — no VPN required, low latency.

## What is Claude Code

Claude Code is an official AI programming assistant from Anthropic. It runs directly in the terminal and supports code generation, refactoring, bug fixing, test writing, and more.

## Configuration Steps

### 1. Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

### 2. Configure Environment Variables

```bash
# Add to ~/.bash_profile or ~/.zshrc
export ANTHROPIC_AUTH_TOKEN="your Levolink API Key"
export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"

# Apply changes
source ~/.bash_profile
```

### 3. Start Using

```bash
cd your-project
claude
```

## Recommended Groups

| Group | Multiplier | Best For |
|-------|-----------|----------|
| Default (Azure+MJ) | 1.0x | Daily use, great value |
| CC Dedicated | 2.4x | Optimized for Claude Code, best stability |
| anti/kiro | 1.2x | Best value option |

## FAQ

### Q: Claude Code reports "authentication failed"

Check that your environment variables are set correctly:
```bash
echo $ANTHROPIC_AUTH_TOKEN
echo $ANTHROPIC_BASE_URL
```

### Q: Slow response times

Try switching groups. The CC Dedicated group is optimized for Claude Code and offers faster speeds.

### Q: Does it support Claude Opus 4.8?

Yes. Type `/model` in Claude Code to switch models.

## Related Links

- [Levolink AI Website](https://ai.levolink.com)
- [Claude Code Official Docs](https://docs.anthropic.com/en/docs/claude-code)
- [API Documentation](https://levolink.apifox.cn/)
