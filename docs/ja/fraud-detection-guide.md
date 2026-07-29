# プロキシの水増し検出完全ガイド

> AI API プロキシが安価なモデルで高価なモデルを偽装していないか検出する方法。

## なぜ検出が必要か

一部のプロキシは利益のために、GLM-4 などの安価なモデルで GPT-5 を偽装したり、Haiku で Opus を偽装したりしています。ユーザーは高価なモデルの料金を支払いながら、低品質なモデルの出力を受け取っています。

## 検出方法

### 方法 1：推論能力テスト

ハイエンドモデル（GPT-5.6/Claude Opus 4.8）とローエンドモデルでは、推論能力に明確な差があります。

```python
from openai import OpenAI

client = OpenAI(api_key="あなたのKey", base_url="https://ai.levolink.com/v1")

# テスト 1：古典的な推論問題
resp = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": """
    A farmer has 17 sheep. All but 9 die. How many are left?
    Think step by step.
    """}]
)
print(resp.choices[0].message.content)
# GPT-5.6 の正解: 9 (all but 9 died = 9羽生存)
# ローエンドモデルはよく間違えて: 8 と答える
```

### 方法 2：長コンテキストテスト

ハイエンドモデルは 200K+ token のコンテキストをサポートしますが、ローエンドモデルは通常 8K-32K しか対応していません。

```python
# 100K+ token の長文を送信し、末尾に特定の情報を設定
# その後、モデルにその情報を問う
# ローエンドモデルはコンテキストを失い、答えられない

long_text = "これはとても長いテキストです..." * 5000  # 約 100K tokens
long_text += "パスワードは：PurpleDragon42"

resp = client.chat.completions.create(
    model="claude-opus-4-8",
    messages=[{"role": "user", "content": long_text + "\n\nパスワードは何ですか？"}]
)
# Claude Opus 4.8 は正しく PurpleDragon42 と答える
# ローエンドモデルはコンテキストを失う
```

### 方法 3：コード能力テスト

```python
resp = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": """
    Python でスレッドセーフな LRU キャッシュを実装してください：
    1. TTL 有効期限をサポート
    2. maxsize 制限をサポート
    3. スレッドセーフ
    4. ヒット率統計付き
    """}]
)
# Claude Sonnet 4.6 は完全な実装を提供する
# ローエンドモデルは不完全またはバグのあるコードを返す
```

### 方法 4：Token 課金検証

```python
import tiktoken

# tiktoken で token 数を計算
enc = tiktoken.encoding_for_model("gpt-5.6-sol")
text = "Hello, world! " * 1000
tokens = enc.encode(text)
print(f"実際の token 数: {len(tokens)}")

# リクエストを送信し、課金 token 数を比較
resp = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": text}]
)
print(f"API 返却の prompt_tokens: {resp.usage.prompt_tokens}")
# API 返却値が実際より大幅に多い場合、課金に問題がある可能性
```

### 方法 5：レスポンス速度比較

```python
import time

start = time.time()
resp = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": "Say hello"}]
)
elapsed = time.time() - start

# 正常なレイテンシ：0.5-2s
# 5秒以上の場合、ローエンドモデルへ転送している可能性
# 0.1秒未満の場合、キャッシュの可能性
print(f"レイテンシ: {elapsed:.2f}s")
```

## Levolink AI の透明性

Levolink AI は 33 のグループを提供し、各グループのバックエンドチャネルを明示しています：

| グループ | バックエンド | 倍率 | 透明性 |
|------|------|------|--------|
| 限定特価 | 混合チャネル | 0.6x | 最安値、品質に波がある可能性 |
| Codex 専用 | GPT プログラミング最適化 | 0.8x | 最高のコスパ |
| デフォルト | Azure + MJ | 1.0x | 標準品質 |
| CC 専用 | Claude 最適化 | 2.4x | Claude Code に最適 |
| AWS エンタープライズ | AWS Bedrock | 4.0x | エンタープライズ級の安定性 |
| 正価官転 | 公式直結 | 16.0x | 100% 公式品質 |

ユーザーはニーズに応じて選択でき、価格は透明で水増しありません。
