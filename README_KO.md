<h1 align="center">🚀 중국 AI API 프록시 | VPN 없이 Claude/GPT/Gemini/DeepSeek 직접 연결 | Levolink AI</h1>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License"/>
  <img src="https://img.shields.io/badge/500%2B-Models-34d399?style=flat" alt="Models"/>
  <img src="https://img.shields.io/badge/CDN-China%20Accel-3b82f6?style=flat" alt="CDN"/>
  <img src="https://img.shields.io/badge/OpenAI-Compatible-10a37f?style=flat" alt="OpenAI Compatible"/>
</p>

<div align="center">

**VPN 불필요 · 저지연 · 500+ 모델 · OpenAI Compatible · Claude Code Ready**

[🌐 웹사이트](https://ai.levolink.com) · [📋 가격](https://ai.levolink.com/pricing) · [📖 API 문서](https://levolink.apifox.cn/) · [💬 문의](https://ai.levolink.com)

</div>

> Last updated: 2026-08-04 16:48 (UTC+8)| [中文](./README.md) | [English](./README_EN.md) | 한국어 | [日本語](./README_JA.md) | [Español](./README_ES.md) | [Deutsch](./README_DE.md)

---

## 📋 목차

- [🖥️ 제품 미리보기](#-제품-미리보기)
- [🔍 API 프록시 선택 방법](#-api-프록시-선택-방법)
- [💰 실시간 모델 가격](#-실시간-모델-가격)
- [🛠️ 연동 가이드](#-연동-가이드)
- [📊 비교](#-비교)
- [❓ FAQ](#-faq)
- [📖 심층 가이드](#-심층-가이드)
- [🤝 기여하기](#-기여하기)

---

## 🖥️ 제품 미리보기

![Levolink AI 홈페이지 - 500+ AI 모델 API 프록시 대시보드](https://raw.githubusercontent.com/jiaqing77cn/levolink-ai-api/main/assets/homepage.jpg)

![Levolink AI 콘솔 - API 키 생성, 사용량 확인, 계정 충전](https://raw.githubusercontent.com/jiaqing77cn/levolink-ai-api/main/assets/console.jpg)

---

## 🔍 API 프록시 선택 방법

AI API 프록시를 선택할 때 평가해야 할 6가지 기준:

| 평가 기준 | 확인 사항 | 위험 신호 |
|-----------|----------|----------|
| **안정성** | 잦은 다운타임이 있는가? 지연이 심한가? | 연결 끊김, 공지 없음 |
| **속도** | 응답 지연이 허용 범위인가? | 첫 토큰까지 5초 이상 |
| **모델 커버리지** | 최신 모델을 사용할 수 있는가? | 신모델 추가가 느림 |
| **가격 투명성** | 청구가 명확한가? 사용 로그가 있는가? | 호출 기록 없음, 불투명 |
| **모델 치환** | 저렴한 모델을 고급 모델로 둔갑하는가? | 비정상적으로 낮은 가격, 품질 저하 |
| **서비스 종료 위험** | 기업 운영인가? 지원이 있는가? | 개인 운영, 고객 지원 없음 |

### ⚠️ 주의사항 체크리스트

1. **캐시 가격 함정**: 정상적인 캐시 가격은 10%이지만, 일부는 15%-30%를 청구합니다
2. **모델 치환 감지**: 동일한 프롬프트로 공식 API와 프록시의 출력을 비교하세요
3. **토큰 수 조작 확인**: 알려진 토큰 수로 요청을 보내 청구가 부풀려지는지 확인하세요
4. **저가 함정**: 시장 가격보다 훨씬 낮은 가격은 GLM을 GPT로 둔갑할 가능성이 높습니다
5. **서비스 종료 위험**: 대금을 많이 예치하지 마세요! 사용한 만큼만 결제하세요

### 🔬 모델 치환 감지 방법

```python
# 방법 1: 능력 테스트 - 추론 프롬프트 사용
prompt = "A farmer has 17 sheep. All but 9 die. How many are left?"
# GPT/Claude 정답: 9
# 저급 모델은 종종 틀림: 8

# 방법 2: 긴 컨텍스트 테스트
# 50K+ 토큰의 긴 텍스트를 보내고 끝부분의 내용을 질문하세요
# 저급 모델은 컨텍스트를 잃어버림

# 방법 3: 코드 능력 테스트
prompt = "Implement an LRU cache with TTL expiration in Python"
# 공식 API와 프록시의 코드 품질을 비교하세요
```

---

## 💰 실시간 모델 가격

> 가격은 GitHub Actions가 [Levolink API](https://ai.levolink.com/api/pricing)에서 자동으로 가져오며, 매시간 업데이트됩니다.
>
> 단위: USD / Million Tokens | 출력/입력 비율 = 출력 가격 ÷ 입력 가격

### OpenAI GPT 시리즈

<!-- GPT_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `gpt-5-codex` | Enterprise Azure 2 | 0.35x | $0.44 | $3.50 | Codex Exclusive | 0.8x | $1.00 | $8.00 | 8x |
| `gpt-5-mini` | Enterprise Azure 2 | 0.35x | $0.09 | $0.70 | Special-Premium GPT | 5.6x | $1.40 | $11.20 | 8x |
| `gpt-5-mini-2025-08-07` | Enterprise Azure 2 | 0.35x | $0.09 | $0.70 | Special-Premium GPT | 5.6x | $1.40 | $11.20 | 8x |
| `gpt-5-nano` | Enterprise Azure 2 | 0.35x | $0.02 | $0.14 | Special-Premium GPT | 5.6x | $0.28 | $2.24 | 8x |
| `gpt-5-nano-2025-08-07` | Enterprise Azure 2 | 0.35x | $0.02 | $0.14 | Special-Premium GPT | 5.6x | $0.28 | $2.24 | 8x |
| `gpt-5-pro` | Enterprise Azure 2 | 0.35x | $5.25 | $42.00 | Special-Premium GPT | 5.6x | $84.00 | $672.00 | 8x |
| `gpt-5.1-codex` | Sale 10% Off | 0.54x | $0.68 | $5.40 | Codex Exclusive | 0.8x | $1.00 | $8.00 | 8x |
| `gpt-5.1-codex-max` | Sale 10% Off | 0.54x | $0.68 | $5.40 | Pure Azure | 1.5x | $1.88 | $15.00 | 8x |
| `gpt-5.1-codex-mini` | Enterprise Azure 2 | 0.35x | $0.09 | $0.70 | Pure Azure | 1.5x | $0.38 | $3.00 | 8x |
| `gpt-5.2-chat` | Enterprise Azure 2 | 0.35x | $0.61 | $4.90 | Special-Premium GPT | 5.6x | $9.80 | $78.40 | 8x |
| `gpt-5.2-chat-latest` | Enterprise Azure 2 | 0.35x | $0.61 | $4.90 | Special-Premium GPT | 5.6x | $9.80 | $78.40 | 8x |
| `gpt-5.2-codex` | Sale 10% Off | 0.54x | $0.95 | $7.56 | Special-Premium GPT | 5.6x | $9.80 | $78.40 | 8x |
| `gpt-5.3-chat-latest` | Enterprise Azure 2 | 0.35x | $0.61 | $4.90 | Special-Premium GPT | 5.6x | $9.80 | $78.40 | 8x |
| `gpt-5.3-codex` | Sale 10% Off | 0.54x | $0.95 | $7.56 | Special-Premium GPT | 5.6x | $9.80 | $78.40 | 8x |
| `gpt-5.3-codex-spark` | Codex Exclusive | 0.8x | $1.40 | $11.20 | Premium OpenAI | 8x | $14.00 | $112.00 | 8x |

<!-- GPT_PRICE_TABLE_END -->

### Anthropic Claude 시리즈

<!-- CLAUDE_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `claude-fable-5` | Default | 1x | $10.00 | $50.00 | Claude Code Exclusive | 2.4x | $24.00 | $120.00 | 5x |
| `claude-haiku-4-5-20251001` | Default | 1x | $1.00 | $5.00 | Claude Code Exclusive | 2.4x | $2.40 | $12.00 | 5x |
| `claude-opus-4-1-20250805` | Default | 1x | $15.00 | $75.00 | Relay Claude 1 | 4x | $60.00 | $300.00 | 5x |
| `claude-opus-4-5-20251101` | Default | 1x | $5.00 | $25.00 | Claude Code Exclusive | 2.4x | $12.00 | $60.00 | 5x |
| `claude-opus-4-6` | Default | 1x | $5.00 | $25.00 | Claude Code Exclusive | 2.4x | $12.00 | $60.00 | 5x |
| `claude-opus-4-7` | Default | 1x | $5.00 | $25.00 | Claude Code Exclusive | 2.4x | $12.00 | $60.00 | 5x |
| `claude-opus-4-8` | Default | 1x | $5.00 | $25.00 | Claude Code Exclusive | 2.4x | $12.00 | $60.00 | 5x |
| `claude-sonnet-4-20250514` | Default | 1x | $3.00 | $15.00 | Relay Claude 1 | 4x | $12.00 | $60.00 | 5x |
| `claude-sonnet-4-5-20250929` | Default | 1x | $3.00 | $15.00 | Claude Code Exclusive | 2.4x | $7.20 | $36.00 | 5x |
| `claude-sonnet-4-6` | Default | 1x | $3.00 | $15.00 | Claude Code Exclusive | 2.4x | $7.20 | $36.00 | 5x |
| `claude-sonnet-5` | Default | 1x | $2.00 | $10.00 | Claude Code Exclusive | 2.4x | $4.80 | $24.00 | 5x |

<!-- CLAUDE_PRICE_TABLE_END -->

### Google Gemini 시리즈

<!-- GEMINI_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `gemini-2.0-flash-lite` | Relay Gemini | 3.6x | $0.27 | $1.08 | Premium Gemini | 6x | $0.45 | $1.80 | 4x |
| `gemini-2.5-flash` | Gemini CLI | 1x | $0.30 | $2.50 | Premium Gemini | 6x | $1.80 | $15.01 | 8.34x |
| `gemini-2.5-flash-image` | Premium Gemini | 2.4x | $0.00 | $0.00 | Premium Gemini | 6x | $0.00 | $0.00 | 0x |
| `gemini-2.5-flash-lite` | Gemini CLI | 1x | $0.10 | $0.40 | Premium Gemini | 6x | $0.60 | $2.40 | 4x |
| `gemini-2.5-pro` | Gemini CLI | 1x | $1.25 | $10.00 | Premium Gemini | 6x | $7.50 | $60.00 | 8x |
| `gemini-3-pro-image` | Premium Gemini | 2.4x | $0.00 | $0.00 | Premium Gemini | 6x | $0.00 | $0.00 | 0x |
| `gemini-3.1-flash-image` | Premium Gemini | 2.4x | $0.00 | $0.00 | Premium Gemini | 6x | $0.00 | $0.00 | 0x |
| `gemini-3.1-flash-lite` | Gemini CLI | 1x | $0.25 | $1.50 | Premium Gemini | 6x | $1.50 | $9.00 | 6x |

<!-- GEMINI_PRICE_TABLE_END -->

### DeepSeek 시리즈

<!-- DEEPSEEK_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `deepseek-r1` | UChat Qwen | 0.6x | $2.40 | $9.60 | Pure Azure | 1.5x | $6.00 | $24.00 | 4x |
| `deepseek-r1-0528` | UChat Qwen | 0.6x | $2.40 | $9.60 | Pure Azure | 1.5x | $6.00 | $24.00 | 4x |
| `deepseek-r1-2025-01-20` | UChat Qwen | 0.6x | $2.40 | $9.60 | Pure Azure | 1.5x | $6.00 | $24.00 | 4x |
| `deepseek-r1-250120` | UChat Qwen | 0.6x | $2.40 | $9.60 | Pure Azure | 1.5x | $6.00 | $24.00 | 4x |
| `deepseek-r1-250528` | UChat Qwen | 0.6x | $2.40 | $9.60 | Pure Azure | 1.5x | $6.00 | $24.00 | 4x |
| `deepseek-r1-distill-qwen-32b` | Special-Domestic 40% | 0.8x | $1.60 | $4.80 | Pure Azure | 1.5x | $3.00 | $9.00 | 3x |
| `deepseek-r1-distill-qwen-7b` | Special-Domestic 40% | 0.8x | $0.40 | $0.80 | Pure Azure | 1.5x | $0.75 | $1.50 | 2x |
| `deepseek-reasoner` | UChat Qwen | 0.6x | $2.40 | $9.60 | Pure Azure | 1.5x | $6.00 | $24.00 | 4x |

<!-- DEEPSEEK_PRICE_TABLE_END -->

### 중국 모델 (Qwen/Doubao/GLM/Kimi/MiniMax)

<!-- CN_MODEL_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `qwen3-max` | Flash Sale | 0.6x | $1.50 | $6.00 | Pure Azure | 1.5x | $3.75 | $15.00 | 4x |
| `qwen3-max-2026-01-23` | Alibaba 40% | 0.8x | $2.00 | $8.00 | Pure Azure | 1.5x | $3.75 | $15.00 | 4x |
| `qwen3-coder` | Special-Domestic 40% | 0.8x | $4.80 | $19.20 | Pure Azure | 1.5x | $9.00 | $36.00 | 4x |
| `qwen3-coder-plus` | Flash Sale | 0.6x | $2.40 | $9.60 | Special-HC1 | 1.32x | $5.28 | $21.12 | 4x |
| `qwen3.6-plus` | Default | 1x | $2.00 | $12.00 | Pure Azure | 1.5x | $3.00 | $18.00 | 6x |
| `qwen3.7-max` | Flash Sale | 0.6x | $7.20 | $21.60 | Pure Azure | 1.5x | $18.00 | $54.00 | 3x |
| `glm-4.6` | Flash Sale | 0.6x | $1.20 | $4.80 | Pure Azure | 1.5x | $3.00 | $12.00 | 4x |
| `glm-4.5` | Flash Sale | 0.6x | $0.96 | $3.84 | Pure Azure | 1.5x | $2.40 | $9.60 | 4x |
| `glm-4.5-air` | Flash Sale | 0.6x | $0.48 | $3.60 | Pure Azure | 1.5x | $1.20 | $9.00 | 7.5x |
| `kimi-k2` | Special-Domestic 40% | 0.8x | $3.20 | $12.80 | Special-Premium GPT | 5.6x | $22.40 | $89.60 | 4x |
| `kimi-k2.5` | Special-Domestic 40% | 0.8x | $3.20 | $16.80 | Pure Azure | 1.5x | $6.00 | $31.50 | 5.25x |
| `kimi-k3` | Pure Azure | 1.5x | $30.00 | $150.00 | Official Relay | 3x | $60.00 | $300.00 | 5x |

<!-- CN_MODEL_PRICE_TABLE_END -->

> 💡 33개 그룹 및 228개 모델의 전체 가격표는 [Levolink AI 가격 페이지](https://ai.levolink.com/pricing)에서 확인하세요

### 그룹 등급

| 그룹 유형 | 비율 | 추천 용도 |
|-----------|------|----------|
| 플래시 세일 | 0.6x | 테스트, 저비용 사용 |
| Codex 전용 | 0.8x | GPT 코딩, 일일 사용 |
| 기본 | 1.0x | 표준 품질, 균형 잡힌 선택 |
| anti/kiro | 1.2x | 가성비 Claude |
| Claude Code 전용 | 2.4x | Claude Code 프로그래밍 |
| Azure 채널 | 3.0x | 안정적인 GPT |
| AWS 엔터프라이즈 | 4.0x | 엔터프라이즈급 Claude |
| Vertex/직접 | 6.0x | 최고 품질 |
| 공식 프리미엄 | 16.0x | 완전한 공식 품질 |

---

## 🛠️ 연동 가이드

### 빠른 시작

1. [Levolink AI](https://ai.levolink.com) 방문 -> 회원가입 -> 콘솔 -> 키 생성
2. 충전 (최소 1위안)
   - Alipay / WeChat Pay / Crypto Pay / Stripe / Global Pay
3. 연동 방법 선택:

### Python (OpenAI SDK)

```python
from openai import OpenAI

client = OpenAI(
    api_key="***",
    base_url="https://ai.levolink.com/v1"
)

# GPT-5.6 Sol
resp = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": "Write a Python quicksort"}]
)

# Claude Sonnet 4.6
resp = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": "Explain quantum computing"}],
    extra_body={"anthropic_version": "vertex-2023-10-01"}
)

# DeepSeek R1
resp = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[{"role": "user", "content": "Implement a web server in Python"}]
)
```

### Node.js / curl

```bash
curl https://ai.levolink.com/v1/chat/completions \
  -H "Authorization: Bearer ***" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.6-sol",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

전체 예제는 [`examples/`](./examples/) 디렉토리에서 확인하세요 ([Python](examples/quickstart.py) / [Node.js](examples/quickstart.js) / [Shell](examples/quickstart.sh) 포함).

### Claude Code

```bash
npm install -g @anthropic-ai/claude-code

echo 'export ANTHROPIC_AUTH_TOKEN="***"' >> ~/.bash_profile
echo 'export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"' >> ~/.bash_profile
source ~/.bash_profile

cd your-project && claude
```

📖 전체 가이드: [Claude Code 설정](docs/ko/claude-code-guide.md)

### OpenAI Codex

```bash
npm install -g @openai/codex
export OPENAI_API_KEY="***"
export OPENAI_API_BASE="https://ai.levolink.com/v1"
```

📖 전체 가이드: [Codex 설정](docs/ko/codex-setup.md)

### Gemini CLI

```bash
npm install -g @google/gemini-cli
export GEMINI_API_KEY="***"
export GEMINI_API_BASE="https://ai.levolink.com/v1"
```

📖 전체 가이드: [Cursor IDE 설정](docs/ko/cursor-setup.md) (Gemini CLI에도 동일하게 적용)

### 도구 연동

| 도구 | 설정 |
|------|------|
| **Dify / FastGPT** | API Key + Base URL: `https://ai.levolink.com/v1` |
| **n8n** | HTTP Request -> URL: `https://ai.levolink.com/v1/chat/completions` |
| **LangChain** | `ChatOpenAI(openai_api_key="key", openai_api_base="https://ai.levolink.com/v1")` |
| **NextChat** | 설정 -> 커스텀 API -> URL: `https://ai.levolink.com/v1` |
| **Cursor IDE** | 설정 -> 환경변수 -> `ANTHROPIC_BASE_URL=https://ai.levolink.com/v1` |
| **OpenClaw** | `openai_api_key: key` + `openai_api_base: https://ai.levolink.com/v1` |

### 사용 사례

- **AI 코딩** - Claude Code / Codex와 Claude 4.8 / GPT-5.6으로 리팩토링, 버그 수정
- **긴 문서 처리** - 10만 단 이상 분석, 계약서 검토, 논문 요약
- **AI 에이전트** - 하나의 키로 모든 모델 사용, 멀티 에이전트 병렬 작업
- **RAG 지식 베이스** - DeepSeek / GPT와 벡터 데이터베이스로 기업 Q&A 구축
- **자동화 워크플로우** - n8n / FastGPT / Dify 연동으로 전체 자동화

---

## 📊 2026년 비교 및 리뷰

> 2026-07-29 기준 공개 정보를 바탕으로 합니다. 참고용입니다.

| | [Levolink AI](https://ai.levolink.com) | OpenRouter | SiliconFlow | 기타 프록시 | 자체 구축 |
|--|-------------|-----------|-------------|---------------|------------|
| 모델 수 | **228+** | ~400 | ~200 | ~100 | 수동 |
| 그룹 옵션 | **33개 그룹** | 없음 (공급자별) | 없음 | 1-3개 | - |
| 중국 CDN | ✅ 다중 노드 | ❌ 중국 노드 없음 | ✅ 단일 | ✅ | ❌ |
| 최소 충전 | **¥1** | ~¥35 | ¥50 | ¥20 | - |
| 사용량 기반 결제 | ✅ | ✅ | ✅ | ✅ | ❌ |
| Claude Code 지원 | ✅ | ✅ | ✅ | ✅ | ❌ |
| OpenAI Compatible | ✅ | ✅ | ✅ | ✅ | 어댑터 필요 |
| 가격 투명성 | ✅ 33개 그룹 | 모델별, 선택 제한 | 단일 가격 | 단일 가격 | - |
| 세금계산서 | ✅ | ❌ 중국 세금계산서 없음 | ✅ | ❌ | - |
| GitHub 오픈소스 | ✅ 자동 가격 업데이트 | ❌ | ❌ | ❌ | - |

---

## ❓ FAQ

**응답이 공식 API와 동일한가요?**

네. Levolink AI는 요청을 공식 모델로 전달하기만 하므로 응답은 공식 API와 일치합니다.

**계정이 정지될 위험이 있나요?**

아니요. 공식 계정 시스템이 아닌 Levolink AI의 키를 사용하므로 공식 계정이 정지될 위험이 없습니다.

**그룹 간 차이는 무엇인가요?**

각 그룹은 서로 다른 백엔드 채널(Azure/AWS/Vertex/공식 직접 연결 등)에 대응하며, 품질과 가격이 다릅니다. 저가 그룹은 가성비가 좋고, 고가 그룹은 최대 안정성을 제공합니다. 기본 그룹으로 시작한 후 필요에 따라 조정하세요.

**streaming을 지원하나요?**

네, 모든 모델이 `stream: true`를 지원하며 지연이 낮습니다.

**중국에서 속도가 어떤가요?**

중국 CDN 노드를 사용하여 지연이 일반적으로 40-200ms입니다. 공식 API에 직접 연결하는 것보다 훨씬 빠릅니다.

**무료 체험이 있나요?**

신규 사용자에게 체험 크레딧이 제공됩니다. 무료로 시작하고 준비되면 충전하세요.

**세금계산서를 발급받을 수 있나요?**

네. 설정 -> 실명 인증 -> 지갑 -> 세금계산서. 영수증은 5영업일 이내 발행됩니다.

**어떤 그룹을 선택해야 하나요?**

- 가성비: 플래시 세일 (0.6x) / Codex 전용 (0.8x)
- 균형: 기본 (1.0x)
- 고품질: Claude Code 전용 (2.4x) / Azure (3.0x)
- 최고 품질: Vertex (6.0x) / 공식 프리미엄 (16.0x)

---

## 📖 심층 가이드

| 가이드 | 내용 |
|--------|------|
| [Claude Code 설정 가이드](docs/ko/claude-code-guide.md) | 중국에서 Claude Code 완전 설정 |
| [Claude Desktop 가이드](docs/ko/claude-desktop-guide.md) | Claude Desktop에 Levolink AI 설정 |
| [Codex 설정 가이드](docs/ko/codex-setup.md) | 중국에서 OpenAI Codex CLI 설정 |
| [Gemini CLI 가이드](docs/ko/gemini-cli-guide.md) | Gemini CLI로 Levolink AI 통해 Gemini 모델 사용 |
| [Cursor IDE 설정](docs/ko/cursor-setup.md) | Cursor에서 GPT-5.6 / Claude 4.8 / Gemini 사용 |
| [Grok Build 가이드](docs/ko/grok-build-guide.md) | xAI Grok Build에 Levolink AI 커스텀 모델 설정 |
| [OpenCode 가이드](docs/ko/opencode-guide.md) | OpenCode 오픈소스 에이전트에 Levolink AI 설정 |
| [OpenClaw 가이드](docs/ko/openclaw-guide.md) | OpenClaw Agent 런타임에 Levolink AI 설정 |
| [CC Switch 가이드](docs/ko/cc-switch-guide.md) | 여러 AI 도구의 Levolink AI 설정 통합 관리 |
| [Dify 연동 가이드](docs/ko/dify-integration.md) | Dify와 Levolink AI 연결 |
| [모델 선택 가이드](docs/ko/model-selection-guide.md) | 228개 모델 중 무엇을 선택할까? 용도 및 예산별 |
| [사기 감지 가이드](docs/ko/fraud-detection-guide.md) | API 프록시에서 모델 치환을 감지하는 5가지 방법 |
| [비용 계산기 가이드](docs/ko/cost-calculator-guide.md) | API 비용 추정 및 지출 최적화 |

---

## 🤝 기여하기

- 🐛 버그 신고 -> [이슈 열기](https://github.com/jiaqing77cn/levolink-ai-api/issues)
- 📝 문서 개선 -> PR 제출
- 💡 기능 제안 -> [디스커션 시작](https://github.com/jiaqing77cn/levolink-ai-api/discussions)
- 📄 기여 가이드 -> [CONTRIBUTING.md](./CONTRIBUTING.md) 참조
- 📋 변경 이력 -> [CHANGELOG.md](./CHANGELOG.md) 참조

---

## 📜 라이선스

MIT License · Copyright (c) 2026 [Levolink AI](https://ai.levolink.com)

## 📢 상표 표시

GPT 및 OpenAI는 OpenAI의 상표입니다. Claude는 Anthropic PBC의 상표입니다. Gemini는 Google LLC의 상표입니다. DeepSeek는 DeepSeek의 상표입니다. 이 리포지토리는 호환성 설명만을 목적으로 하며, 이들 기업과의 공식 제휴나 보증을 의미하지 않습니다.
