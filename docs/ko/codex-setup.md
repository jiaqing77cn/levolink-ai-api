# OpenAI Codex 연결 튜토리얼

> 중국에서 OpenAI Codex CLI를 사용하는 최적의 방법, VPN 없이 Levolink AI를 통해 이용.

## Codex CLI란?

OpenAI Codex CLI는 OpenAI에서 출시한 터미널 AI 프로그래밍 어시스턴트로, 코드 생성, 리팩토링, 버그 수정, 테스트 작성 등을 지원합니다. Claude Code와 유사하지만 GPT 모델을 기반으로 합니다.

## 설정 단계

### 1. Codex CLI 설치

```bash
npm install -g @openai/codex
```

### 2. 환경 변수 설정

```bash
# ~/.bash_profile 또는 ~/.zshrc에 추가
export OPENAI_API_KEY="당신의 Levolink API Key"
export OPENAI_API_BASE="https://ai.levolink.com/v1"

# 적용
source ~/.bash_profile
```

### 3. 사용 시작

```bash
cd your-project
codex
```

## 추천 그룹 및 모델

| 용도 | 모델 | 그룹 | 배율 | 입력 가격 |
|------|------|------|------|--------|
| 일상 코딩 | `gpt-5.6-luna` | Codex 전용 | 0.8x | $0.64/M |
| 복잡한 코딩 | `gpt-5.6-sol` | Codex 전용 | 0.8x | $3.20/M |
| 경량 작업 | `gpt-5.4-mini` | 한정 특가 | 0.6x | $0.27/M |
| 코드 자동완성 | `gpt-5-codex` | Codex 전용 | 0.8x | $0.80/M |

## Windows 설정

### PowerShell

```powershell
$env:OPENAI_API_KEY="당신의 Levolink API Key"
$env:OPENAI_API_BASE="https://ai.levolink.com/v1"
codex
```

### 영구 설정

```powershell
[System.Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "당신의Key", "User")
[System.Environment]::SetEnvironmentVariable("OPENAI_API_BASE", "https://ai.levolink.com/v1", "User")
```

## 자주 묻는 질문

### Q: Codex에서 "Invalid API key" 오류가 발생합니다

환경 변수가 올바른지 확인하세요:
```bash
echo $OPENAI_API_KEY
echo $OPENAI_API_BASE
# Base URL 끝에 /v1이 있는지 확인
```

### Q: 응답 속도가 느립니다

Codex 전용 그룹(0.8x)으로 전환하세요. 해당 그룹은 GPT 프로그래밍 모델에 최적화되어 있습니다.

### Q: GPT-5.6 Sol을 지원하나요?

지원합니다. Codex에서 `--model gpt-5.6-sol`로 모델을 지정할 수 있습니다.

### Q: Claude Code와의 차이점은?

| 항목 | Codex CLI | Claude Code |
|------|-----------|-------------|
| 모델 | GPT 시리즈 | Claude 시리즈 |
| 코딩 스타일 | 직관적이고 효율적 | 깊이 있는 추론 |
| 컨텍스트 | 128K | 200K |
| 적합한 상황 | 빠른 프로토타입, 스크립트 | 복잡한 리팩토링, 아키텍처 설계 |

두 도구 모두 Levolink AI를 통해 사용할 수 있으며, 하나의 Key로 전환할 수 있습니다.

## 관련 링크

- [Levolink AI 공식 웹사이트](https://ai.levolink.com)
- [Codex CLI 공식 문서](https://github.com/openai/codex)
- [API 문서](https://levolink.apifox.cn/)
- [모델 선택 가이드](./model-selection-guide.md)
