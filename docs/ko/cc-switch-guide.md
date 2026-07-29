# CC Switch 연결 튜토리얼

> CC Switch를 사용하여 Claude Code, Codex, Gemini CLI, OpenCode, OpenClaw 등 도구의 Levolink AI 설정을 통합 관리하세요.

## CC Switch란?

CC Switch는 크로스 플랫폼 데스크톱 도구로, 여러 AI 프로그래밍 도구의 API 설정을 통합 관리합니다. Claude Code, Claude Desktop, Codex, Gemini CLI, Grok Build, OpenCode, OpenClaw, Hermes를 지원하며, 원클릭으로 API Provider를 전환할 수 있어 수동으로 설정 파일을 편집할 필요가 없습니다.

## 설치

### macOS

```bash
# Homebrew
brew install --cask cc-switch
```

### Windows

[ccswitch.io](https://ccswitch.io)에서 설치 패키지를 다운로드하세요.

### Linux

[GitHub Releases](https://github.com/farion1231/cc-switch/releases)에서 AppImage를 다운로드하세요.

## Levolink AI 설정

### 1. Provider 추가

CC Switch 열기 -> 「Provider 추가」 클릭 -> 「커스텀」 선택:

| 설정 항목 | 값 |
|--------|-----|
| 이름 | Levolink AI |
| API Key | 당신의 Levolink API Key |
| Base URL | `https://ai.levolink.com/v1` |
| 형식 | OpenAI Compatible |

### 2. 각 도구 설정

CC Switch가 각 도구의 설정을 자동으로 생성합니다:

**Claude Code:**
```bash
export ANTHROPIC_AUTH_TOKEN="당신의Key"
export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"
```

**Codex:**
```bash
export OPENAI_API_KEY="당신의Key"
export OPENAI_API_BASE="https://ai.levolink.com/v1"
```

**Gemini CLI:**
```bash
export GEMINI_API_KEY="당신의Key"
export GEMINI_API_BASE="https://ai.levolink.com/v1"
```

**OpenCode:**
```json
{
  "provider": {
    "levolink": {
      "api_key": "당신의Key",
      "base_url": "https://ai.levolink.com/v1"
    }
  }
}
```

### 3. 원클릭 전환

CC Switch 인터페이스에서 대상 도구 선택 -> 「Levolink AI」 선택 -> 「적용」 클릭. CC Switch가 해당 도구의 설정 파일을 자동으로 수정합니다.

## 추천 설정

| 도구 | 추천 모델 | 그룹 |
|------|---------|------|
| Claude Code | `claude-sonnet-4-6` | 기본 (1.0x) |
| Codex | `gpt-5.6-sol` | Codex 전용 (0.8x) |
| Gemini CLI | `gemini-2.5-pro` | gemini-cli (1.0x) |
| OpenCode | `gpt-5.6-luna` | Codex 전용 (0.8x) |
| OpenClaw | `claude-opus-4-8` | 기본 (1.0x) |

## 다중 Provider 관리

CC Switch는 여러 Provider를 동시에 설정할 수 있어 비교 테스트에 편리합니다:

1. 「Levolink AI - 한시적 특가」 추가 (0.6x)
2. 「Levolink AI - 기본」 추가 (1.0x)
3. 「Levolink AI - CC 전용」 추가 (2.4x)

인터페이스에서 원클릭으로 전환할 수 있으며, 코드나 환경 변수를 수정할 필요가 없습니다.

## 자주 묻는 질문

### Q: CC Switch에서 설정을 수정한 후 도구에 적용되지 않습니다

대상 도구를 완전히 종료하고 다시 시작했는지 확인하세요. Claude Code는 환경 변수를 다시 source해야 합니다.

### Q: 다른 도구에 다른 Provider를 설정할 수 있나요?

가능합니다. CC Switch는 각 도구마다 독립적으로 Provider와 모델을 설정할 수 있습니다.

### Q: CC Switch는 무료인가요?

CC Switch는 오픈소스 도구로 무료로 사용할 수 있습니다.

## 관련 링크

- [Levolink AI 공식 웹사이트](https://ai.levolink.com)
- [CC Switch 공식 웹사이트](https://ccswitch.io)
- [CC Switch GitHub](https://github.com/farion1231/cc-switch)
- [API 문서](https://levolink.apifox.cn/)
