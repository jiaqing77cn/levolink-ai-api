# Dify セットアップガイド

> Dify を Levolink AI に接続し、1つの Key で 500以上の AI モデルを呼び出す。

## Dify とは

Dify はオープンソースの LLM アプリ開発プラットフォームで、ナレッジベース管理、Agent オーケストレーション、ワークフロー自動化をサポートしています。Levolink AI に接続することで、Dify から GPT-5.6、Claude 4.8、Gemini、DeepSeek などの全モデルを呼び出せるようになります。

## 設定手順

### 1. Levolink API Key を取得

[Levolink AI](https://ai.levolink.com) にアクセス -> 登録 -> コンソール -> Key 作成

### 2. Dify でモデルプロバイダーを設定

Dify -> 設定 -> モデルプロバイダー -> **OpenAI API 互換** を選択：

| 設定項目 | 値 |
|--------|-----|
| API Key | あなたの Levolink API Key |
| API endpoint | `https://ai.levolink.com/v1` |
| モデル名 | `gpt-5.6-sol` / `claude-sonnet-4-6` / `deepseek-reasoner` など |

### 3. 複数モデルを追加

Difyの「モデル」ページで、必要なモデルを順次追加します：

**推奨設定：**

| 用途 | モデル | 推奨グループ |
|------|------|---------|
| チャットアシスタント | `claude-sonnet-4-6` | デフォルト (1.0x) |
| プログラミングアシスタント | `gpt-5.6-sol` | Codex 専用 (0.8x) |
| 長文処理 | `gemini-2.5-pro` | Gemini-CLI 混合 (1.0x) |
| 推論タスク | `deepseek-reasoner` | 限定特価 (0.6x) |
| 日常チャット | `gpt-5.6-luna` | Codex 専用 (0.8x) |

### 4. アプリで使用

アプリ作成時に、「モデル」ドロップダウンから追加済みのモデルを選択するだけです。

## RAG ナレッジベース設定

Dify のナレッジベース機能を Levolink AI と組み合わせて使用：

1. **Embedding モデル**：`text-embedding-3-large` を使用（Levolink 対応）
2. ** rerank モデル**：現在非対応、rerank をオフに可能
3. **対話モデル**：`claude-sonnet-4-6` または `gpt-5.6-sol` を推奨

### ナレッジベースコスト見積もり

| ドキュメント数 | Embedding 費用 | 対話費/回 |
|--------|---------------|----------|
| 100件 | ~$0.02 | ~$0.01 |
| 1000件 | ~$0.20 | ~$0.01 |
| 10000件 | ~$2.00 | ~$0.02 |

## Agent ワークフロー設定

Dify Agent + Levolink AI の典型的なワークフロー：

```
ユーザー入力 -> Claude Sonnet 4.6（意図识别）
            -> DeepSeek R1（推論分析）
            -> GPT-5.6 Sol（回答生成）
```

1つの API Key で全モデルを統括でき、複数アカウントは不要です。

## Docker デプロイの Dify

Docker で Dify をデプロイしている場合、`docker-compose.yml` で環境変数を設定：

```yaml
services:
  api:
    environment:
      - OPENAI_API_KEY=あなたのLevolink Key
      - OPENAI_API_BASE=https://ai.levolink.com/v1
```

## よくある質問

### Q: Dify で "model not found" エラーが出る

モデル名が完全に一致していることを確認してください。Levolink が対応しているモデルリストは [README 価格表](../../README_JA.md#-リアルタイムモデル料金) を参照してください。

### Q: ストリーミング出力が動作しない

Dify のモデル設定で「ストリーミング出力」オプションをオンにしてください。Levolink の全モデルは streaming に対応しています。

### Q: コストを抑える方法

1. 限定特価グループ（0.6x 倍率）を使用
2. 長文には Gemini 2.5 Flash（$0.30/M 入力）を使用
3. 日常チャットには GPT-5.6 Luna（$0.80/M 入力）を使用
4. Dify で token 制限を設定

## 関連リンク

- [Levolink AI 公式サイト](https://ai.levolink.com)
- [Dify 公式ドキュメント](https://docs.dify.ai)
- [API ドキュメント](https://levolink.apifox.cn/)
- [モデル選択ガイド](./model-selection-guide.md)
- [コスト計算ツール](./cost-calculator-guide.md)
