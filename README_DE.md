<h1 align="center">🚀 KI-API-Proxy in China | Claude/GPT/Gemini/DeepSeek ohne VPN | Levolink AI</h1>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License"/>
  <img src="https://img.shields.io/badge/500%2B-Models-34d399?style=flat" alt="Models"/>
  <img src="https://img.shields.io/badge/CDN-China%20Accel-3b82f6?style=flat" alt="CDN"/>
  <img src="https://img.shields.io/badge/OpenAI-Compatible-10a37f?style=flat" alt="OpenAI Compatible"/>
</p>

<div align="center">

**Kein VPN · Geringe Latenz · 500+ Modelle · OpenAI Compatible · Claude Code Ready**

[🌐 Website](https://ai.levolink.com) · [📋 Preise](https://ai.levolink.com/pricing) · [📖 API-Dokumentation](https://levolink.apifox.cn/) · [💬 Kontakt](https://ai.levolink.com)

</div>

> Last updated: 2026-08-02 11:32 (UTC+8)| [中文](./README.md) | [English](./README_EN.md) | [한국어](./README_KO.md) | [日本語](./README_JA.md) | [Español](./README_ES.md) | Deutsch

---

## 📋 Inhaltsverzeichnis

- [🖥️ Produktvorschau](#-produktvorschau)
- [🔍 Wie wählt man einen API-Proxy aus](#-wie-wählt-man-einen-api-proxy-aus)
- [💰 Live-Modellpreise](#-live-modellpreise)
- [🛠️ Integrationsleitfaden](#-integrationsleitfaden)
- [📊 Vergleich](#-vergleich)
- [❓ FAQ](#-faq)
- [📖 Ausführliche Leitfäden](#-ausführliche-leitfäden)
- [🤝 Mitwirken](#-mitwirken)

---

## 🖥️ Produktvorschau

![Levolink AI homepage - 500+ AI model API proxy dashboard](https://raw.githubusercontent.com/jiaqing77cn/levolink-ai-api/main/assets/homepage.jpg)

![Levolink AI dashboard - create API keys, view usage, top up account](https://raw.githubusercontent.com/jiaqing77cn/levolink-ai-api/main/assets/console.jpg)

---

## 🔍 Wie wählt man einen API-Proxy aus

Sechs Dimensionen zur Bewertung bei der Auswahl eines KI-API-Proxys:

| Dimension | Was prüfen | Warnsignale |
|-----------|-----------|-------------|
| **Stabilität** | Häufige Ausfälle? Hohe Latenz? | Verbindungsabbrüche, keine Ankündigungen |
| **Geschwindigkeit** | Ist die Antwortlatenz akzeptabel? | >5s Verzögerung bis zum ersten Token |
| **Modellabdeckung** | Neueste Modelle verfügbar? | Langsame Ergänzung neuer Modelle |
| **Preistransparenz** | Klare Abrechnung? Nutzungsprotokolle? | Keine Aufrufprotokolle, intransparent |
| **Modellaustausch** | Günstige Modelle als Premium getarnt? | Auffällig niedrige Preise, schlechte Qualität |
| **Ausfallrisiko** | Unternehmensgeführt? Support vorhanden? | Einzelperson, kein Kundenservice |

### ⚠️ Kontrollliste für Fallstricke

1. **Cache-Preisfalle**: Normaler Cache-Preis liegt bei 10%, einige verlangen 15%-30%
2. **Modellaustausch erkennen**: Outputs zwischen offizieller API und Proxy mit denselben Prompts vergleichen
3. **Token-Zähl-Betrug**: Anfragen mit bekannter Token-Anzahl senden, prüfen ob Abrechnung aufgebläht wird
4. **Niedrigpreis-Falle**: Preise weit unter Marktniveau bedeuten oft GLM, der sich als GPT ausgibt
5. **Ausfallrisiko (Exit Scam)**: Keine großen Guthaben einzahlen! Pay-as-you-go nutzen

### 🔬 Modellaustausch erkennen

```python
# Methode 1: Fähigkeitstest - Reasoning-Prompts verwenden
prompt = "A farmer has 17 sheep. All but 9 die. How many are left?"
# GPT/Claude richtige Antwort: 9
# Low-End-Modelle liegen oft falsch: 8

# Methode 2: Long-Context-Test
# 50K+ Token langen Text senden, nach Details am Ende fragen
# Low-End-Modelle verlieren den Kontext

# Methode 3: Code-Fähigkeitstest
prompt = "Implement an LRU cache with TTL expiration in Python"
# Code-Qualität zwischen offizieller API und Proxy vergleichen
```

---

## 💰 Live-Modellpreise

> Preise werden automatisch von der [Levolink API](https://ai.levolink.com/api/pricing) über GitHub Actions abgerufen, stündlich aktualisiert.
>
> Einheit: USD / Million Tokens | Output/Input-Verhältnis = Output-Preis ÷ Input-Preis

### OpenAI GPT Serie

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
| `gpt-5.1-codex-mini` | Enterprise Azure 2 | 0.35x | $0.09 | $0.70 | Pure Azure | 1.5x | $0.38 | $3.00 | 8x |
| `gpt-5.2-chat` | Enterprise Azure 2 | 0.35x | $0.61 | $4.90 | Special-Premium GPT | 5.6x | $9.80 | $78.40 | 8x |
| `gpt-5.2-chat-latest` | Enterprise Azure 2 | 0.35x | $0.61 | $4.90 | Special-Premium GPT | 5.6x | $9.80 | $78.40 | 8x |
| `gpt-5.2-codex` | Sale 10% Off | 0.54x | $0.95 | $7.56 | Special-Premium GPT | 5.6x | $9.80 | $78.40 | 8x |
| `gpt-5.3-chat-latest` | Enterprise Azure 2 | 0.35x | $0.61 | $4.90 | Special-Premium GPT | 5.6x | $9.80 | $78.40 | 8x |
| `gpt-5.3-codex` | Sale 10% Off | 0.54x | $0.95 | $7.56 | Special-Premium GPT | 5.6x | $9.80 | $78.40 | 8x |
| `gpt-5.3-codex-spark` | Codex Exclusive | 0.8x | $1.40 | $11.20 | Premium OpenAI | 8x | $14.00 | $112.00 | 8x |

<!-- GPT_PRICE_TABLE_END -->

### Anthropic Claude Serie

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

### Google Gemini Serie

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

### DeepSeek Serie

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

### Chinesische Modelle (Qwen/Doubao/GLM/Kimi/MiniMax)

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

> 💡 Vollständige Preisliste mit allen 33 Gruppen und 228 Modellen unter [Levolink AI Pricing](https://ai.levolink.com/pricing)

### Gruppen-Stufen

| Gruppentyp | Verhältnis | Optimal für |
|------------|-----------|-------------|
| Flash Sale | 0.6x | Tests, kostengünstige Nutzung |
| Codex Exclusive | 0.8x | GPT-Codierung, tägliche Nutzung |
| Default | 1.0x | Standardqualität, ausgewogen |
| anti/kiro | 1.2x | Budget Claude |
| Claude Code Exclusive | 2.4x | Claude Code Programmierung |
| Azure Channel | 3.0x | Stabiles GPT |
| AWS Enterprise | 4.0x | Enterprise-Claude |
| Vertex/Direct | 6.0x | Höchste Qualität |
| Official Premium | 16.0x | Volle offizielle Qualität |

---

## 🛠️ Integrationsleitfaden

### Schnellstart

1. [Levolink AI](https://ai.levolink.com) besuchen -> Registrieren -> Konsole -> Key erstellen
2. Guthaben aufladen (mind. 1 Yuan)
   - Alipay / WeChat Pay / Crypto Pay / Stripe / Global Pay
3. Integrationsmethode wählen:

### Python (OpenAI SDK)

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

Vollständige Beispiele im Verzeichnis [`examples/`](./examples/) (inkl. [Python](examples/quickstart.py) / [Node.js](examples/quickstart.js) / [Shell](examples/quickstart.sh)).

### Claude Code

```bash
npm install -g @anthropic-ai/claude-code

echo 'export ANTHROPIC_AUTH_TOKEN="***"' >> ~/.bash_profile
echo 'export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"' >> ~/.bash_profile
source ~/.bash_profile

cd your-project && claude
```

📖 Vollständiger Leitfaden: [Claude Code Setup](docs/de/claude-code-guide.md)

### OpenAI Codex

```bash
npm install -g @openai/codex
export OPENAI_API_KEY="***"
export OPENAI_API_BASE="https://ai.levolink.com/v1"
```

📖 Vollständiger Leitfaden: [Codex Setup](docs/de/codex-setup.md)

### Gemini CLI

```bash
npm install -g @google/gemini-cli
export GEMINI_API_KEY="***"
export GEMINI_API_BASE="https://ai.levolink.com/v1"
```

📖 Vollständiger Leitfaden: [Cursor IDE Setup](docs/de/cursor-setup.md) (gilt auch für Gemini CLI)

### Tool-Integrationen

| Tool | Setup |
|------|-------|
| **Dify / FastGPT** | API Key + Base URL: `https://ai.levolink.com/v1` |
| **n8n** | HTTP Request -> URL: `https://ai.levolink.com/v1/chat/completions` |
| **LangChain** | `ChatOpenAI(openai_api_key="key", openai_api_base="https://ai.levolink.com/v1")` |
| **NextChat** | Settings -> Custom API -> URL: `https://ai.levolink.com/v1` |
| **Cursor IDE** | Settings -> Env Vars -> `ANTHROPIC_BASE_URL=https://ai.levolink.com/v1` |
| **OpenClaw** | `openai_api_key: key` + `openai_api_base: https://ai.levolink.com/v1` |

### Anwendungsfälle

- **AI-Codierung** - Claude Code / Codex mit Claude 4.8 / GPT-5.6 für Refactoring, Bug-Fixes
- **Lange Dokumente verarbeiten** - 100K+ Wort-Analyse, Vertragsprüfung, Papier-Zusammenfassung
- **KI-Agenten** - Ein Key für alle Modelle, Multi-Agent-Parallelaufgaben
- **RAG-Wissensbasen** - DeepSeek / GPT mit Vektordatenbanken für Enterprise-Q&A
- **Automatisierte Workflows** - n8n / FastGPT / Dify-Integration für vollständige Automatisierung

---

## 📊 Vergleich & Review 2026

> Basierend auf öffentlich verfügbaren Informationen vom 2026-07-29. Nur als Referenz.

| | [Levolink AI](https://ai.levolink.com) | OpenRouter | SiliconFlow | Andere Proxys | Selbstgebaut |
|--|-------------|-----------|-------------|---------------|------------|
| Modellanzahl | **228+** | ~400 | ~200 | ~100 | Manuell |
| Gruppen-Optionen | **33 Gruppen** | Keine (pro Anbieter) | Keine | 1-3 | - |
| China CDN | ✅ Multi-Node | ❌ Keine China-Knoten | ✅ Einzel | ✅ | ❌ |
| Mindestaufladung | **¥1** | ~¥35 | ¥50 | ¥20 | - |
| Pay-as-you-go | ✅ | ✅ | ✅ | ✅ | ❌ |
| Claude Code ready | ✅ | ✅ | ✅ | ✅ | ❌ |
| OpenAI compatible | ✅ | ✅ | ✅ | ✅ | Adapter nötig |
| Preistransparenz | ✅ 33 Gruppen | Pro Modell, eingeschränkte Wahl | Einzelpreis | Einzelpreis | - |
| Rechnung | ✅ | ❌ Keine CN-Rechnung | ✅ | ❌ | - |
| GitHub Open Source | ✅ Auto-Pricing | ❌ | ❌ | ❌ | - |

---

## ❓ FAQ

**Sind die Antworten identisch mit der offiziellen API?**

Ja. Levolink AI leitet Anfragen nur an offizielle Modelle weiter - die Antworten sind mit der offiziellen API konsistent.

**Kann mein Account gesperrt werden?**

Nein. Sie verwenden den Key von Levolink AI, nicht das offizielle Account-System - Ihr offizieller Account ist nicht gefährdet.

**Was ist der Unterschied zwischen den Gruppen?**

Verschiedene Gruppen entsprechen verschiedenen Backend-Kanälen (Azure/AWS/Vertex/Official Direct usw.) mit unterschiedlicher Qualität und Preis. Kosten günstigere Gruppen bieten besseres Preis-Leistungs-Verhältnis; teurere Gruppen bieten maximale Stabilität. Mit der Default-Gruppe starten und bei Bedarf anpassen.

**Wird streaming unterstützt?**

Ja, alle Modelle unterstützen `stream: true` mit geringer Latenz.

**Wie schnell ist es aus China?**

China CDN-Knoten, Latenz typischerweise 40-200ms - deutlich schneller als direkte Verbindung zu offiziellen APIs.

**Gibt es eine kostenlose Stufe?**

Neue Nutzer erhalten Testguthaben. Kostenlos starten, bei Bedarf aufladen.

**Kann ich eine Rechnung erhalten?**

Ja. Settings -> Identitätsverifizierung -> Wallet -> Rechnung. E-Rechnung wird innerhalb von 5 Werktagen ausgestellt.

**Welche Gruppe soll ich wählen?**

- Budget: Flash Sale (0.6x) / Codex Exclusive (0.8x)
- Ausgewogen: Default (1.0x)
- Hohe Qualität: Claude Code Exclusive (2.4x) / Azure (3.0x)
- Maximale Qualität: Vertex (6.0x) / Official Premium (16.0x)

---

## 📖 Ausführliche Leitfäden

| Leitfaden | Inhalt |
|-----------|--------|
| [Claude Code Anleitung](docs/de/claude-code-guide.md) | Vollständige Claude-Code-Konfiguration für China |
| [Claude Desktop Anleitung](docs/de/claude-desktop-guide.md) | Claude Desktop mit Levolink AI konfigurieren |
| [Codex Anleitung](docs/de/codex-setup.md) | OpenAI Codex CLI-Konfiguration für China |
| [Gemini CLI Anleitung](docs/de/gemini-cli-guide.md) | Gemini CLI mit Levolink AI für Gemini-Modelle |
| [Cursor IDE Anleitung](docs/de/cursor-setup.md) | GPT-5.6 / Claude 4.8 / Gemini in Cursor verwenden |
| [Grok Build Anleitung](docs/de/grok-build-guide.md) | xAI Grok Build mit Levolink AI Custom-Modellen |
| [OpenCode Anleitung](docs/de/opencode-guide.md) | OpenCode Open-Source-Agent mit Levolink AI |
| [OpenClaw Anleitung](docs/de/openclaw-guide.md) | OpenClaw Agent-Runtime mit Levolink AI |
| [CC Switch Anleitung](docs/de/cc-switch-guide.md) | Unified Konfigurationsmanagement für mehrere AI-Tools |
| [Dify Integrationsleitfaden](docs/de/dify-integration.md) | Dify mit Levolink AI verbinden |
| [Modell-Auswahlleitfaden](docs/de/model-selection-guide.md) | Welches der 228 Modelle wählen? Nach Anwendungsfall & Budget |
| [Fraud Detection Leitfaden](docs/de/fraud-detection-guide.md) | 5 Methoden zur Erkennung von Modellaustausch bei API-Proxys |
| [Kostenrechner-Anleitung](docs/de/cost-calculator-guide.md) | API-Kosten schätzen und Ausgaben optimieren |

---

## 🤝 Mitwirken

- 🐛 Fehler melden -> [Issue eröffnen](https://github.com/jiaqing77cn/levolink-ai-api/issues)
- 📝 Dokumentation verbessern -> PR einreichen
- 💡 Feature wünschen -> [Diskussion starten](https://github.com/jiaqing77cn/levolink-ai-api/discussions)
- 📄 Mitwirkungsleitfaden -> Siehe [CONTRIBUTING.md](./CONTRIBUTING.md)
- 📋 Changelog -> Siehe [CHANGELOG.md](./CHANGELOG.md)

---

## 📜 Lizenz

MIT License · Copyright (c) 2026 [Levolink AI](https://ai.levolink.com)

## 📢 Markenrechtlicher Hinweis

GPT und OpenAI sind Marken von OpenAI. Claude ist eine Marke von Anthropic PBC. Gemini ist eine Marke von Google LLC. DeepSeek ist eine Marke von DeepSeek. Dieses Repository beschreibt lediglich Kompatibilität und impliziert keine offizielle Verbindung mit oder Unterstützung durch diese Unternehmen.
