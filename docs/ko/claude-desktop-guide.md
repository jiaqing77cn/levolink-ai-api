# Claude Desktop 연결 튜토리얼

> Claude Desktop 데스크톱 앱에서 Levolink AI를 사용하여 VPN 없이 Claude 모델을 호출하세요.

## Claude Desktop이란?

Claude Desktop은 Anthropic에서 공식 출시한 데스크톱 클라이언트로, macOS와 Windows를 지원합니다. 환경 변수를 설정하면 Claude Desktop이 Levolink AI를 통해 Claude 모델에 접근할 수 있습니다.

## 설정 단계

### 1. 환경 변수 설정

**macOS:**

```bash
# ~/.zshrc 또는 ~/.bash_profile에 추가
export ANTHROPIC_API_KEY="당신의 Levolink API Key"
export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"

# 적용
source ~/.zshrc
```

**Windows:**

```powershell
# PowerShell 영구 설정
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "당신의Key", "User")
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_BASE_URL", "https://ai.levolink.com/v1", "User")
```

### 2. Claude Desktop 재시작

Claude Desktop을 완전히 종료한 후(최소화가 아님) 다시 시작하세요. 앱이 새 환경 변수를 읽어옵니다.

### 3. 연결 확인

Claude Desktop에서 메시지를 보내서 정상적으로 응답을 받으면 Levolink AI를 통한 중계가 성공적으로 설정된 것입니다.

## MCP Server 설정

Claude Desktop은 MCP(Model Context Protocol)를 지원하여 더 많은 도구를 연결할 수 있습니다:

설정 파일 편집:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "levolink": {
      "command": "curl",
      "args": ["https://ai.levolink.com/v1/chat/completions"]
    }
  }
}
```

## 추천 모델

| 용도 | 모델 | 그룹 추천 |
|------|------|---------|
| 일상 대화 | `claude-sonnet-4-6` | 기본 (1.0x) |
| 복잡한 작업 | `claude-opus-4-8` | 기본 (1.0x) |
| 경량 작업 | `claude-haiku-4-5` | 기본 (1.0x) |

## 자주 묻는 질문

### Q: Claude Desktop 시작 후 환경 변수를 읽지 못합니다?

앱을 완전히 종료했는지 확인하세요(트레이 아이콘 우클릭 -> Quit), 그리고 터미널에서 시작하세요:

```bash
open -a "Claude"
```

### Q: "connection error"가 표시됩니다?

API Key가 올바른지, Base URL이 `/v1`로 끝나는지 확인하세요.

### Q: Claude Opus 4.8을 지원하나요?

지원합니다. 대화 중 `/model claude-opus-4-8`을 입력하여 모델을 전환하세요.

## 관련 링크

- [Levolink AI 공식 웹사이트](https://ai.levolink.com)
- [Claude Desktop 공식 다운로드](https://claude.ai/download)
- [API 문서](https://levolink.apifox.cn/)
