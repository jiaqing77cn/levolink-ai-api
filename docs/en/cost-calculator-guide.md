# Cost Calculator Guide

> Estimate your AI API costs and find the most cost-effective model and group combination.

## Quick Cost Estimation

### Basic Concepts

| Term | Meaning |
|------|---------|
| Input Token | Text you send to the model (including system prompts, context) |
| Output Token | Text the model returns |
| Multiplier | Price coefficient for the group — lower is cheaper |
| Output/Input Ratio | Output price / input price (typically 3-8x) |

### Approximate Token Counts per Conversation

| Scenario | Input Tokens | Output Tokens |
|----------|-------------|---------------|
| Simple Q&A | 50-200 | 100-500 |
| Code generation | 200-1,000 | 500-2,000 |
| Long text analysis | 5,000-50,000 | 500-2,000 |
| Claude Code coding | 5,000-30,000 | 2,000-10,000 |

## Monthly Cost Estimates by Scenario

### Scenario 1: Daily AI Chat (Light Usage)

- 20 conversations per day
- ~500 input + 500 output = 1,000 tokens per conversation
- Monthly usage: ~600K tokens (300K input + 300K output)

| Model | Group | Monthly Cost |
|-------|-------|-------------|
| `gpt-5.6-luna` | Limited-time Sale (0.6x) | ~$0.36 |
| `gemini-2.5-flash` | Gemini-CLI Mixed (1.0x) | ~$0.90 |
| `claude-sonnet-5` | Default (1.0x) | ~$3.60 |

### Scenario 2: AI Coding Assistant (Moderate Usage)

- 50 code requests per day
- ~5,000 input + 2,000 output = 7,000 tokens per request
- Monthly usage: ~10.5M tokens (7.5M input + 3M output)

| Model | Group | Monthly Cost |
|-------|-------|-------------|
| `gpt-5.6-luna` | Codex Dedicated (0.8x) | ~$9.12 |
| `gpt-5.6-sol` | Codex Dedicated (0.8x) | ~$45.60 |
| `claude-sonnet-4-6` | Default (1.0x) | ~$67.50 |
| `claude-opus-4-8` | Default (1.0x) | ~$112.50 |

### Scenario 3: Claude Code Heavy Coding

- 100 requests per day
- ~15,000 input + 5,000 output = 20,000 tokens per request
- Monthly usage: ~60M tokens (45M input + 15M output)

| Model | Group | Monthly Cost |
|-------|-------|-------------|
| `claude-sonnet-4-6` | Default (1.0x) | ~$360 |
| `claude-sonnet-4-6` | CC Dedicated (2.4x) | ~$864 |
| `claude-opus-4-8` | Default (1.0x) | ~$600 |
| `gpt-5.6-sol` | Codex Dedicated (0.8x) | ~$228 |

### Scenario 4: Long Text Processing

- 10 document analyses per day
- ~50,000 input + 1,000 output per request
- Monthly usage: ~15.3M tokens (15M input + 300K output)

| Model | Group | Monthly Cost |
|-------|-------|-------------|
| `gemini-2.5-pro` | Gemini-CLI Mixed (1.0x) | ~$19.13 |
| `claude-opus-4-8` | Default (1.0x) | ~$82.50 |
| `gpt-5.6-sol` | Codex Dedicated (0.8x) | ~$50.40 |

## Cost-Saving Strategies

### 1. Group Selection

| Strategy | Group | Multiplier | Best For |
|----------|-------|-----------|----------|
| Most economical | Limited-time Sale | 0.6x | Testing, non-critical tasks |
| Best value | Codex Dedicated | 0.8x | Daily coding |
| Balanced | Default | 1.0x | Production environments |
| High stability | CC Dedicated | 2.4x | Claude Code coding |

### 2. Model Mixing

Don't rely on just one model. Recommended strategy:
- **Simple tasks** (translation, summarization): Gemini 2.5 Flash ($0.30/M input)
- **Daily coding**: GPT-5.6 Luna ($0.80/M input)
- **Complex coding**: Claude Sonnet 4.6 or GPT-5.6 Sol
- **Ultra-long text**: Gemini 2.5 Pro (1M context, $1.25/M input)

### 3. Cache Utilization

Levolink supports cached pricing (standard 10%). For scenarios with repeated identical context (like Claude Code), caching can significantly reduce costs.

### 4. Set Token Limits

Set max_tokens limits at the application layer to avoid unexpected overspending.

## Using the Cost Calculator Script

The repository includes a cost calculator script:

```bash
cd levolink-ai-api
python scripts/cost_calculator.py
```

Enter your estimated usage to automatically calculate monthly costs across models and groups.

## Related Links

- [Full Pricing Table](../../README_EN.md#-live-model-pricing)
- [Model Selection Guide](./model-selection-guide.md)
- [Levolink AI Pricing Page](https://ai.levolink.com/pricing)
