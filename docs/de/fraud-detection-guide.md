# Vollständiger Leitfaden zur Erkennung von Modell-Manipulation bei API-Proxys

> So erkennst du, ob ein KI-API-Proxy günstige Modelle als teure Modelle ausgibt.

## Warum ist das wichtig?

Einige Proxys verwenden aus Profitgründen billige Modelle wie GLM-4 anstelle von GPT-5 oder Haiku anstelle von Opus. Nutzer zahlen für hochwertige Modelle, erhalten aber die Ausgabe von minderwertigen Modellen.

## Erkennungsmethoden

### Methode 1: Reasoning-Fähigkeit testen

Hochwertige Modelle (GPT-5.6/Claude Opus 4.8) und minderwertige Modelle unterscheiden sich deutlich in ihrer Reasoning-Fähigkeit.

```python
from openai import OpenAI

client = OpenAI(api_key="Dein Key", base_url="https://ai.levolink.com/v1")

# Test 1: Klassisches Reasoning-Problem
resp = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": """
    A farmer has 17 sheep. All but 9 die. How many are left?
    Think step by step.
    """}]
)
print(resp.choices[0].message.content)
# GPT-5.6 korrekte Antwort: 9 (all but 9 died = 9 survived)
# Minderwertige Modelle antworten oft: 8
```

### Methode 2: Langen Kontext testen

Hochwertige Modelle unterstützen 200K+ Token Kontext, minderwertige Modelle通常 nur 8K-32K.

```python
# Sende einen langen Text mit 100K+ Token, am Ende eine bestimmte Information platzieren
# Dann das Modell fragen, was diese Information ist
# Minderwertige Modelle verlieren den Kontext und können nicht antworten

long_text = "Dies ist ein sehr langer Text..." * 5000  # ca. 100K Tokens
long_text += "Das Passwort ist: PurpleDragon42"

resp = client.chat.completions.create(
    model="claude-opus-4-8",
    messages=[{"role": "user", "content": long_text + "\n\nWas ist das Passwort?"}]
)
# Claude Opus 4.8 kann korrekt PurpleDragon42 antworten
# Minderwertige Modelle verlieren den Kontext
```

### Methode 3: Code-Fähigkeit testen

```python
resp = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": """
    Implementiere einen Thread-sicheren LRU-Cache in Python:
    1. Mit TTL-Ablauf
    2. Mit maxsize-Limit
    3. Thread-sicher
    4. Mit Trefferstatistik
    """}]
)
# Claude Sonnet 4.6 liefert eine vollständige Implementierung
# Minderwertige Modelle liefern unvollständigen oder fehlerhaften Code
```

### Methode 4: Token-Abrechnung überprüfen

```python
import tiktoken

# Token-Anzahl mit tiktoken berechnen
enc = tiktoken.encoding_for_model("gpt-5.6-sol")
text = "Hello, world! " * 1000
tokens = enc.encode(text)
print(f"Tatsächliche Token-Anzahl: {len(tokens)}")

# Anfrage senden und abgerechnete Token-Anzahl vergleichen
resp = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": text}]
)
print(f"API zurückgegebene prompt_tokens: {resp.usage.prompt_tokens}")
# Wenn die API deutlich mehr zurückgibt als tatsächlich gesendet, ist die Abrechnung fehlerhaft
```

### Methode 5: Antwortgeschwindigkeit vergleichen

```python
import time

start = time.time()
resp = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": "Say hello"}]
)
elapsed = time.time() - start

# Normale Latenz: 0.5-2s
# Bei >5s eventuell Weiterleitung an minderwertiges Modell
# Bei <0.1s eventuell zwischengespeicherte Antwort
print(f"Latenz: {elapsed:.2f}s")
```

## Transparenz von Levolink AI

Levolink AI bietet 33 Gruppen, wobei jede Gruppe das Backend klar ausweist:

| Gruppe | Backend | Multiplikator | Transparenz |
|------|------|------|--------|
| Zeitlich begrenztes Angebot | Gemischte Kanäle | 0.6x | Am günstigsten, Qualität kann schwanken |
| Codex Exklusiv | GPT-Programmierung optimiert | 0.8x | Bestes Preis-Leistungs-Verhältnis |
| Standard | Azure + MJ | 1.0x | Standardqualität |
| CC Exklusiv | Claude optimiert | 2.4x | Optimal für Claude Code |
| AWS Enterprise | AWS Bedrock | 4.0x | Enterprise-Stabilität |
| Original Official | Offizielle Direktverbindung | 16.0x | 100% offizielle Qualität |

Nutzer können je nach Bedarf wählen – Preise sind transparent, keine Modell-Manipulation.
