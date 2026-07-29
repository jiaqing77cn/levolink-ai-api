# OpenAI Codex セットアップガイド

> 中国国内で OpenAI Codex CLI を使う最適なソリューション。VPN 不要、Levolink AI 経由で利用。

## Codex CLI とは

OpenAI Codex CLI は OpenAI が提供するターミナル AI プログラミングアシスタントです。コード生成、リファクタリング、バグ修正、テスト作成などをサポートしています。Claude Code と似ていますが、GPT モデルをベースにしています。

## 設定手順

### 1. Codex CLI のインストール

```bash
npm install -g @openai/codex
```

### 2. 環境変数の設定

```bash
# ~/.bash_profile または ~/.zshrc に追加
export OPENAI_API_KEY="あなたの Levolink API Key"
export OPENAI_API_BASE="https://ai.levolink.com/v1"

# 反映
source ~/.bash_profile
```

### 3. 使い始める

```bash
cd your-project
codex
```

## 推奨グループとモデル

| 用途 | モデル | グループ | 倍率 | 入力価格 |
|------|------|------|------|--------|
| 日常プログラミング | `gpt-5.6-luna` | Codex 専用 | 0.8x | $0.64/M |
| 複雑なプログラミング | `gpt-5.6-sol` | Codex 専用 | 0.8x | $3.20/M |
| 軽量タスク | `gpt-5.4-mini` | 限定特価 | 0.6x | $0.27/M |
| コード補完 | `gpt-5-codex` | Codex 専用 | 0.8x | $0.80/M |

## Windows 設定

### PowerShell

```powershell
$env:OPENAI_API_KEY="あなたの Levolink API Key"
$env:OPENAI_API_BASE="https://ai.levolink.com/v1"
codex
```

### 永続設定

```powershell
[System.Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "あなたのKey", "User")
[System.Environment]::SetEnvironmentVariable("OPENAI_API_BASE", "https://ai.levolink.com/v1", "User")
```

## よくある質問

### Q: Codex で "Invalid API key" エラーが出る

環境変数が正しく設定されているか確認してください：
```bash
echo $OPENAI_API_KEY
echo $OPENAI_API_BASE
# Base URL の末尾に /v1 があることを確認
```

### Q: レスポンスが遅い

Codex 専用グループ（0.8x）に切り替えてください。このグループは GPT プログラミングモデル向けに最適化されています。

### Q: GPT-5.6 Sol に対応していますか

対応しています。Codex で `--model gpt-5.6-sol` でモデルを指定できます。

### Q: Claude Code との違いは

| 項目 | Codex CLI | Claude Code |
|------|-----------|-------------|
| モデル | GPT シリーズ | Claude シリーズ |
| プログラミングスタイル | 直接的で効率的 | 深い推論 |
| コンテキスト | 128K | 200K |
| 適したシーン | 高速プロトタイピング、スクリプト | 複雑なリファクタリング、アーキテクチャ設計 |

どちらも Levolink AI 経由で利用でき、1つの Key で切り替え可能です。

## 関連リンク

- [Levolink AI 公式サイト](https://ai.levolink.com)
- [Codex CLI 公式ドキュメント](https://github.com/openai/codex)
- [API ドキュメント](https://levolink.apifox.cn/)
- [モデル選択ガイド](./model-selection-guide.md)
