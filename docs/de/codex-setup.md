# OpenAI Codex Anleitung

> Die beste Lösung für die Nutzung von OpenAI Codex CLI in China, ohne VPN, über Levolink AI.

## Was ist Codex CLI

OpenAI Codex CLI ist der von OpenAI entwickelte KI-Programmierassistent für das Terminal, der Code-Generierung, Refactoring, Bug-Fixing und Test-Erstellung unterstützt. Ähnlich wie Claude Code, aber basierend auf GPT-Modellen.

## Konfigurationsschritte

### 1. Codex CLI installieren

```bash
npm install -g @openai/codex
```

### 2. Umgebungsvariablen konfigurieren

```bash
# Zur ~/.bash_profile oder ~/.zshrc hinzufügen
export OPENAI_API_KEY="Dein Levolink API Key"
export OPENAI_API_BASE="https://ai.levolink.com/v1"

# Aktivieren
source ~/.bash_profile
```

### 3. Mit der Nutzung beginnen

```bash
cd your-project
codex
```

## Empfohlene Gruppen und Modelle

| Verwendung | Modell | Gruppe | Multiplikator | Eingabepreis |
|------|------|------|------|--------|
| Tägliche Programmierung | `gpt-5.6-luna` | Codex Exklusiv | 0.8x | $0.64/M |
| Komplexe Programmierung | `gpt-5.6-sol` | Codex Exklusiv | 0.8x | $3.20/M |
| Leichte Aufgaben | `gpt-5.4-mini` | Zeitlich begrenztes Angebot | 0.6x | $0.27/M |
| Code-Vervollständigung | `gpt-5-codex` | Codex Exklusiv | 0.8x | $0.80/M |

## Windows-Konfiguration

### PowerShell

```powershell
$env:OPENAI_API_KEY="Dein Levolink API Key"
$env:OPENAI_API_BASE="https://ai.levolink.com/v1"
codex
```

### Dauerhafte Einstellung

```powershell
[System.Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "Dein Key", "User")
[System.Environment]::SetEnvironmentVariable("OPENAI_API_BASE", "https://ai.levolink.com/v1", "User")
```

## Häufige Fragen

### F: Codex meldet "Invalid API key"

Überprüfe, ob die Umgebungsvariablen korrekt gesetzt sind:
```bash
echo $OPENAI_API_KEY
echo $OPENAI_API_BASE
# Stelle sicher, dass die Base URL mit /v1 endet
```

### F: Die Antwortgeschwindigkeit ist langsam

Wechsle zur Codex-exklusiven Gruppe (0.8x), die für GPT-Programmiermodelle optimiert ist.

### F: Wird GPT-5.6 Sol unterstützt?

Ja. Gib in Codex `--model gpt-5.6-sol` an, um das Modell auszuwählen.

### F: Was ist der Unterschied zu Claude Code?

| Dimension | Codex CLI | Claude Code |
|------|-----------|-------------|
| Modell | GPT-Serie | Claude-Serie |
| Programmierstil | Direkt und effizient | Tiefgreifendes Reasoning |
| Kontext | 128K | 200K |
| Anwendungsbereich | Schnelle Prototypen, Skripte | Komplexes Refactoring, Architektur-Design |

Beide lassen sich über Levolink AI nutzen – mit einem einzigen Key kannst du zwischen beiden wechseln.

## Verwandte Links

- [Levolink AI Webseite](https://ai.levolink.com)
- [Codex CLI offizielle Dokumentation](https://github.com/openai/codex)
- [API Dokumentation](https://levolink.apifox.cn/)
- [Modell-Auswahlleitfaden](./model-selection-guide.md)
