# OpenCode 연결 튜토리얼

> OpenCode에서 Levolink AI를 사용하여 500개 이상의 AI 모델을 호출하세요. VPN이 필요 없습니다.

## OpenCode란?

OpenCode는 오픈소스 AI 프로그래밍 어시스턴트(180K+ Stars)로, 터미널, 데스크톱, IDE 플러그인 세 가지 형태를 지원합니다. OpenAI 호환 API 엔드포인트를 설정하여 Levolink AI를 연결할 수 있습니다.

## 설정 단계

### 1. OpenCode 설치

```bash
# 추천 설치 방법
curl -fsSL https://opencode.ai/install | bash

# 또는 npm을 통해
npm install -g opencode-ai
```

### 2. Levolink AI를 Provider로 설정

프로젝트 루트 디렉토리에 `opencode.json` 생성:

```json
{
  "provider": {
    "levolink": {
      "name": "Levolink AI",
      "api_key": "당신의 Levolink API Key",
      "base_url": "https://ai.levolink.com/v1",
      "models": {
        "gpt-5.6-sol": { "name": "GPT-5.6 Sol" },
        "claude-sonnet-4-6": { "name": "Claude Sonnet 4.6" },
        "gemini-2.5-pro": { "name": "Gemini 2.5 Pro" },
        "deepseek-reasoner": { "name": "DeepSeek R1" }
      }
    }
  },
  "model": "levolink/gpt-5.6-sol"
}
```

### 3. 또는 TUI를 통해 설정

```bash
cd your-project
opencode
```

OpenCode TUI에서 실행:

```
/connect
```

"Custom OpenAI Compatible"을 선택하고 다음을 입력하세요:
- **API Key**: 당신의 Levolink API Key
- **Base URL**: `https://ai.levolink.com/v1`

### 4. 프로젝트 초기화

```
/init
```

OpenCode가 프로젝트 구조를 분석하고 `AGENTS.md` 파일을 생성합니다.

## 추천 모델

| 용도 | 모델 | 그룹 추천 |
|------|------|---------|
| 일상 프로그래밍 | `gpt-5.6-luna` | Codex 전용 (0.8x) |
| 복잡한 프로그래밍 | `claude-sonnet-4-6` | 기본 (1.0x) |
| 심층 추론 | `claude-opus-4-8` | 기본 (1.0x) |
| 긴 텍스트 | `gemini-2.5-pro` | gemini-cli (1.0x) |
| 가성비 | `deepseek-reasoner` | 한시적 특가 (0.6x) |

## 사용 예시

```
# Plan 모드 (Tab 키로 전환)
> src/api/index.ts의 인증 로직을 리팩토링해주세요

# Build 모드
> 계획에 따라 수정을 실행하세요

# 수정 취소
/undo
```

## 자주 묻는 질문

### Q: OpenCode에서 "provider not found" 오류가 발생합니다

`opencode.json`이 프로젝트 루트 디렉토리에 있는지, JSON 형식이 올바른지 확인하세요.

### Q: 모델을 어떻게 전환하나요?

TUI에서 `/model levolink/claude-sonnet-4-6`을 입력하여 모델을 전환하세요.

### Q: Plan 모드를 지원하나요?

지원합니다. `Tab` 키를 눌러 Build와 Plan 모드 간에 전환할 수 있습니다.

### Q: 여러 Provider를 어떻게 설정하나요?

`opencode.json`에 여러 provider를 추가하고 `/model provider/model`로 전환하세요.

## 관련 링크

- [Levolink AI 공식 웹사이트](https://ai.levolink.com)
- [OpenCode 공식 문서](https://opencode.ai/docs/)
- [API 문서](https://levolink.apifox.cn/)
- [모델 선택 가이드](./model-selection-guide.md)
