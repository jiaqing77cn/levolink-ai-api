# OpenCode 連携ガイド

> OpenCode で Levolink AI を使用し、500 以上の AI モデルを呼び出します。VPN は不要です。

## OpenCode とは

OpenCode はオープンソースの AI プログラミングアシスタント（160K+ Stars）で、ターミナル、デスクトップ、IDE プラグインの3つの形式をサポートしています。OpenAI 互換の API エンドポイントを設定することで、Levolink AI を連携できます。

## 設定手順

### 1. OpenCode のインストール

```bash
# 推奨インストール方法
curl -fsSL https://opencode.ai/install | bash

> ⚠️ インストール前にスクリプト内容を確認することを推奨

# または npm 経由
npm install -g opencode-ai
```

### 2. Levolink AI を Provider として設定

プロジェクトルートに `opencode.json` を作成：

```json
{
  "provider": {
    "levolink": {
      "name": "Levolink AI",
      "api_key": "あなたの Levolink API Key",
      "base_url": "https://ai.levolink.com/v1",
      "models": {
        "gpt-5.6-sol": { "name": "GPT-5.6 Sol" },
        "claude-sonnet-4-6": { "name": "Claude Sonnet 4.6" },
        "gemini-2.5-pro": { "name": "Gemini 2.5 Pro" },
        "deepseek-reasoner": { "name": "DeepSeek R1" }
      }
    }
  },
  "model": "levolink/gpt-5.6-sol"
}
```

### 3. または TUI から設定

```bash
cd your-project
opencode
```

OpenCode TUI で以下を実行：

```
/connect
```

「Custom OpenAI Compatible」を選択し、以下を入力：
- **API Key**: あなたの Levolink API Key
- **Base URL**: `https://ai.levolink.com/v1`

### 4. プロジェクトの初期化

```
/init
```

OpenCode がプロジェクト構造を分析し、`AGENTS.md` ファイルを生成します。

## 推奨モデル

| 用途 | モデル | グループ推奨 |
|------|------|---------|
| 日常プログラミング | `gpt-5.6-luna` | Codex 専用 (0.8x) |
| 複雑なプログラミング | `claude-sonnet-4-6` | デフォルト (1.0x) |
| 高度な推論 | `claude-opus-4-8` | デフォルト (1.0x) |
| 長文 | `gemini-2.5-pro` | gemini-cli (1.0x) |
| コストパフォーマンス | `deepseek-reasoner` | 期間限定特価 (0.6x) |

## 使用例

```
# Plan モード（Tab キーで切り替え）
> src/api/index.ts の認証ロジックをリファクタリング

# Build モード
> 計画に従って変更を実行

# 変更を取り消す
/undo
```

## よくある質問

### Q: OpenCode で "provider not found" エラーが出る

`opencode.json` がプロジェクトルートにあるか、JSON フォーマットが正しいか確認してください。

### Q: モデルを切り替える方法

TUI で `/model levolink/claude-sonnet-4-6` と入力してモデルを切り替えてください。

### Q: Plan モードに対応していますか

対応しています。`Tab` キーで Build と Plan モードを切り替えられます。

### Q: 複数の Provider を設定する方法

`opencode.json` に複数の provider を追加し、`/model provider/model` で切り替えてください。

## 関連リンク

- [Levolink AI 公式サイト](https://ai.levolink.com)
- [OpenCode 公式ドキュメント](https://opencode.ai/docs/)
- [API ドキュメント](https://levolink.apifox.cn/)
- [モデル選択ガイド](./model-selection-guide.md)
