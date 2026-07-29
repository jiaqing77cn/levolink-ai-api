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

> Last updated: 2026-07-28 09:51 (UTC+8) | [中文](./README.md) | [English](./README_EN.md) | [한국어](./README_KO.md) | 日本語 | [Español](./README_ES.md) | [Deutsch](./README_DE.md)

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
| `gpt-5-codex` | enterprise-a… | 0.35x | $0.15 | $1.22 | Codex专属 | 0.8x | $0.35 | $2.80 | 8x |
| `gpt-5-mini` | enterprise-a… | 0.35x | $0.03 | $0.24 | 特供-优质gpt | 5.6x | $0.49 | $3.92 | 8x |
| `gpt-5-mini-2025-08-07` | enterprise-a… | 0.35x | $0.03 | $0.24 | 特供-优质gpt | 5.6x | $0.49 | $3.92 | 8x |
| `gpt-5-nano` | enterprise-a… | 0.35x | $0.01 | $0.05 | 特供-优质gpt | 5.6x | $0.10 | $0.78 | 8x |
| `gpt-5-nano-2025-08-07` | enterprise-a… | 0.35x | $0.01 | $0.05 | 特供-优质gpt | 5.6x | $0.10 | $0.78 | 8x |
| `gpt-5-pro` | enterprise-a… | 0.35x | $1.84 | $14.70 | 特供-优质gpt | 5.6x | $29.40 | $235.20 | 8x |
| `gpt-5.1-codex` | 特价9折 | 0.54x | $0.36 | $2.92 | Codex专属 | 0.8x | $0.54 | $4.32 | 8x |
| `gpt-5.1-codex-max` | 特价9折 | 0.54x | $0.36 | $2.92 | 纯AZ | 1.5x | $1.01 | $8.10 | 8x |
| `gpt-5.1-codex-mini` | enterprise-a… | 0.35x | $0.03 | $0.24 | 纯AZ | 1.5x | $0.13 | $1.05 | 8x |
| `gpt-5.2-chat` | enterprise-a… | 0.35x | $0.21 | $1.71 | 特供-优质gpt | 5.6x | $3.43 | $27.44 | 8x |
| `gpt-5.2-chat-latest` | enterprise-a… | 0.35x | $0.21 | $1.71 | 特供-优质gpt | 5.6x | $3.43 | $27.44 | 8x |
| `gpt-5.2-codex` | 特价9折 | 0.54x | $0.51 | $4.08 | 特供-优质gpt | 5.6x | $5.29 | $42.34 | 8x |
| `gpt-5.3-chat-latest` | enterprise-a… | 0.35x | $0.21 | $1.71 | 特供-优质gpt | 5.6x | $3.43 | $27.44 | 8x |
| `gpt-5.3-codex` | 特价9折 | 0.54x | $0.51 | $4.08 | 特供-优质gpt | 5.6x | $5.29 | $42.34 | 8x |
| `gpt-5.3-codex-spark` | Codex专属 | 0.8x | $1.12 | $8.96 | Premium OpenAI | 8x | $11.20 | $89.60 | 8x |

<!-- GPT_PRICE_TABLE_END -->

### Anthropic Claudeシリーズ

