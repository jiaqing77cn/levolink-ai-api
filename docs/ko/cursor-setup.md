# Cursor IDE 연결 튜토리얼

> Cursor IDE에서 Levolink AI를 사용하여 GPT-5.6 / Claude 4.8 / Gemini 3.5 호출.

## 설정 단계

### 1. Cursor 설정 열기

`Cmd/Ctrl + ,` -> "OpenAI" 검색 -> "OpenAI API Key" 찾기

### 2. 설정 입력

- **API Key**: 당신의 Levolink API Key
- **Base URL**: `https://ai.levolink.com/v1`

### 3. ~/.cursor/settings.json 수정

```json
{
  "openai.apiKey": "당신의 Levolink API Key",
  "openai.baseUrl": "https://ai.levolink.com/v1",
  "openai.model": "gpt-5.6-sol"
}
```

### 4. Claude 모델 사용

Cursor의 모델 선택에서 커스텀 모델 이름을 입력하세요:
- `claude-sonnet-4-6` - 일상 코딩
- `claude-opus-4-8` - 복잡한 작업
- `gpt-5.6-sol` - GPT 프로그래밍

## 추천 설정

| 용도 | 모델 | 그룹 |
|------|------|------|
| 코드 자동완성 | gpt-5.6-luna | Codex 전용 (0.8x) |
| 대화 | claude-sonnet-4-6 | 기본 (1.0x) |
| 복잡한 리팩토링 | claude-opus-4-8 | CC 전용 (2.4x) |
