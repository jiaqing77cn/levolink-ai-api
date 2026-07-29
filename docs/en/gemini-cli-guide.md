# Gemini CLI Setup Guide

> Use Levolink AI with Gemini CLI to access Gemini 3.5 Pro / Flash and other models without a VPN.

## What is Gemini CLI

Gemini CLI is Google's terminal AI assistant, supporting code generation, document analysis, task automation, and more. Through Levolink AI proxy, users in China can directly use Gemini series models.

## Configuration Steps

### 1. Install Gemini CLI

```bash
npm install -g @google/gemini-cli
```

### 2. Configure Environment Variables

```bash
# Add to ~/.bash_profile or ~/.zshrc
export GEMINI_API_KEY="your Levolink API Key"
export GEMINI_API_BASE="https://ai.levolink.com/v1"

# Apply changes
source ~/.bash_profile
```

### 3. Start Using

```bash
cd your-project
gemini
```

## Recommended Models and Groups

| Use Case | Model | Group | Rate |
|----------|-------|-------|------|
| Daily use | `gemini-2.5-flash` | gemini-cli | 1.0x |
| Lightweight tasks | `gemini-2.5-flash-lite` | gemini-cli | 1.0x |
| Complex tasks | `gemini-2.5-pro` | gemini-cli | 1.0x |
| Image generation | `gemini-3-pro-image` | premium-gemini | 2.4x |

## Specifying a Model

```bash
# Use a specific model
gemini --model gemini-2.5-pro

# Or switch in interactive mode
> /model gemini-2.5-flash
```

## Windows Configuration

```powershell
$env:GEMINI_API_KEY="your Levolink API Key"
$env:GEMINI_API_BASE="https://ai.levolink.com/v1"
gemini
```

Permanent setting:

```powershell
[System.Environment]::SetEnvironmentVariable("GEMINI_API_KEY", "your-key", "User")
[System.Environment]::SetEnvironmentVariable("GEMINI_API_BASE", "https://ai.levolink.com/v1", "User")
```

## FAQ

### Q: Gemini CLI reports "Invalid API key"

Check that your environment variables are set correctly:

```bash
echo $GEMINI_API_KEY
echo $GEMINI_API_BASE
# Make sure the Base URL ends with /v1
```

### Q: Slow response times

The gemini-cli group (1.0x rate) is optimized for Gemini models and offers faster response speeds.

### Q: Does it support Gemini 3.5 Pro?

Yes. Use `--model gemini-3-pro-image` or switch in interactive mode.

## Related Links

- [Levolink AI Official Site](https://ai.levolink.com)
- [Gemini CLI Official Documentation](https://github.com/google-gemini/gemini-cli)
- [API Documentation](https://levolink.apifox.cn/)
- [Model Selection Guide](./model-selection-guide.md)