<!-- CLAUDE_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `claude-fable-5` | default | 1x | $10.00 | $50.00 | Claude Code专… | 2.4x | $24.00 | $120.00 | 5x |
| `claude-haiku-4-5-20251001` | default | 1x | $1.00 | $5.00 | Claude Code专… | 2.4x | $2.40 | $12.00 | 5x |
| `claude-opus-4-1-20250805` | default | 1x | $15.00 | $75.00 | Claude Code专… | 2.4x | $36.00 | $180.00 | 5x |
| `claude-opus-4-5-20251101` | default | 1x | $5.00 | $25.00 | Claude Code专… | 2.4x | $12.00 | $60.00 | 5x |
| `claude-opus-4-6` | default | 1x | $5.00 | $25.00 | Claude Code专… | 2.4x | $12.00 | $60.00 | 5x |
| `claude-opus-4-7` | default | 1x | $5.00 | $25.00 | Claude Code专… | 2.4x | $12.00 | $60.00 | 5x |
| `claude-opus-4-8` | default | 1x | $5.00 | $25.00 | Claude Code专… | 2.4x | $12.00 | $60.00 | 5x |
| `claude-sonnet-4-20250514` | default | 1x | $3.00 | $15.00 | Claude Code专… | 2.4x | $7.20 | $36.00 | 5x |
| `claude-sonnet-4-5-20250929` | default | 1x | $3.00 | $15.00 | Claude Code专… | 2.4x | $7.20 | $36.00 | 5x |
| `claude-sonnet-4-6` | default | 1x | $3.00 | $15.00 | Claude Code专… | 2.4x | $7.20 | $36.00 | 5x |
| `claude-sonnet-5` | default | 1x | $2.00 | $10.00 | Claude Code专… | 2.4x | $4.80 | $24.00 | 5x |

<!-- CLAUDE_PRICE_TABLE_END -->

### Google Geminiシリーズ

<!-- GEMINI_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `gemini-2.0-flash-lite` | 官转gemini | 3.6x | $0.97 | $3.89 | Premium Gemini | 6x | $1.62 | $6.48 | 4x |
| `gemini-2.5-flash` | gemini-cli | 1x | $0.30 | $2.50 | Premium Gemini | 6x | $1.80 | $15.01 | 8.34x |
| `gemini-2.5-flash-image` | 优质gemini | 2.4x | $0.00 | $0.00 | Premium Gemini | 6x | $0.00 | $0.00 | 0x |
| `gemini-2.5-flash-lite` | gemini-cli | 1x | $0.10 | $0.40 | Premium Gemini | 6x | $0.60 | $2.40 | 4x |
| `gemini-2.5-pro` | gemini-cli | 1x | $1.25 | $10.00 | Premium Gemini | 6x | $7.50 | $60.00 | 8x |
| `gemini-3-pro-image` | 优质gemini | 2.4x | $0.00 | $0.00 | Premium Gemini | 6x | $0.00 | $0.00 | 0x |
| `gemini-3.1-flash-image` | 优质gemini | 2.4x | $0.00 | $0.00 | Premium Gemini | 6x | $0.00 | $0.00 | 0x |
| `gemini-3.1-flash-lite` | gemini-cli | 1x | $0.25 | $1.50 | Premium Gemini | 6x | $1.50 | $9.00 | 6x |

<!-- GEMINI_PRICE_TABLE_END -->

### DeepSeekシリーズ

<!-- DEEPSEEK_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `deepseek-r1` | uchat_qwen | 0.6x | $1.44 | $5.76 | 纯AZ | 1.5x | $3.60 | $14.40 | 4x |
| `deepseek-r1-0528` | uchat_qwen | 0.6x | $1.44 | $5.76 | 纯AZ | 1.5x | $3.60 | $14.40 | 4x |
| `deepseek-r1-2025-01-20` | uchat_qwen | 0.6x | $1.44 | $5.76 | 纯AZ | 1.5x | $3.60 | $14.40 | 4x |
| `deepseek-r1-250120` | uchat_qwen | 0.6x | $1.44 | $5.76 | 纯AZ | 1.5x | $3.60 | $14.40 | 4x |
| `deepseek-r1-250528` | uchat_qwen | 0.6x | $1.44 | $5.76 | 纯AZ | 1.5x | $3.60 | $14.40 | 4x |
| `deepseek-r1-distill-qwen-32b` | 特供-国产4折 | 0.8x | $1.28 | $3.84 | 纯AZ | 1.5x | $2.40 | $7.20 | 3x |
| `deepseek-r1-distill-qwen-7b` | 特供-国产4折 | 0.8x | $0.32 | $0.64 | 纯AZ | 1.5x | $0.60 | $1.20 | 2x |
| `deepseek-reasoner` | uchat_qwen | 0.6x | $1.44 | $5.76 | 纯AZ | 1.5x | $3.60 | $14.40 | 4x |

