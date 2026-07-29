# OpenClaw Setup Guide

> Use Levolink AI as the backend model provider for OpenClaw.

## What is OpenClaw

OpenClaw is an open-source AI Agent runtime that supports multi-model scheduling, a skill system, scheduled tasks, a memory system, and more. By configuring an OpenAI-compatible API endpoint, you can connect it to Levolink AI.

## Configuration Steps

### 1. Install OpenClaw

```bash
# Install via npm
npm install -g openclaw

# Or using Docker
docker run -d openclaw/openclaw
```

### 2. Configure Gateway

Edit OpenClaw's Gateway configuration file (typically at `~/.openclaw/config.yaml` or `config.yaml` in the project directory):

```yaml
# Model configuration
model:
  # Default model
  default: volces/glm-5.2

  # OpenAI-compatible provider
  providers:
    - name: levolink
      api_key: "your Levolink API Key"
      base_url: "https://ai.levolink.com/v1"
      models:
        - gpt-5.6-sol
        - gpt-5.6-luna
        - claude-sonnet-4-6
        - claude-opus-4-8
        - gemini-2.5-pro
        - deepseek-reasoner
```

### 3. Or Configure via Environment Variables

```bash
# Add to ~/.bash_profile or ~/.zshrc
export OPENAI_API_KEY="your Levolink API Key"
export OPENAI_API_BASE="https://ai.levolink.com/v1"

source ~/.bash_profile
```

### 4. Start OpenClaw

```bash
openclaw gateway start

# Check status
openclaw status
```

## Recommended Model Configuration

| Use Case | Model | Group Suggestion |
|----------|-------|-----------------|
| Agent daily tasks | `gpt-5.6-luna` | Codex Exclusive (0.8x) |
| Complex reasoning | `claude-opus-4-8` | Default (1.0x) |
| Coding tasks | `claude-sonnet-4-6` | Default (1.0x) |
| Long context processing | `gemini-2.5-pro` | gemini-cli (1.0x) |
| Best value | `deepseek-reasoner` | Limited-time discount (0.6x) |

## Session Model Switching

OpenClaw supports specifying different models for different sessions:

```bash
# Switch model in a session
/model claude-opus-4-8

# View current model
/status
```

## Multi-Model Scheduling

OpenClaw supports scheduling multiple models simultaneously, ideal for Agent parallel tasks:

```yaml
# Configure multiple providers to use simultaneously
model:
  providers:
    - name: levolink-gpt
      api_key: "your-key"
      base_url: "https://ai.levolink.com/v1"
    - name: levolink-claude
      api_key: "your-key"
      base_url: "https://ai.levolink.com/v1"
```

## FAQ

### Q: OpenClaw reports "model not available"

Check that the Gateway is running and the model name is correct:

```bash
openclaw status
openclaw models list
```

### Q: How do I set the default model?

Set `model.default` in the configuration file, or use the `/model` command in a session.

### Q: Does it support streaming output?

Yes. OpenClaw uses streaming output by default.

### Q: How do I control costs?

1. Use the limited-time discount group (0.6x rate)
2. Choose appropriate models for different tasks
3. Set token limits in the configuration

## Related Links

- [Levolink AI Official Site](https://ai.levolink.com)
- [OpenClaw Official Documentation](https://docs.openclaw.ai)
- [OpenClaw GitHub](https://github.com/openclaw/openclaw)
- [API Documentation](https://levolink.apifox.cn/)
- [Model Selection Guide](./model-selection-guide.md)
