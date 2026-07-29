# Claude Desktop 連携ガイド

> Claude Desktop デスクトップアプリで Levolink AI を使用し、VPN なしで Claude モデルを直接呼び出します。

## Claude Desktop とは

Claude Desktop は Anthropic が公式提供するデスクトップクライアントで、macOS と Windows に対応しています。環境変数を設定することで、Claude Desktop が Levolink AI を経由して Claude モデルにアクセスするようにできます。

## 設定手順

### 1. 環境変数の設定

**macOS：**

```bash
# ~/.zshrc または ~/.bash_profile に追加
export ANTHROPIC_API_KEY="あなたの Levolink API Key"
export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"

# 反映
source ~/.zshrc
```

**Windows：**

```powershell
# PowerShell で永続的に設定
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "あなたのKey", "User")
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_BASE_URL", "https://ai.levolink.com/v1", "User")
```

### 2. Claude Desktop の再起動

Claude Desktop を完全に終了（最小化ではなく）してから、再起動してください。アプリが新しい環境変数を読み込みます。

### 3. 接続確認

Claude Desktop でメッセージを送信し、正常に返信が受信できれば、Levolink AI 経由の接続は成功です。

## MCP Server 設定

Claude Desktop は MCP（Model Context Protocol）に対応しており、追加ツールを連携できます：

設定ファイルを編集：
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

## 推奨モデル

| 用途 | モデル | グループ推奨 |
|------|------|---------|
| 日常会話 | `claude-sonnet-4-6` | デフォルト (1.0x) |
| 複雑なタスク | `claude-opus-4-8` | デフォルト (1.0x) |
| 軽量タスク | `claude-haiku-4-5` | デフォルト (1.0x) |

## よくある質問

### Q: Claude Desktop 起動後に環境変数が読み込まれない？

アプリを完全に終了（トレイアイコンを右クリック -> Quit）してから、ターミナルから起動してください：

```bash
open -a "Claude"
```

### Q: "connection error" と表示される？

API Key が正しいか、Base URL が `/v1` で終わっているかを確認してください。

### Q: Claude Opus 4.8 に対応していますか？

対応しています。会話中に `/model claude-opus-4-8` を入力してモデルを切り替えてください。

## 関連リンク

- [Levolink AI 公式サイト](https://ai.levolink.com)
- [Claude Desktop 公式ダウンロード](https://claude.ai/download)
- [API ドキュメント](https://levolink.apifox.cn/)
