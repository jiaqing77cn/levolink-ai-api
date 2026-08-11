<h1 align="center">🚀 中国AI APIプロキシ | VPN不要でClaude/GPT/Gemini/DeepSeekに直接接続 | Levolink AI</h1>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License"/>
  <img src="https://img.shields.io/badge/500%2B-Models-34d399?style=flat" alt="Models"/>
  <img src="https://img.shields.io/badge/CDN-China%20Accel-3b82f6?style=flat" alt="CDN"/>
  <img src="https://img.shields.io/badge/OpenAI-Compatible-10a37f?style=flat" alt="OpenAI Compatible"/>
</p>

<div align="center">

**VPN不要 · 低レイテンシ · 500以上のモデル · OpenAI Compatible · Claude Code対応**

[🌐 公式サイト](https://ai.levolink.com) · [📋 料金](https://ai.levolink.com/pricing) · [📖 APIドキュメント](https://levolink.apifox.cn/) · [💬 お問い合わせ](https://ai.levolink.com)

</div>

> Last updated: 2026-08-11 10:08 (UTC+8)| [中文](./README.md) | [English](./README_EN.md) | [한국어](./README_KO.md) | 日本語 | [Español](./README_ES.md) | [Deutsch](./README_DE.md)

---

## 📋 目次

- [🖥️ プロダクトプレビュー](#-プロダクトプレビュー)
- [🔍 APIプロキシの選び方](#-apiプロキシの選び方)
- [💰 リアルタイムモデル料金](#-リアルタイムモデル料金)
- [🛠️ 統合ガイド](#-統合ガイド)
- [📊 比較](#-比較)
- [❓ FAQ](#-faq)
- [📖 詳細ガイド](#-詳細ガイド)
- [🤝 コントリビュート](#-コントリビュート)

---

## 🖥️ プロダクトプレビュー

![Levolink AI ホームページ - 500以上のAIモデルAPIプロキシダッシュボード](https://raw.githubusercontent.com/jiaqing77cn/levolink-ai-api/main/assets/homepage.jpg)

![Levolink AI コンソール - APIキー作成、使用量確認、アカウントチャージ](https://raw.githubusercontent.com/jiaqing77cn/levolink-ai-api/main/assets/console.jpg)

---

## 🔍 APIプロキシの選び方

AI APIプロキシを選ぶ際に評価すべき6つの評価軸：

| 評価軸 | 確認ポイント | 危険信号 |
|-----------|--------------|-----------|
| **安定性** | 頻繁にダウンする？レイテンシが高い？ | 切断、告知なし |
| **速度** | レスポンスレイテンシは許容範囲？ | 初回トークンまで5秒以上 |
| **モデルカバレッジ** | 最新モデルが利用可能？ | 新モデル追加が遅い |
| **価格透明性** | 課金が明確？使用ログあり？ | 呼出記録なし、不透明 |
| **モデルすり替え** | 安価なモデルを高級モデルとして偽装？ | 異常に安い、品質が低い |
| **退出リスク** | 企業運営？サポートあり？ | 個人運営、カスタマーサポートなし |

### ⚠️ 落とし穴チェックリスト

1. **キャッシュ価格の罠**：通常のキャッシュ価格は10%、一部は15%-30%を請求する
2. **モデルすり替え検出**：同じプロンプトで公式とプロキシの出力を比較する
3. **トークン数不正**：既知のトークン数でリクエストを送信し、課金が水増しされていないか確認する
4. **低価格の罠**：市場価格を大幅に下回る価格は、GLMがGPTを偽装している可能性が高い
5. **退出詐欺リスク**：大額入金しないこと！従量課金で利用する

### 🔬 モデルすり替えの検出方法

```python
# 方法1：能力テスト - 推論プロンプトを使用
prompt = "A farmer has 17 sheep. All but 9 die. How many are left?"
# GPT/Claudeの正解：9
# 低品質モデルは多くの場合間違える：8

# 方法2：長文コンテキストテスト
# 50K+トークンの長文を送信し、末尾の詳細について質問する
# 低品質モデルはコンテキストを見失う

# 方法3：コード能力テスト
prompt = "Implement an LRU cache with TTL expiration in Python"
# 公式とプロキシのコード品質を比較する
```

---

## 💰 リアルタイムモデル料金

> 価格はGitHub Actionsにより[Levolink API](https://ai.levolink.com/api/pricing)から自動取得され、毎時更新されます。
>
> 単位：USD / Million Tokens | 出力/入力比 = 出力価格 ÷ 入力価格

### OpenAI GPTシリーズ

<!-- GPT_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `gpt-5-codex` | Enterprise Azure 2 | 0.35x | $0.44 | $3.50 | Codex Exclusive | 0.8x | $1.00 | $8.00 | 8x |
| `gpt-5-mini` | Enterprise Azure 2 | 0.35x | $0.09 | $0.70 | Special-Premium GPT | 5.6x | $1.40 | $11.20 | 8x |
| `gpt-5-mini-2025-08-07` | Enterprise Azure 2 | 0.35x | $0.09 | $0.70 | Special-Premium GPT | 5.6x | $1.40 | $11.20 | 8x |
| `gpt-5-nano` | Enterprise Azure 2 | 0.35x | $0.02 | $0.14 | Special-Premium GPT | 5.6x | $0.28 | $2.24 | 8x |
| `gpt-5-nano-2025-08-07` | Enterprise Azure 2 | 0.35x | $0.02 | $0.14 | Special-Premium GPT | 5.6x | $0.28 | $2.24 | 8x |
| `gpt-5-pro` | Enterprise Azure 2 | 0.35x | $5.25 | $42.00 | Special-Premium GPT | 5.6x | $84.00 | $672.00 | 8x |
| `gpt-5.1-codex` | Sale 10% Off | 0.54x | $0.68 | $5.40 | Codex Exclusive | 0.8x | $1.00 | $8.00 | 8x |
| `gpt-5.1-codex-max` | Sale 10% Off | 0.54x | $0.68 | $5.40 | Pure Azure | 1.5x | $1.88 | $15.00 | 8x |
| `gpt-5.1-codex-mini` | Sale 10% Off | 0.54x | $0.14 | $1.08 | Pure Azure | 1.5x | $0.38 | $3.00 | 8x |
| `gpt-5.2-chat` | Enterprise Azure 2 | 0.35x | $0.61 | $4.90 | Special-Premium GPT | 5.6x | $9.80 | $78.40 | 8x |
| `gpt-5.2-chat-latest` | Enterprise Azure 2 | 0.35x | $0.61 | $4.90 | Special-Premium GPT | 5.6x | $9.80 | $78.40 | 8x |
| `gpt-5.2-codex` | Sale 10% Off | 0.54x | $0.95 | $7.56 | Special-Premium GPT | 5.6x | $9.80 | $78.40 | 8x |
| `gpt-5.3-chat-latest` | Enterprise Azure 2 | 0.35x | $0.61 | $4.90 | Special-Premium GPT | 5.6x | $9.80 | $78.40 | 8x |
| `gpt-5.3-codex` | Sale 10% Off | 0.54x | $0.95 | $7.56 | Special-Premium GPT | 5.6x | $9.80 | $78.40 | 8x |
| `gpt-5.3-codex-spark` | Codex Exclusive | 0.8x | $1.40 | $11.20 | Premium OpenAI | 8x | $14.00 | $112.00 | 8x |

<!-- GPT_PRICE_TABLE_END -->

### Anthropic Claudeシリーズ

<!-- CLAUDE_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `claude-fable-5` | Default | 1x | $10.00 | $50.00 | Claude Code Exclusive | 2.4x | $24.00 | $120.00 | 5x |
| `claude-haiku-4-5-20251001` | Default | 1x | $1.00 | $5.00 | Claude Code Exclusive | 2.4x | $2.40 | $12.00 | 5x |
| `claude-opus-4-1-20250805` | Default | 1x | $15.00 | $75.00 | Relay Claude 1 | 4x | $60.00 | $300.00 | 5x |
| `claude-opus-4-5-20251101` | Default | 1x | $5.00 | $25.00 | Claude Code Exclusive | 2.4x | $12.00 | $60.00 | 5x |
| `claude-opus-4-6` | Default | 1x | $5.00 | $25.00 | Claude Code Exclusive | 2.4x | $12.00 | $60.00 | 5x |
| `claude-opus-4-7` | Default | 1x | $5.00 | $25.00 | Claude Code Exclusive | 2.4x | $12.00 | $60.00 | 5x |
| `claude-opus-4-8` | Default | 1x | $5.00 | $25.00 | Claude Code Exclusive | 2.4x | $12.00 | $60.00 | 5x |
| `claude-sonnet-4-20250514` | Default | 1x | $3.00 | $15.00 | Relay Claude 1 | 4x | $12.00 | $60.00 | 5x |
| `claude-sonnet-4-5-20250929` | Default | 1x | $3.00 | $15.00 | Claude Code Exclusive | 2.4x | $7.20 | $36.00 | 5x |
| `claude-sonnet-4-6` | Default | 1x | $3.00 | $15.00 | Claude Code Exclusive | 2.4x | $7.20 | $36.00 | 5x |
| `claude-sonnet-5` | Default | 1x | $2.00 | $10.00 | Claude Code Exclusive | 2.4x | $4.80 | $24.00 | 5x |

<!-- CLAUDE_PRICE_TABLE_END -->

### Google Geminiシリーズ

<!-- GEMINI_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `gemini-2.0-flash-lite` | Relay Gemini | 3.6x | $0.27 | $1.08 | Premium Gemini | 6x | $0.45 | $1.80 | 4x |
| `gemini-2.5-flash` | Gemini CLI | 1x | $0.30 | $2.50 | Premium Gemini | 6x | $1.80 | $15.01 | 8.34x |
| `gemini-2.5-flash-image` | Premium Gemini | 2.4x | $0.00 | $0.00 | Premium Gemini | 6x | $0.00 | $0.00 | 0x |
| `gemini-2.5-flash-lite` | Gemini CLI | 1x | $0.10 | $0.40 | Premium Gemini | 6x | $0.60 | $2.40 | 4x |
| `gemini-2.5-pro` | Gemini CLI | 1x | $1.25 | $10.00 | Premium Gemini | 6x | $7.50 | $60.00 | 8x |
| `gemini-3-pro-image` | Premium Gemini | 2.4x | $0.00 | $0.00 | Premium Gemini | 6x | $0.00 | $0.00 | 0x |
| `gemini-3.1-flash-image` | Premium Gemini | 2.4x | $0.00 | $0.00 | Premium Gemini | 6x | $0.00 | $0.00 | 0x |
| `gemini-3.1-flash-lite` | Gemini CLI | 1x | $0.25 | $1.50 | Premium Gemini | 6x | $1.50 | $9.00 | 6x |

<!-- GEMINI_PRICE_TABLE_END -->

### DeepSeekシリーズ

<!-- DEEPSEEK_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `deepseek-r1` | UChat Qwen | 0.6x | $2.40 | $9.60 | Pure Azure | 1.5x | $6.00 | $24.00 | 4x |
| `deepseek-r1-0528` | UChat Qwen | 0.6x | $2.40 | $9.60 | Pure Azure | 1.5x | $6.00 | $24.00 | 4x |
| `deepseek-r1-2025-01-20` | UChat Qwen | 0.6x | $2.40 | $9.60 | Pure Azure | 1.5x | $6.00 | $24.00 | 4x |
| `deepseek-r1-250120` | UChat Qwen | 0.6x | $2.40 | $9.60 | Pure Azure | 1.5x | $6.00 | $24.00 | 4x |
| `deepseek-r1-250528` | UChat Qwen | 0.6x | $2.40 | $9.60 | Pure Azure | 1.5x | $6.00 | $24.00 | 4x |
| `deepseek-r1-distill-qwen-32b` | Special-Domestic 40% | 0.8x | $1.60 | $4.80 | Pure Azure | 1.5x | $3.00 | $9.00 | 3x |
| `deepseek-r1-distill-qwen-7b` | Special-Domestic 40% | 0.8x | $0.40 | $0.80 | Pure Azure | 1.5x | $0.75 | $1.50 | 2x |
| `deepseek-reasoner` | UChat Qwen | 0.6x | $2.40 | $9.60 | Pure Azure | 1.5x | $6.00 | $24.00 | 4x |

<!-- DEEPSEEK_PRICE_TABLE_END -->

### 中国製モデル（Qwen/Doubao/GLM/Kimi/MiniMax）

<!-- CN_MODEL_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `qwen3-max` | Flash Sale | 0.6x | $1.50 | $6.00 | Pure Azure | 1.5x | $3.75 | $15.00 | 4x |
| `qwen3-max-2026-01-23` | Alibaba 40% | 0.8x | $2.00 | $8.00 | Pure Azure | 1.5x | $3.75 | $15.00 | 4x |
| `qwen3-coder` | Special-Domestic 40% | 0.8x | $4.80 | $19.20 | Pure Azure | 1.5x | $9.00 | $36.00 | 4x |
| `qwen3-coder-plus` | Flash Sale | 0.6x | $2.40 | $9.60 | Special-HC1 | 1.32x | $5.28 | $21.12 | 4x |
| `qwen3.6-plus` | Default | 1x | $2.00 | $12.00 | Pure Azure | 1.5x | $3.00 | $18.00 | 6x |
| `qwen3.7-max` | Flash Sale | 0.6x | $7.20 | $21.60 | Pure Azure | 1.5x | $18.00 | $54.00 | 3x |
| `glm-4.6` | Flash Sale | 0.6x | $1.20 | $4.80 | Pure Azure | 1.5x | $3.00 | $12.00 | 4x |
| `glm-4.5` | Flash Sale | 0.6x | $0.96 | $3.84 | Pure Azure | 1.5x | $2.40 | $9.60 | 4x |
| `glm-4.5-air` | Flash Sale | 0.6x | $0.48 | $3.60 | Pure Azure | 1.5x | $1.20 | $9.00 | 7.5x |
| `kimi-k2` | Special-Domestic 40% | 0.8x | $3.20 | $12.80 | Special-Premium GPT | 5.6x | $22.40 | $89.60 | 4x |
| `kimi-k2.5` | Special-Domestic 40% | 0.8x | $3.20 | $16.80 | Pure Azure | 1.5x | $6.00 | $31.50 | 5.25x |
| `kimi-k3` | Pure Azure | 1.5x | $30.00 | $150.00 | Official Relay | 3x | $60.00 | $300.00 | 5x |

<!-- CN_MODEL_PRICE_TABLE_END -->

> 💡 全33グループ・228モデルの完全な料金表は[Levolink AI 料金ページ](https://ai.levolink.com/pricing)でご確認ください。

### グループティア

| グループタイプ | 倍率 | 最適な用途 |
|------------|-------|----------|
| フラッシュセール | 0.6x | テスト、低コスト利用 |
| Codex专属 | 0.8x | GPTコーディング、日常利用 |
| デフォルト | 1.0x | 標準品質、バランス型 |
| anti/kiro | 1.2x | コスト重視のClaude利用 |
| Claude Code専属 | 2.4x | Claude Codeプログラミング |
| Azureチャネル | 3.0x | 安定性重視のGPT |
| AWSエンタープライズ | 4.0x | エンタープライズ級Claude |
| Vertex/ダイレクト | 6.0x | 最高品質 |
| 公式プレミアム | 16.0x | 完全な公式品質 |

---

## 🛠️ 統合ガイド

### クイックスタート

1. [Levolink AI](https://ai.levolink.com)にアクセス -> 新規登録 -> コンソール -> キー作成
2. チャージ（最低1元）
   - Alipay / WeChat Pay / Crypto Pay / Stripe / Global Pay
3. 統合方法を選択：

### Python（OpenAI SDK）

```python
from openai import OpenAI

client = OpenAI(
    api_key="***",
    base_url="https://ai.levolink.com/v1"
)

# GPT-5.6 Sol
resp = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": "Write a Python quicksort"}]
)

# Claude Sonnet 4.6
resp = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": "Explain quantum computing"}],
    extra_body={"anthropic_version": "vertex-2023-10-01"}
)

# DeepSeek R1
resp = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[{"role": "user", "content": "Implement a web server in Python"}]
)
```

### Node.js / curl

```bash
curl https://ai.levolink.com/v1/chat/completions \
  -H "Authorization: Bearer ***" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.6-sol",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

完全なサンプルは[`examples/`](./examples/)ディレクトリをご覧ください（[Python](examples/quickstart.py) / [Node.js](examples/quickstart.js) / [Shell](examples/quickstart.sh)を含む）。

### Claude Code

```bash
npm install -g @anthropic-ai/claude-code

echo 'export ANTHROPIC_AUTH_TOKEN="***"' >> ~/.bash_profile
echo 'export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"' >> ~/.bash_profile
source ~/.bash_profile

cd your-project && claude
```

📖 完全ガイド：[Claude Code セットアップ](docs/ja/claude-code-guide.md)

### OpenAI Codex

```bash
npm install -g @openai/codex
export OPENAI_API_KEY="***"
export OPENAI_API_BASE="https://ai.levolink.com/v1"
```

📖 完全ガイド：[Codex セットアップ](docs/ja/codex-setup.md)

### Gemini CLI

```bash
npm install -g @google/gemini-cli
export GEMINI_API_KEY="***"
export GEMINI_API_BASE="https://ai.levolink.com/v1"
```

📖 完全ガイド：[Cursor IDE セットアップ](docs/ja/cursor-setup.md)（Gemini CLIにも適用）

### ツール統合

| ツール | 設定方法 |
|------|-------|
| **Dify / FastGPT** | API Key + Base URL: `https://ai.levolink.com/v1` |
| **n8n** | HTTP Request -> URL: `https://ai.levolink.com/v1/chat/completions` |
| **LangChain** | `ChatOpenAI(openai_api_key="key", openai_api_base="https://ai.levolink.com/v1")` |
| **NextChat** | 設定 -> カスタムAPI -> URL: `https://ai.levolink.com/v1` |
| **Cursor IDE** | 設定 -> 環境変数 -> `ANTHROPIC_BASE_URL=https://ai.levolink.com/v1` |
| **OpenClaw** | `openai_api_key: key` + `openai_api_base: https://ai.levolink.com/v1` |

### ユースケース

- **AIコーディング** - Claude Code / CodexでClaude 4.8 / GPT-5.6を使用し、リファクタリングやバグ修正
- **長文処理** - 10万字以上の文書分析、契約書レビュー、論文要約
- **AIエージェント** - 1つのキーで全モデルにアクセス、マルチエージェント並列タスク
- **RAGナレッジベース** - DeepSeek / GPTとベクトルデータベースでエンタープライズQ&A
- **自動化ワークフロー** - n8n / FastGPT / Dify統合でフルオートメーション

---

## 📊 2026年 比較・レビュー

> 2026-07-29時点の公開情報に基づきます。参考用です。

| | [Levolink AI](https://ai.levolink.com) | OpenRouter | SiliconFlow | その他プロキシ | セルフビルド |
|--|-------------|-----------|-------------|---------------|------------|
| モデル数 | **228以上** | ~400 | 約200 | 約100 | 手動 |
| グループ選択肢 | **33グループ** | なし（プロバイダー別） | なし | 1-3 | - |
| 中国CDN | ✅ マルチノード | ❌ 中国ノードなし | ✅ 単一 | ✅ | ❌ |
| 最低チャージ | **¥1** | ~¥35 | ¥50 | ¥20 | - |
| 従量課金 | ✅ | ✅ | ✅ | ✅ | ❌ |
| Claude Code対応 | ✅ | ✅ | ✅ | ✅ | ❌ |
| OpenAI互換 | ✅ | ✅ | ✅ | ✅ | アダプター必要 |
| 価格透明性 | ✅ 33グループ | モデル別、選択制限 | 単一価格 | 単一価格 | - |
| 請求書 | ✅ | ❌ 中国の請求書なし | ✅ | ❌ | - |
| GitHubオープンソース | ✅ 自動価格更新 | ❌ | ❌ | ❌ | - |

---

## ❓ FAQ

**公式APIと同じレスポンスですか？**

はい。Levolink AIは公式モデルへのリクエストを転送するだけです。レスポンスは公式APIと一致しています。

**アカウントがBANされるリスクはありますか？**

いいえ。Levolink AIのキーを使用するため、公式アカウントシステムには関与しません。公式アカウントが停止されるリスクはありません。

**グループ間の違いは何ですか？**

グループによってバックエンドチャネル（Azure/AWS/Vertex/公式ダイレクトなど）が異なり、品質と価格が異なります。低コストグループはコストパフォーマンスに優れ、高価格グループは最大の安定性を提供します。まずデフォルトグループから始め、必要に応じて調整してください。

**streamingに対応していますか？**

はい、全モデルで`stream: true`に対応しており、低レイテンシで利用できます。

**中国からの速度はどのくらいですか？**

中国CDNノードを使用し、レイテンシは通常40-200msです。公式APIに直接接続するよりはるかに高速です。

**無料枠はありますか？**

新規ユーザーにはトライアルクレジットが付与されます。無料で開始し、必要に応じてチャージしてください。

**請求書は発行できますか？**

はい。設定 -> 実名認証 -> ウォレット -> 請求書。5営業日以内に電子請求書が発行されます。

**どのグループを選ぶべきですか？**

- コスト重視：フラッシュセール（0.6x）/ Codex专属（0.8x）
- バランス型：デフォルト（1.0x）
- 高品質：Claude Code専属（2.4x）/ Azure（3.0x）
- 最高品質：Vertex（6.0x）/ 公式プレミアム（16.0x）

---

## 📖 詳細ガイド

| ガイド | 内容 |
|-------|---------|
| [Claude Code セットアップガイド](docs/ja/claude-code-guide.md) | 中国向けClaude Codeの完全設定 |
| [Claude Desktop ガイド](docs/ja/claude-desktop-guide.md) | Claude DesktopにLevolink AIを設定 |
| [Codex セットアップガイド](docs/ja/codex-setup.md) | 中国向けOpenAI Codex CLI設定 |
| [Gemini CLI ガイド](docs/ja/gemini-cli-guide.md) | Gemini CLIでLevolink AI経由でGeminiモデルを使用 |
| [Cursor IDE セットアップ](docs/ja/cursor-setup.md) | CursorでGPT-5.6 / Claude 4.8 / Geminiを使用 |
| [Grok Build ガイド](docs/ja/grok-build-guide.md) | xAI Grok BuildにLevolink AIカスタムモデルを設定 |
| [OpenCode ガイド](docs/ja/opencode-guide.md) | OpenCodeオープンソースエージェントにLevolink AIを設定 |
| [OpenClaw ガイド](docs/ja/openclaw-guide.md) | OpenClaw AgentランタイムにLevolink AIを設定 |
| [CC Switch ガイド](docs/ja/cc-switch-guide.md) | 複数AIツールのLevolink AI設定を統合管理 |
| [Dify 統合ガイド](docs/ja/dify-integration.md) | DifyとLevolink AIの連携 |
| [モデル選択ガイド](docs/ja/model-selection-guide.md) | 228モデルからどれを選ぶ？用途と予算別 |
| [詐欺検出ガイド](docs/ja/fraud-detection-guide.md) | APIプロキシでモデルすり替えを検出する5つの方法 |
| [コスト計算ガイド](docs/ja/cost-calculator-guide.md) | APIコストの見積もりと最適化 |

---

## 🤝 コントリビュート

- 🐛 バグ報告 -> [Issueを開く](https://github.com/jiaqing77cn/levolink-ai-api/issues)
- 📝 ドキュメント改善 -> PRを提出
- 💡 機能要望 -> [Discussionを開始](https://github.com/jiaqing77cn/levolink-ai-api/discussions)
- 📄 コントリビュートガイド -> [CONTRIBUTING.md](./CONTRIBUTING.md)を参照
- 📋 変更履歴 -> [CHANGELOG.md](./CHANGELOG.md)を参照

---

## 📜 ライセンス

MIT License · Copyright (c) 2026 [Levolink AI](https://ai.levolink.com)

## 📢 商標表示

GPTおよびOpenAIはOpenAIの商標です。ClaudeはAnthropic PBCの商標です。GeminiはGoogle LLCの商標です。DeepSeekはDeepSeekの商標です。このリポジトリは互換性の説明のみを目的としており、これらの企業との公式な提携や承認を意味するものではありません。
