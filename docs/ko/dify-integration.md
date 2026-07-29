# Dify 연결 튜토리얼

> Dify를 Levolink AI에 연결하여 하나의 Key로 500+ AI 모델을 호출.

## Dify란?

Dify는 오픈소스 LLM 애플리케이션 개발 플랫폼으로, 지식베이스 관리, Agent 오케스트레이션, 워크플로우 자동화를 지원합니다. Levolink AI와 연결하면 Dify에서 GPT-5.6, Claude 4.8, Gemini, DeepSeek 등 모든 모델을 호출할 수 있습니다.

## 설정 단계

### 1. Levolink API Key 받기

[Levolink AI](https://ai.levolink.com)로 이동 -> 회원가입 -> 콘솔 -> Key 생성

### 2. Dify에서 모델 공급자 설정

Dify -> 설정 -> 모델 공급자 -> **OpenAI API 호환** 선택:

| 설정 항목 | 값 |
|--------|-----|
| API Key | 당신의 Levolink API Key |
| API endpoint | `https://ai.levolink.com/v1` |
| 모델 이름 | `gpt-5.6-sol` / `claude-sonnet-4-6` / `deepseek-reasoner` 등 |

### 3. 여러 모델 추가

Dify의「모델」페이지에서 필요한 모델을 순서대로 추가하세요:

**추천 설정:**

| 용도 | 모델 | 그룹 추천 |
|------|------|---------|
| 대화 어시스턴트 | `claude-sonnet-4-6` | 기본 (1.0x) |
| 프로그래밍 어시스턴트 | `gpt-5.6-sol` | Codex 전용 (0.8x) |
| 긴 텍스트 처리 | `gemini-2.5-pro` | Gemini-CLI 혼합 (1.0x) |
| 추론 작업 | `deepseek-reasoner` | 한정 특가 (0.6x) |
| 일상 대화 | `gpt-5.6-luna` | Codex 전용 (0.8x) |

### 4. 애플리케이션에서 사용

앱을 생성할 때,「모델」드롭다운에서 추가한 모델을 선택하면 됩니다.

## RAG 지식베이스 설정

Dify의 지식베이스 기능을 Levolink AI와 함께 사용:

1. **Embedding 모델**: `text-embedding-3-large` 사용 (Levolink 지원)
2. **Rerank 모델**: 현재 미지원, rerank 비활성화 가능
3. **대화 모델**: `claude-sonnet-4-6` 또는 `gpt-5.6-sol` 추천

### 지식베이스 비용 추정

| 문서 수 | Embedding 비용 | 대화당 비용 |
|--------|---------------|----------|
| 100편 | ~$0.02 | ~$0.01 |
| 1000편 | ~$0.20 | ~$0.01 |
| 10000편 | ~$2.00 | ~$0.02 |

## Agent 워크플로우 설정

Dify Agent + Levolink AI의 일반적인 워크플로우:

```
사용자 입력 -> Claude Sonnet 4.6 (의도 인식)
             -> DeepSeek R1 (추론 분석)
             -> GPT-5.6 Sol (응답 생성)
```

하나의 API Key로 모든 모델을调度할 수 있어, 여러 계정이 필요 없습니다.

## Docker로 배포한 Dify

Docker로 Dify를 배포한 경우, `docker-compose.yml`에서 환경 변수를 설정하세요:

```yaml
services:
  api:
    environment:
      - OPENAI_API_KEY=당신의Levolink Key
      - OPENAI_API_BASE=https://ai.levolink.com/v1
```

## 자주 묻는 질문

### Q: Dify에서 "model not found" 오류가 발생합니다

모델 이름이 정확히 일치하는지 확인하세요. Levolink가 지원하는 모델 목록은 [README 가격표](../../README_KO.md#-실시간-모델-가격)를 참조하세요.

### Q: 스트리밍 출력이 작동하지 않습니다

Dify 모델 설정에서「스트리밍 출력」옵션을 활성화하세요. Levolink의 모든 모델은 streaming을 지원합니다.

### Q: 비용을 어떻게 관리하나요?

1. 한정 특가 그룹(0.6x 배율) 사용
2. 긴 텍스트는 Gemini 2.5 Flash($0.30/M 입력) 사용
3. 일상 대화는 GPT-5.6 Luna($0.80/M 입력) 사용
4. Dify에서 token 제한 설정

## 관련 링크

- [Levolink AI 공식 웹사이트](https://ai.levolink.com)
- [Dify 공식 문서](https://docs.dify.ai)
- [API 문서](https://levolink.apifox.cn/)
- [모델 선택 가이드](./model-selection-guide.md)
- [비용 계산기](./cost-calculator-guide.md)
