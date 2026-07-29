# Grok Build 연결 튜토리얼

> Grok Build에서 Levolink AI를 중계로 사용하여 GPT/Claude/Gemini 등의 모델을 호출하세요.

## Grok Build란?

Grok Build는 xAI에서 출시한 터미널 AI 프로그래밍 어시스턴트로, 대화형 TUI, 헤드리스 모드 및 ACP 프로토콜을 지원합니다. 커스텀 모델 설정을 통해 Grok Build에서 Levolink AI의 모든 모델을 호출할 수 있습니다.

## 설정 단계

### 1. Grok Build 설치

**macOS / Linux:**

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
```

**Windows (PowerShell):**

```powershell
irm https://x.ai/cli/install.ps1 | iex
```

### 2. 커스텀 모델 설정

`~/.grok/config.toml` 편집 (Windows: `%USERPROFILE%\.grok\config.toml`):

```toml
# Levolink AI를 백엔드로 사용
[model.levolink-gpt]
model = "gpt-5.6-sol"
base_url = "https://ai.levolink.com/v1"
name = "GPT-5.6 Sol (Levolink)"
env_key = "LEVOLINK_API_KEY"

[model.levolink-claude]
model = "claude-sonnet-4-6"
base_url = "https://ai.levolink.com/v1"
name = "Claude Sonnet 4.6 (Levolink)"
env_key = "LEVOLINK_API_KEY"

[model.levolink-gemini]
model = "gemini-2.5-pro"
base_url = "https://ai.levolink.com/v1"
name = "Gemini 2.5 Pro (Levolink)"
env_key = "LEVOLINK_API_KEY"

[models]
default = "levolink-gpt"
```

### 3. API Key 설정

```bash
export LEVOLINK_API_KEY="당신의 Levolink API Key"
```

### 4. 사용 시작

```bash
cd your-project
grok
```

TUI에서 `/model`을 사용하여 모델 전환:

```
/model levolink-claude
```

## 추천 모델 설정

| 용도 | 모델 | 그룹 추천 |
|------|------|---------|
| 일상 프로그래밍 | `gpt-5.6-luna` | Codex 전용 (0.8x) |
| 복잡한 프로그래밍 | `gpt-5.6-sol` | Codex 전용 (0.8x) |
| 심층 추론 | `claude-opus-4-8` | 기본 (1.0x) |
| 긴 텍스트 | `gemini-2.5-pro` | gemini-cli (1.0x) |

## 헤드리스 모드

```bash
# Levolink 모델을 사용하여 작업 실행
grok -p "Explain this codebase" -m levolink-claude

# JSON 출력
grok -p "Analyze architecture" -m levolink-gpt --output-format streaming-json
```

## 자주 묻는 질문

### Q: Grok Build 시작 시 "model not found"가 표시됩니다

`grok inspect`를 실행하여 설정이 올바르게 로드되었는지 확인하세요:

```bash
grok inspect
```

### Q: Grok 모델과 Levolink 모델을 동시에 사용할 수 있나요?

`config.toml`에 xAI 공식 모델과 Levolink 모델을 모두 추가하고 `/model` 명령으로 전환하세요.

### Q: 스트리밍 출력을 지원하나요?

지원합니다. Levolink AI의 모든 모델은 스트리밍 출력을 지원합니다.

## 관련 링크

- [Levolink AI 공식 웹사이트](https://ai.levolink.com)
- [Grok Build 공식 문서](https://docs.x.ai/build/overview)
- [Grok Build GitHub](https://github.com/xai-org/grok-build)
- [API 문서](https://levolink.apifox.cn/)
