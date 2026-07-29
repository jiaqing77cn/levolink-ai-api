# Grok Build 連携ガイド

> Grok Build で Levolink AI 経由で GPT/Claude/Gemini などのモデルを呼び出します。

## Grok Build とは

Grok Build は xAI が提供するターミナル AI プログラミングアシスタントで、インタラクティブ TUI、ヘッドレスモード、ACP プロトコルをサポートしています。カスタムモデル設定により、Grok Build から Levolink AI 上の任意のモデルを呼び出すことができます。

## 設定手順

### 1. Grok Build のインストール

**macOS / Linux：**

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
```

**Windows (PowerShell)：**

```powershell
irm https://x.ai/cli/install.ps1 | iex
```

### 2. カスタムモデルの設定

`~/.grok/config.toml` を編集（Windows: `%USERPROFILE%\.grok\config.toml`）：

```toml
# Levolink AI をバックエンドとして使用
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

### 3. API Key の設定

```bash
export LEVOLINK_API_KEY="あなたの Levolink API Key"
```

### 4. 使い方

```bash
cd your-project
grok
```

TUI で `/model` を使用してモデルを切り替え：

```
/model levolink-claude
```

## 推奨モデル設定

| 用途 | モデル | グループ推奨 |
|------|------|---------|
| 日常プログラミング | `gpt-5.6-luna` | Codex 専用 (0.8x) |
| 複雑なプログラミング | `gpt-5.6-sol` | Codex 専用 (0.8x) |
| 高度な推論 | `claude-opus-4-8` | デフォルト (1.0x) |
| 長文 | `gemini-2.5-pro` | gemini-cli (1.0x) |

## ヘッドレスモード

```bash
# Levolink モデルを使用してタスクを実行
grok -p "Explain this codebase" -m levolink-claude

# JSON 出力
grok -p "Analyze architecture" -m levolink-gpt --output-format streaming-json
```

## よくある質問

### Q: Grok Build 起動時に "model not found" と表示される

`grok inspect` を実行して設定が正しく読み込まれているか確認してください：

```bash
grok inspect
```

### Q: Grok モデルと Levolink モデルを同時に使用できますか？

`config.toml` に xAI 公式モデルと Levolink モデルの両方を追加し、`/model` コマンドで切り替えることができます。

### Q: ストリーミング出力に対応していますか

対応しています。Levolink AI のすべてのモデルがストリーミング出力に対応しています。

## 関連リンク

- [Levolink AI 公式サイト](https://ai.levolink.com)
- [Grok Build 公式ドキュメント](https://docs.x.ai/build/overview)
- [Grok Build GitHub](https://github.com/xai-org/grok-build)
- [API ドキュメント](https://levolink.apifox.cn/)