<!-- DEEPSEEK_PRICE_TABLE_END -->

### 中国製モデル（Qwen/Doubao/GLM/Kimi/MiniMax）

<!-- CN_MODEL_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `qwen3-max` | 限时特价 | 0.6x | $0.90 | $3.60 | 纯AZ | 1.5x | $2.25 | $9.00 | 4x |
| `qwen3-max-2026-01-23` | 阿里4折 | 0.8x | $1.60 | $6.40 | 纯AZ | 1.5x | $3.00 | $12.00 | 4x |
| `qwen3-coder` | 特供-国产4折 | 0.8x | $3.84 | $15.36 | 纯AZ | 1.5x | $7.20 | $28.80 | 4x |
| `qwen3-coder-plus` | 限时特价 | 0.6x | $1.44 | $5.76 | 特供-HC1 | 1.32x | $3.17 | $12.67 | 4x |
| `qwen3.6-plus` | default | 1x | $2.00 | $12.00 | 纯AZ | 1.5x | $3.00 | $18.00 | 6x |
| `qwen3.7-max` | 限时特价 | 0.6x | $4.32 | $12.96 | 纯AZ | 1.5x | $10.80 | $32.40 | 3x |
| `glm-4.6` | 限时特价 | 0.6x | $0.72 | $2.88 | 纯AZ | 1.5x | $1.80 | $7.20 | 4x |
| `glm-4.5` | 限时特价 | 0.6x | $0.58 | $2.30 | 纯AZ | 1.5x | $1.44 | $5.76 | 4x |
| `glm-4.5-air` | 限时特价 | 0.6x | $0.29 | $2.16 | 纯AZ | 1.5x | $0.72 | $5.40 | 7.5x |
| `kimi-k2` | enterprise-a… | 0.45x | $0.81 | $3.24 | 特供-优质gpt | 5.6x | $10.08 | $40.32 | 4x |
| `kimi-k2.5` | 特供-国产4折 | 0.8x | $2.56 | $13.44 | 纯AZ | 1.5x | $4.80 | $25.20 | 5.25x |
| `kimi-k3` | 纯AZ | 1.5x | $45.00 | $225.00 | 官转 | 3x | $90.00 | $450.00 | 5x |

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

| | [Levolink AI](https://ai.levolink.com) | OpenRouter | SiliconFlow | その他プロキシ | セルフビルド |
|--|-------------|-----------|-------------|---------------|------------|
| モデル数 | **500以上** | ~400 | 約200 | 約100 | 手動 |
| グループ選択肢 | **33グループ** | なし（プロバイダー別） | なし | 1-3 | - |
| 中国CDN | ✅ マルチノード | ❌ 中国ノードなし | ✅ 単一 | ✅ | ❌ |
| 最低チャージ | **1元** | ~$5（~35元） | 50元 | 20元 | - |
| 従量課金 | ✅ | ✅ | ✅ | ✅ | ❌ |
| Claude Code対応 | ✅ | ✅ | ✅ | ✅ | ❌ |
| OpenAI互換 | ✅ | ✅ | ✅ | ✅ | アダプター必要 |
| 価格透明性 | ✅ 33グループ | モデル別、選択制限 | 単一価格 | 単一価格 | - |
| 請求書 | ✅ | ❌ 中国の請求書なし | ✅ | ❌ | - |
| GitHubオープンソース | ✅ 自動価格更新 | ❌ | ❌ | ❌ | - |

---

## ❓ FAQ

**公式APIと同じレスポンスですか？**

はい。Levolink AIは公式モデルへのリクエストを転送するだけです。レスポンスはバイト単位で完全に同一です。

**アカウントがBANされるリスクはありますか？**

いいえ。Levolink AIのキーを使用するため、公式アカウントシステムには関与しません。BANリスクはありません。

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
