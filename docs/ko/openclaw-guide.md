# OpenClaw 연결 튜토리얼

> OpenClaw에서 Levolink AI를 백엔드 모델 제공자로 사용하세요.

## OpenClaw란?

OpenClaw는 오픈소스 AI Agent 런타임으로, 다중 모델 스케줄링, 스킬 시스템, 정기 작업, 메모리 시스템 등을 지원합니다. OpenAI 호환 API 엔드포인트를 설정하여 Levolink AI를 연결할 수 있습니다.

## 설정 단계

### 1. OpenClaw 설치

```bash
# npm으로 설치
npm install -g openclaw

# 또는 Docker 사용
docker run -d openclaw/openclaw
```

### 2. Gateway 설정

OpenClaw의 Gateway 설정 파일 편집 (일반적으로 `~/.openclaw/config.yaml` 또는 프로젝트 디렉토리의 `config.yaml`):

```yaml
# 모델 설정
model:
  # 기본 모델
  default: volces/glm-5.2

  # OpenAI 호환 제공자
  providers:
    - name: levolink
      api_key: "당신의 Levolink API Key"
      base_url: "https://ai.levolink.com/v1"
      models:
        - gpt-5.6-sol
        - gpt-5.6-luna
        - claude-sonnet-4-6
        - claude-opus-4-8
        - gemini-2.5-pro
        - deepseek-reasoner
```

### 3. 또는 환경 변수로 설정

```bash
# ~/.bash_profile 또는 ~/.zshrc에 추가
export OPENAI_API_KEY="당신의 Levolink API Key"
export OPENAI_API_BASE="https://ai.levolink.com/v1"

source ~/.bash_profile
```

### 4. OpenClaw 시작

```bash
openclaw gateway start

# 상태 확인
openclaw status
```

## 추천 모델 설정

| 용도 | 모델 | 그룹 추천 |
|------|------|---------|
| Agent 일상 작업 | `gpt-5.6-luna` | Codex 전용 (0.8x) |
| 복잡한 추론 | `claude-opus-4-8` | 기본 (1.0x) |
| 프로그래밍 작업 | `claude-sonnet-4-6` | 기본 (1.0x) |
| 긴 텍스트 처리 | `gemini-2.5-pro` | gemini-cli (1.0x) |
| 가성비 선택 | `deepseek-reasoner` | 한시적 특가 (0.6x) |

## 세션 모델 전환

OpenClaw는 다양한 세션에 다른 모델을 지정할 수 있습니다:

```bash
# 세션에서 모델 전환
/model claude-opus-4-8

# 현재 모델 확인
/status
```

## 다중 모델 스케줄링

OpenClaw는 여러 모델을 동시에 스케줄링할 수 있어 Agent 병렬 작업에 적합합니다:

```yaml
# 여러 provider를 동시에 사용하도록 설정
model:
  providers:
    - name: levolink-gpt
      api_key: "당신의Key"
      base_url: "https://ai.levolink.com/v1"
    - name: levolink-claude
      api_key: "당신의Key"
      base_url: "https://ai.levolink.com/v1"
```

## 자주 묻는 질문

### Q: OpenClaw에서 "model not available" 오류가 발생합니다

Gateway가 시작되었는지, 모델 이름이 올바른지 확인하세요:

```bash
openclaw status
openclaw models list
```

### Q: 기본 모델을 어떻게 설정하나요?

설정 파일에서 `model.default`를 설정하거나, 세션에서 `/model` 명령을 사용하세요.

### Q: 스트리밍 출력을 지원하나요?

지원합니다. OpenClaw는 기본적으로 스트리밍 출력을 사용합니다.

### Q: 비용을 어떻게 관리하나요?

1. 한시적 특가 그룹(0.6x 배율) 사용
2. 작업에 맞는 적절한 모델 선택
3. 설정에서 token 제한 설정

## 관련 링크

- [Levolink AI 공식 웹사이트](https://ai.levolink.com)
- [OpenClaw 공식 문서](https://docs.openclaw.ai)
- [OpenClaw GitHub](https://github.com/openclaw/openclaw)
- [API 문서](https://levolink.apifox.cn/)
- [모델 선택 가이드](./model-selection-guide.md)
