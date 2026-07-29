# Dify Integration Guide

> Connect Dify to Levolink AI — one API Key to access 500+ AI models.

## What is Dify

Dify is an open-source LLM application development platform that supports knowledge base management, agent orchestration, and workflow automation. By connecting to Levolink AI, Dify can access GPT-5.6, Claude 4.8, Gemini, DeepSeek, and all other supported models.

## Configuration Steps

### 1. Get Your Levolink API Key

Go to [Levolink AI](https://ai.levolink.com) -> Register -> Dashboard -> Create Key

### 2. Configure Model Provider in Dify

In Dify, go to Settings -> Model Providers -> Select **OpenAI API Compatible**:

| Setting | Value |
|---------|-------|
| API Key | Your Levolink API Key |
| API endpoint | `https://ai.levolink.com/v1` |
| Model name | `gpt-5.6-sol` / `claude-sonnet-4-6` / `deepseek-reasoner`, etc. |

### 3. Add Multiple Models

In Dify's "Models" page, add the models you need one by one:

**Recommended configuration:**

| Use Case | Model | Recommended Group |
|----------|-------|-------------------|
| Chat assistant | `claude-sonnet-4-6` | Default (1.0x) |
| Coding assistant | `gpt-5.6-sol` | Codex Dedicated (0.8x) |
| Long text processing | `gemini-2.5-pro` | Gemini-CLI Mixed (1.0x) |
| Reasoning tasks | `deepseek-reasoner` | Limited-time Sale (0.6x) |
| Daily chat | `gpt-5.6-luna` | Codex Dedicated (0.8x) |

### 4. Use in Your Applications

When creating an app, simply select the added model from the "Model" dropdown.

## RAG Knowledge Base Configuration

Using Dify's knowledge base feature with Levolink AI:

1. **Embedding model**: Use `text-embedding-3-large` (supported by Levolink)
2. **Rerank model**: Not currently supported; you can disable reranking
3. **Chat model**: Recommend `claude-sonnet-4-6` or `gpt-5.6-sol`

### Knowledge Base Cost Estimation

| Documents | Embedding Cost | Cost per Query |
|-----------|---------------|----------------|
| 100 | ~$0.02 | ~$0.01 |
| 1,000 | ~$0.20 | ~$0.01 |
| 10,000 | ~$2.00 | ~$0.02 |

## Agent Workflow Configuration

A typical Dify Agent + Levolink AI workflow:

```
User input -> Claude Sonnet 4.6 (intent recognition)
            -> DeepSeek R1 (reasoning & analysis)
            -> GPT-5.6 Sol (response generation)
```

One API Key can orchestrate all models — no need for multiple accounts.

## Docker-Deployed Dify

If you deployed Dify with Docker, set environment variables in `docker-compose.yml`:

```yaml
services:
  api:
    environment:
      - OPENAI_API_KEY=your Levolink Key
      - OPENAI_API_BASE=https://ai.levolink.com/v1
```

## FAQ

### Q: Dify reports "model not found"

Make sure the model name matches exactly. See the [README pricing table](../../README_EN.md#-live-model-pricing) for the full list of supported models.

### Q: Streaming output doesn't work

Enable the "Streaming output" option in Dify's model settings. All Levolink models support streaming.

### Q: How to control costs

1. Use the Limited-time Sale group (0.6x multiplier)
2. Use Gemini 2.5 Flash for long texts ($0.30/M input)
3. Use GPT-5.6 Luna for daily chat ($0.80/M input)
4. Set token limits in Dify

## Related Links

- [Levolink AI Website](https://ai.levolink.com)
- [Dify Official Docs](https://docs.dify.ai)
- [API Documentation](https://levolink.apifox.cn/)
- [Model Selection Guide](./model-selection-guide.md)
- [Cost Calculator](./cost-calculator-guide.md)
