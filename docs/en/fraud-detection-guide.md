# API Proxy Fraud Detection Complete Guide

> How to detect whether an AI API proxy is substituting cheap models for premium ones.

## Why Detection Matters

Some API proxies substitute cheap models like GLM-4 for GPT-5, or Haiku for Opus, to maximize profit. Users pay premium model prices but receive output from low-end models.

## Detection Methods

### Method 1: Reasoning Ability Test

Premium models (GPT-5.6/Claude Opus 4.8) and low-end models have a clear gap in reasoning ability.

```python
from openai import OpenAI

client = OpenAI(api_key="your Key", base_url="https://ai.levolink.com/v1")

# Test 1: Classic reasoning puzzle
resp = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": """
    A farmer has 17 sheep. All but 9 die. How many are left?
    Think step by step.
    """}]
)
print(resp.choices[0].message.content)
# GPT-5.6 correct answer: 9 (all but 9 died = 9 survived)
# Low-end models often answer: 8
```

### Method 2: Long Context Test

Premium models support 200K+ token context, while low-end models typically only support 8K-32K.

```python
# Send a 100K+ token long text with a specific piece of info at the end
# Then ask the model what that info is
# Low-end models will lose context and fail to answer

long_text = "This is a long text..." * 5000  # ~100K tokens
long_text += "The password is: PurpleDragon42"

resp = client.chat.completions.create(
    model="claude-opus-4-8",
    messages=[{"role": "user", "content": long_text + "\n\nWhat is the password?"}]
)
# Claude Opus 4.8 can correctly answer PurpleDragon42
# Low-end models will lose context
```

### Method 3: Code Capability Test

```python
resp = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": """
    Implement a thread-safe LRU cache in Python:
    1. Support TTL expiration
    2. Support maxsize limit
    3. Thread-safe
    4. Include hit rate statistics
    """}]
)
# Claude Sonnet 4.6 will provide a complete implementation
# Low-end models will produce incomplete or buggy code
```

### Method 4: Token Billing Verification

```python
import tiktoken

# Use tiktoken to count tokens
enc = tiktoken.encoding_for_model("gpt-5.6-sol")
text = "Hello, world! " * 1000
tokens = enc.encode(text)
print(f"Actual token count: {len(tokens)}")

# Send request and compare billed token count
resp = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": text}]
)
print(f"API returned prompt_tokens: {resp.usage.prompt_tokens}")
# If the API returns significantly more than actual, billing may be inflated
```

### Method 5: Response Speed Comparison

```python
import time

start = time.time()
resp = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": "Say hello"}]
)
elapsed = time.time() - start

# Normal latency: 0.5-2s
# If >5s, it may be forwarding to a low-end model
# If <0.1s, it may be cached
print(f"Latency: {elapsed:.2f}s")
```

## Levolink AI Transparency

Levolink AI provides 33 channel groups, each clearly labeled with its backend provider:

| Group | Backend | Multiplier | Transparency |
|-------|---------|-----------|-------------|
| Limited-time Sale | Mixed channels | 0.6x | Cheapest, quality may vary |
| Codex Dedicated | GPT coding optimized | 0.8x | Best value |
| Default | Azure + MJ | 1.0x | Standard quality |
| CC Dedicated | Claude optimized | 2.4x | Best for Claude Code |
| AWS Enterprise | AWS Bedrock | 4.0x | Enterprise-grade stability |
| Official Direct | Official direct connection | 16.0x | 100% official quality |

Users can choose based on their needs. Pricing is transparent — no model substitution.
