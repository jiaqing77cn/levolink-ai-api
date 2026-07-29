# Kostenrechner-Anleitung

> Schätze deine KI-API-Aufrufkosten ab und finde die günstigste Modell- und Gruppenkombination.

## Schnelle Kostenschätzung

### Grundlagen

| Begriff | Bedeutung |
|------|------|
| Eingabe-Token | Text, den du an das Modell sendest (inkl. System-Prompt, Kontext) |
| Ausgabe-Token | Text, den das Modell zurückgibt |
| Multiplikator | Preisfaktor der Gruppe, je niedriger desto günstiger |
| Eingabe-/Ausgabeverhältnis | Ausgabepreis / Eingabepreis (üblicherweise 3-8x) |

| Szenario | Eingabe-Token | Ausgabe-Token |
|------|-----------|------------|
| Einfache Q&A | 50-200 | 100-500 |
| Code-Generierung | 200-1000 | 500-2000 |
| Lange Textanalyse | 5000-50000 | 500-2000 |
| Claude Code-Programmierung | 5000-30000 | 2000-10000 |

## Monatskosten nach Szenario

### Szenario 1: Tägliche KI-Konversation (leichte Nutzung)

- Täglich ca. 20 Konversationen
- Pro Konversation ca. 500 Eingabe + 500 Ausgabe = 1000 Token
- Monatsnutzung: ca. 600.000 Token (300.000 Eingabe + 300.000 Ausgabe)

| Modell | Gruppe | Monatskosten |
|------|------|--------|
| `gpt-5.6-luna` | Zeitlich begrenztes Angebot (0.6x) | ~$0.36 |
| `gemini-2.5-flash` | Gemini-CLI Gemischt (1.0x) | ~$0.90 |
| `claude-sonnet-5` | Standard (1.0x) | ~$3.60 |

### Szenario 2: KI-Programmierassistent (mittlere Nutzung)

- Täglich ca. 50 Code-Anfragen
- Pro Anfrage ca. 5000 Eingabe + 2000 Ausgabe = 7000 Token
- Monatsnutzung: ca. 10,5 Mio. Token (7,5 Mio. Eingabe + 3 Mio. Ausgabe)

| Modell | Gruppe | Monatskosten |
|------|------|--------|
| `gpt-5.6-luna` | Codex Exklusiv (0.8x) | ~$9.12 |
| `gpt-5.6-sol` | Codex Exklusiv (0.8x) | ~$45.60 |
| `claude-sonnet-4-6` | Standard (1.0x) | ~$67.50 |
| `claude-opus-4-8` | Standard (1.0x) | ~$112.50 |

### Szenario 3: Claude Code – intensive Programmierung

- Täglich ca. 100 Anfragen
- Pro Anfrage ca. 15000 Eingabe + 5000 Ausgabe = 20000 Token
- Monatsnutzung: ca. 60 Mio. Token (45 Mio. Eingabe + 15 Mio. Ausgabe)

| Modell | Gruppe | Monatskosten |
|------|------|--------|
| `claude-sonnet-4-6` | Standard (1.0x) | ~$360 |
| `claude-sonnet-4-6` | CC Exklusiv (2.4x) | ~$864 |
| `claude-opus-4-8` | Standard (1.0x) | ~$600 |
| `gpt-5.6-sol` | Codex Exklusiv (0.8x) | ~$228 |

### Szenario 4: Lange Texte verarbeiten

- Täglich ca. 10 Dokumentanalysen
- Pro Analyse ca. 50000 Eingabe + 1000 Ausgabe
- Monatsnutzung: ca. 15,3 Mio. Token (15 Mio. Eingabe + 300.000 Ausgabe)

| Modell | Gruppe | Monatskosten |
|------|------|--------|
| `gemini-2.5-pro` | Gemini-CLI Gemischt (1.0x) | ~$19.13 |
| `claude-opus-4-8` | Standard (1.0x) | ~$82.50 |
| `gpt-5.6-sol` | Codex Exklusiv (0.8x) | ~$50.40 |

## Spartipps

### 1. Gruppenauswahl

| Strategie | Gruppe | Multiplikator | Geeignet für |
|------|------|------|------|
| Maximale Ersparnis | Zeitlich begrenztes Angebot | 0.6x | Tests, nicht-kritische Aufgaben |
| Preis-Leistungs-Optimum | Codex Exklusiv | 0.8x | Tägliche Programmierung |
| Ausgewogen | Standard | 1.0x | Produktionsumgebungen |
| Hohe Stabilität | CC Exklusiv | 2.4x | Claude Code-Programmierung |

### 2. Modelle kombinieren

Verwende nicht nur ein einziges Modell. Empfohlene Strategie:
- **Einfache Aufgaben** (Übersetzung, Zusammenfassung): Gemini 2.5 Flash ($0.30/M Eingabe)
- **Tägliche Programmierung**: GPT-5.6 Luna ($0.80/M Eingabe)
- **Komplexe Programmierung**: Claude Sonnet 4.6 oder GPT-5.6 Sol
- **Sehr lange Texte**: Gemini 2.5 Pro (1M Kontext, $1.25/M Eingabe)

### 3. Caching nutzen

Levolink unterstützt Cached-Preise (Standard 10%). Bei Szenarien mit wiederkehrendem gleichen Kontext (wie Claude Code) kann Caching die Kosten erheblich senken.

### 4. Token-Limits festlegen

Setze auf Anwendungsebene ein max_tokens-Limit, um unerwartete Kostenüberschreitungen zu vermeiden.

## Preisrechner-Skript verwenden

Das Repository enthält ein Preisrechner-Skript:

```bash
cd levolink-ai-api
python scripts/cost_calculator.py
```

Gib deine geschätzte Nutzung ein, um automatisch die Monatskosten für verschiedene Modell-/Gruppenkombinationen zu berechnen.

## Verwandte Links

- [Vollständige Preisliste](../../README_DE.md#-live-modellpreise)
- [Modell-Auswahlleitfaden](./model-selection-guide.md)
- [Levolink AI-Preisseite](https://ai.levolink.com/pricing)
