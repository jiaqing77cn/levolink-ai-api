# 中转站掺水检测完全指南

> 如何检测 AI API 中转站是否用低价模型冒充高价模型。

## 为什么要检测

部分中转站为了利润，会用 GLM-4 等便宜模型冒充 GPT-5，用 Haiku 冒充 Opus。用户付了高价模型的钱，得到的是低端模型的输出。

## 检测方法

### 方法 1：推理能力测试

高端模型（GPT-5.6/Claude Opus 4.8）和低端模型在推理能力上有明显差距。

```python
from openai import OpenAI

client = OpenAI(api_key="你的Key", base_url="https://ai.levolink.com/v1")

# 测试 1：经典推理题
resp = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": """
    A farmer has 17 sheep. All but 9 die. How many are left?
    Think step by step.
    """}]
)
print(resp.choices[0].message.content)
# GPT-5.6 正确答案: 9 (all but 9 died = 9 survived)
# 低端模型经常答: 8
```

### 方法 2：长上下文测试

高端模型支持 200K+ token 上下文，低端模型通常只有 8K-32K。

```python
# 发送 100K+ token 的长文本，在结尾放一个特定信息
# 然后问模型这个信息是什么
# 低端模型会丢失上下文，答不上来

long_text = "这是一段很长的文本..." * 5000  # 约 100K tokens
long_text += "密码是：PurpleDragon42"

resp = client.chat.completions.create(
    model="claude-opus-4-8",
    messages=[{"role": "user", "content": long_text + "\n\n密码是什么？"}]
)
# Claude Opus 4.8 能正确回答 PurpleDragon42
# 低端模型会丢失上下文
```

### 方法 3：代码能力测试

```python
resp = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": """
    用 Python 实现一个线程安全的 LRU 缓存：
    1. 支持 TTL 过期
    2. 支持 maxsize 限制
    3. 线程安全
    4. 带命中率统计
    """}]
)
# Claude Sonnet 4.6 会给出完整实现
# 低端模型会给出不完整或有 bug 的代码
```

### 方法 4：Token 计费验证

```python
import tiktoken

# 用 tiktoken 计算 token 数
enc = tiktoken.encoding_for_model("gpt-5.6-sol")
text = "Hello, world! " * 1000
tokens = enc.encode(text)
print(f"实际 token 数: {len(tokens)}")

# 发送请求，对比计费 token 数
resp = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": text}]
)
print(f"API 返回的 prompt_tokens: {resp.usage.prompt_tokens}")
# 如果 API 返回的比实际多很多，说明计费有问题
```

### 方法 5：响应速度对比

```python
import time

start = time.time()
resp = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": "Say hello"}]
)
elapsed = time.time() - start

# 正常延迟：0.5-2s
# 如果 >5s 可能是在转发到低端模型
# 如果 <0.1s 可能是缓存
print(f"延迟: {elapsed:.2f}s")
```

## Levolink AI 的透明度

Levolink AI 提供 33 个分组，每个分组明确标注后端渠道：

| 分组 | 后端 | 倍率 | 透明度 |
|------|------|------|--------|
| 限时特价 | 混合渠道 | 0.6x | 最便宜，质量可能波动 |
| Codex 专属 | GPT 编程优化 | 0.8x | 性价比最高 |
| 默认 | Azure + MJ | 1.0x | 标准质量 |
| CC 专属 | Claude 优化 | 2.4x | Claude Code 最佳 |
| AWS 企业级 | AWS Bedrock | 4.0x | 企业级稳定 |
| 正价官转 | 官方直连 | 16.0x | 100% 官方品质 |

用户可以根据需求选择，价格透明，不掺水。
