# Cursor IDE セットアップガイド

> Cursor IDE で Levolink AI を使って GPT-5.6 / Claude 4.8 / Gemini 3.5 を呼び出す。

## 設定手順

### 1. Cursor 設定を開く

`Cmd/Ctrl + ,` -> 「OpenAI」を検索 -> 「OpenAI API Key」を見つける

### 2. 設定を入力

- **API Key**: あなたの Levolink API Key
- **Base URL**: `https://ai.levolink.com/v1`

### 3. ~/.cursor/settings.json を編集

```json
{
  "openai.apiKey": "あなたの Levolink API Key",
  "openai.baseUrl": "https://ai.levolink.com/v1",
  "openai.model": "gpt-5.6-sol"
}
```

### 4. Claude モデルを使用

Cursor のモデル選択でカスタムモデル名を入力：
- `claude-sonnet-4-6` - 日常プログラミング
- `claude-opus-4-8` - 複雑なタスク
- `gpt-5.6-sol` - GPT プログラミング

## 推奨設定

| 用途 | モデル | グループ |
|------|------|------|
| コード補完 | gpt-5.6-luna | Codex 専用 (0.8x) |
| チャット | claude-sonnet-4-6 | デフォルト (1.0x) |
| 複雑なリファクタリング | claude-opus-4-8 | CC 専用 (2.4x) |
