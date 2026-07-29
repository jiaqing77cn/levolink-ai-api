# Gemini CLI 연결 튜토리얼

> Gemini CLI에서 Levolink AI를 사용하여 Gemini 3.5 Pro / Flash 등의 모델을 호출하세요. VPN이 필요 없습니다.

## Gemini CLI란?

Gemini CLI는 Google에서 출시한 터미널 AI 어시스턴트로, 코드 생성, 문서 분석, 작업 자동화 등을 지원합니다. Levolink AI를 통해 중계하면 한국 사용자도 Gemini 시리즈 모델을 직접 사용할 수 있습니다.

## 설정 단계

### 1. Gemini CLI 설치

```bash
npm install -g @google/gemini-cli
```

### 2. 환경 변수 설정

```bash
# ~/.bash_profile 또는 ~/.zshrc에 추가
export GEMINI_API_KEY="당신의 Levolink API Key"
export GEMINI_API_BASE="https://ai.levolink.com/v1"

# 적용
source ~/.bash_profile
```

### 3. 사용 시작

```bash
cd your-project
gemini
```

## 추천 모델 및 그룹

| 용도 | 모델 | 그룹 | 배율 |
|------|------|------|------|
| 일상 사용 | `gemini-2.5-flash` | gemini-cli | 1.0x |
| 경량 작업 | `gemini-2.5-flash-lite` | gemini-cli | 1.0x |
| 복잡한 작업 | `gemini-2.5-pro` | gemini-cli | 1.0x |
| 이미지 생성 | `gemini-3-pro-image` | 프리미엄 Gemini | 2.4x |

## 모델 지정

```bash
# 특정 모델 사용
gemini --model gemini-2.5-pro

# 또는 대화형 모드에서 전환
> /model gemini-2.5-flash
```

## Windows 설정

```powershell
$env:GEMINI_API_KEY="당신의 Levolink API Key"
$env:GEMINI_API_BASE="https://ai.levolink.com/v1"
gemini
```

영구 설정:

```powershell
[System.Environment]::SetEnvironmentVariable("GEMINI_API_KEY", "당신의Key", "User")
[System.Environment]::SetEnvironmentVariable("GEMINI_API_BASE", "https://ai.levolink.com/v1", "User")
```

## 자주 묻는 질문

### Q: Gemini CLI에서 "Invalid API key" 오류가 발생합니다

환경 변수가 올바르게 설정되었는지 확인하세요:

```bash
echo $GEMINI_API_KEY
echo $GEMINI_API_BASE
# Base URL 끝에 /v1이 있는지 확인
```

### Q: 응답 속도가 느립니다

Gemini-CLI 그룹(1.0x 배율)은 Gemini 모델에 최적화되어 있어 속도가 빠릅니다.

### Q: Gemini 3.5 Pro를 지원하나요?

지원합니다. `--model gemini-3-pro-image`를 사용하거나 대화형 모드에서 전환하세요.

## 관련 링크

- [Levolink AI 공식 웹사이트](https://ai.levolink.com)
- [Gemini CLI 공식 문서](https://github.com/google-gemini/gemini-cli)
- [API 문서](https://levolink.apifox.cn/)
- [모델 선택 가이드](./model-selection-guide.md)
