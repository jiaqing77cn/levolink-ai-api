# 프록시 물타기 검출 완전 가이드

> AI API 프록시이 저가 모델로 고가 모델을 대체하는지 검출하는 방법.

## 왜 검출해야 하는가?

일부 프록시은 이윤을 위해 GLM-4 등 저렴한 모델로 GPT-5를 대체하고, Haiku로 Opus를 대체합니다. 사용자는 고가 모델의 비용을 지불하지만 저가 모델의 출력을 받게 됩니다.

## 검출 방법

### 방법 1: 추론 능력 테스트

고성능 모델(GPT-5.6/Claude Opus 4.8)과 저성능 모델은 추론 능력에서 뚜렷한 차이가 있습니다.

```python
from openai import OpenAI

client = OpenAI(api_key="당신의Key", base_url="https://ai.levolink.com/v1")

# 테스트 1: 고전 추론 문제
resp = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": """
    A farmer has 17 sheep. All but 9 die. How many are left?
    Think step by step.
    """}]
)
print(resp.choices[0].message.content)
# GPT-5.6 정답: 9 (all but 9 died = 9 survived)
# 저성능 모델은 종종: 8이라고 답함
```

### 방법 2: 긴 컨텍스트 테스트

고성능 모델은 200K+ token 컨텍스트를 지원하지만, 저성능 모델은 일반적으로 8K-32K만 지원합니다.

```python
# 100K+ token의 긴 텍스트를 보내고, 끝에 특정 정보를 배치
# 그런 다음 모델에게 그 정보가 무엇인지 질문
# 저성능 모델은 컨텍스트를 잃어버리고 대답하지 못함

long_text = "이것은 아주 긴 텍스트입니다..." * 5000  # 약 100K tokens
long_text += "비밀번호는: PurpleDragon42"

resp = client.chat.completions.create(
    model="claude-opus-4-8",
    messages=[{"role": "user", "content": long_text + "\n\n비밀번호는 무엇인가요?"}]
)
# Claude Opus 4.8은 PurpleDragon42를 정확히 대답
# 저성능 모델은 컨텍스트를 잃어버림
```

### 방법 3: 코드 능력 테스트

```python
resp = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": """
    Python으로 스레드 안전한 LRU 캐시를 구현하세요:
    1. TTL 만료 지원
    2. maxsize 제한 지원
    3. 스레드 안전
    4. 적중률 통계 포함
    """}]
)
# Claude Sonnet 4.6은 완전한 구현을 제공
# 저성능 모델은 불완전하거나 버그가 있는 코드를 제공
```

### 방법 4: Token 과금 검증

```python
import tiktoken

# tiktoken으로 token 수 계산
enc = tiktoken.encoding_for_model("gpt-5.6-sol")
text = "Hello, world! " * 1000
tokens = enc.encode(text)
print(f"실제 token 수: {len(tokens)}")

# 요청을 보내고 과금 token 수를 비교
resp = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": text}]
)
print(f"API가 반환한 prompt_tokens: {resp.usage.prompt_tokens}")
# API가 실제보다 훨씬 많이 반환하면 과금에 문제가 있음
```

### 방법 5: 응답 속도 비교

```python
import time

start = time.time()
resp = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": "Say hello"}]
)
elapsed = time.time() - start

# 정상 지연: 0.5-2s
# 5s 이상이면 저성능 모델로 전송 중일 수 있음
# 0.1s 미만이면 캐시일 수 있음
print(f"지연: {elapsed:.2f}s")
```

## Levolink AI의 투명성

Levolink AI는 33개 그룹을 제공하며, 각 그룹의 백엔드 채널을 명확히 표시합니다:

| 그룹 | 백엔드 | 배율 | 투명성 |
|------|------|------|--------|
| 한정 특가 | 혼합 채널 | 0.6x | 가장 저렴, 품질 변동 가능 |
| Codex 전용 | GPT 프로그래밍 최적화 | 0.8x | 가장 높은 가성비 |
| 기본 | Azure + MJ | 1.0x | 표준 품질 |
| CC 전용 | Claude 최적화 | 2.4x | Claude Code에 최적 |
| AWS 엔터프라이즈 | AWS Bedrock | 4.0x | 엔터프라이즈급 안정성 |
| 정가 공식 전송 | 공식 직결 | 16.0x | 100% 공식 품질 |

사용자는 필요에 따라 선택할 수 있으며, 가격이 투명하고 물타기가 없습니다.
