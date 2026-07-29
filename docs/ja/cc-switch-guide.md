# CC Switch 連携ガイド

> CC Switch を使用して、Claude Code、Codex、Gemini CLI、OpenCode、OpenClaw などのツールの Levolink AI 設定を一元管理します。

## CC Switch とは

CC Switch はクロスプラットフォームのデスクトップツールで、複数の AI プログラミングツールの API 設定を一元管理できます。Claude Code、Claude Desktop、Codex、Gemini CLI、Grok Build、OpenCode、OpenClaw、Hermes に対応し、API Provider をワンクリックで切り替えでき、設定ファイルを手動で編集する必要はありません。

## インストール

### macOS

```bash
# Homebrew
brew install --cask cc-switch
```

### Windows

[ccswitch.io](https://ccswitch.io) からインストーラーをダウンロード。

### Linux

[GitHub Releases](https://github.com/farion1231/cc-switch/releases) から AppImage をダウンロード。

## Levolink AI の設定

### 1. Provider の追加

CC Switch を開く ->「Provider を追加」をクリック ->「カスタム」を選択：

| 設定項目 | 値 |
|--------|-----|
| 名称 | Levolink AI |
| API Key | あなたの Levolink API Key |
| Base URL | `https://ai.levolink.com/v1` |
| フォーマット | OpenAI Compatible |

### 2. 各ツールの設定

CC Switch が各ツールの設定を自動生成します：

**Claude Code：**
```bash
export ANTHROPIC_AUTH_TOKEN="あなたのKey"
export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"
```

**Codex：**
```bash
export OPENAI_API_KEY="あなたのKey"
export OPENAI_API_BASE="https://ai.levolink.com/v1"
```

**Gemini CLI：**
```bash
export GEMINI_API_KEY="あなたのKey"
export GEMINI_API_BASE="https://ai.levolink.com/v1"
```

**OpenCode：**
```json
{
  "provider": {
    "levolink": {
      "api_key": "あなたのKey",
      "base_url": "https://ai.levolink.com/v1"
    }
  }
}
```

### 3. ワンクリック切り替え

CC Switch のインターフェースで対象ツールを選択 ->「Levolink AI」を選択 ->「適用」をクリック。CC Switch が対応ツールの設定ファイルを自動的に更新します。

## 推奨設定

| ツール | 推奨モデル | グループ |
|------|---------|------|
| Claude Code | `claude-sonnet-4-6` | デフォルト (1.0x) |
| Codex | `gpt-5.6-sol` | Codex 専用 (0.8x) |
| Gemini CLI | `gemini-2.5-pro` | gemini-cli (1.0x) |
| OpenCode | `gpt-5.6-luna` | Codex 専用 (0.8x) |
| OpenClaw | `claude-opus-4-8` | デフォルト (1.0x) |

## 複数 Provider の管理

CC Switch は複数の Provider を同時に設定でき、比較テストに便利です：

1.「Levolink AI - 期間限定特価」を追加 (0.6x)
2.「Levolink AI - デフォルト」を追加 (1.0x)
3.「Levolink AI - CC 専用」を追加 (2.4x)

インターフェースでワンクリック切り替えでき、コードや環境変数を変更する必要はありません。

## よくある質問

### Q: CC Switch で設定変更後、ツールに反映されない

対象ツールを完全に終了してから再起動してください。Claude Code の場合は環境変数を再 source する必要があります。

### Q: 異なるツールに異なる Provider を設定できますか

できます。CC Switch はツールごとに独立して Provider とモデルを設定できます。

### Q: CC Switch は無料ですか

CC Switch はオープンソースツールで、無料で利用できます。

## 関連リンク

- [Levolink AI 公式サイト](https://ai.levolink.com)
- [CC Switch 公式サイト](https://ccswitch.io)
- [CC Switch GitHub](https://github.com/farion1231/cc-switch)
- [API ドキュメント](https://levolink.apifox.cn/)
