# Gemini CLI 連携ガイド

> Gemini CLI で Levolink AI を使用し、Gemini 3.5 Pro / Flash などのモデルを呼び出します。VPN は不要です。

## Gemini CLI とは

Gemini CLI は Google が提供するターミナル AI アシスタントで、コード生成、ドキュメント分析、タスク自動化などをサポートしています。Levolink AI 経由で、国内のユーザーも Gemini シリーズモデルを直接利用できます。

## 設定手順

### 1. Gemini CLI のインストール

```bash
npm install -g @google/gemini-cli
```

### 2. 環境変数の設定

```bash
# ~/.bash_profile または ~/.zshrc に追加
export GEMINI_API_KEY="あなたの Levolink API Key"
export GEMINI_API_BASE="https://ai.levolink.com/v1"

# 反映
source ~/.bash_profile
```

### 3. 使い方

```bash
cd your-project
gemini
```

## 推奨モデルとグループ

| 用途 | モデル | グループ | 倍率 |
|------|------|------|------|
| 日常使用 | `gemini-2.5-flash` | gemini-cli | 1.0x |
| 軽量タスク | `gemini-2.5-flash-lite` | gemini-cli | 1.0x |
| 複雑なタスク | `gemini-2.5-pro` | gemini-cli | 1.0x |
| 画像生成 | `gemini-3-pro-image` | プレミアムGemini | 2.4x |

## モデルの指定

```bash
# 特定のモデルを使用
gemini --model gemini-2.5-pro

# またはインタラクティブモードで切り替え
> /model gemini-2.5-flash
```

## Windows 設定

```powershell
$env:GEMINI_API_KEY="あなたの Levolink API Key"
$env:GEMINI_API_BASE="https://ai.levolink.com/v1"
gemini
```

永続的な設定：

```powershell
[System.Environment]::SetEnvironmentVariable("GEMINI_API_KEY", "あなたのKey", "User")
[System.Environment]::SetEnvironmentVariable("GEMINI_API_BASE", "https://ai.levolink.com/v1", "User")
```

## よくある質問

### Q: Gemini CLI で "Invalid API key" エラーが出る

環境変数が正しく設定されているか確認してください：

```bash
echo $GEMINI_API_KEY
echo $GEMINI_API_BASE
# Base URL の末尾に /v1 があることを確認
```

### Q: レスポンスが遅い

Gemini-CLI グループ（1.0x 倍率）は Gemini モデル向けに最適化されており、高速に動作します。

### Q: Gemini 3.5 Pro に対応していますか

対応しています。`--model gemini-3-pro-image` を使用するか、インタラクティブモードで切り替えてください。

## 関連リンク

- [Levolink AI 公式サイト](https://ai.levolink.com)
- [Gemini CLI 公式ドキュメント](https://github.com/google-gemini/gemini-cli)
- [API ドキュメント](https://levolink.apifox.cn/)
- [モデル選択ガイド](./model-selection-guide.md)
