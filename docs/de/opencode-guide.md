# OpenCode Integrationsanleitung

> Verwenden Sie Levolink AI in OpenCode, um über 500 AI-Modelle ohne VPN aufzurufen.

## Was ist OpenCode?

OpenCode ist ein Open-Source-AI-Programmierassistent (180K+ Stars) und unterstützt Terminal-, Desktop- und IDE-Plugin-Formate. Durch die Konfiguration eines OpenAI-kompatiblen API-Endpunkts kann Levolink AI eingebunden werden.

## Konfigurationsschritte

### 1. OpenCode installieren

```bash
# Empfohlene Installation
curl -fsSL https://opencode.ai/install | bash

> ⚠️ Skript vor der Installation überprüfen

# Oder über npm
npm install -g opencode-ai
```

### 2. Levolink AI als Provider konfigurieren

Erstellen Sie `opencode.json` im Projekt-Stammverzeichnis:

```json
{
  "provider": {
    "levolink": {
      "name": "Levolink AI",
      "api_key": "Ihr Levolink API Key",
      "base_url": "https://ai.levolink.com/v1",
      "models": {
        "gpt-5.6-sol": { "name": "GPT-5.6 Sol" },
        "claude-sonnet-4-6": { "name": "Claude Sonnet 4.6" },
        "gemini-2.5-pro": { "name": "Gemini 2.5 Pro" },
        "deepseek-reasoner": { "name": "DeepSeek R1" }
      }
    }
  },
  "model": "levolink/gpt-5.6-sol"
}
```

### 3. Oder über TUI konfigurieren

```bash
cd your-project
opencode
```

Führen Sie im OpenCode TUI aus:

```
/connect
```

Wählen Sie "Custom OpenAI Compatible" und geben Sie ein:
- **API Key**: Ihr Levolink API Key
- **Base URL**: `https://ai.levolink.com/v1`

### 4. Projekt initialisieren

```
/init
```

OpenCode analysiert die Projektstruktur und erstellt eine `AGENTS.md`-Datei.

## Empfohlene Modelle

| Verwendungszweck | Modell | Gruppenempfehlung |
|------|------|---------|
| Tägliche Programmierung | `gpt-5.6-luna` | Codex exklusiv (0.8x) |
| Komplexe Programmierung | `claude-sonnet-4-6` | Standard (1.0x) |
| Tiefgreifendes Reasoning | `claude-opus-4-8` | Standard (1.0x) |
| Lange Texte | `gemini-2.5-pro` | gemini-cli (1.0x) |
| Preis-Leistungs-Verhältnis | `deepseek-reasoner` | Zeitlich begrenztes Sonderangebot (0.6x) |

## Verwendungsbeispiele

```
# Plan-Modus (mit Tab wechseln)
> Refaktoriere die Authentifizierungslogik in src/api/index.ts

# Build-Modus
> Änderungen gemäß Plan ausführen

# Änderungen rückgängig machen
/undo
```

## Häufig gestellte Fragen

### F: OpenCode meldet "provider not found"

Überprüfen Sie, ob sich `opencode.json` im Projekt-Stammverzeichnis befindet und das JSON-Format korrekt ist.

### F: Wie wechsle ich das Modell?

Geben Sie im TUI `/model levolink/claude-sonnet-4-6` ein, um das Modell zu wechseln.

### F: Wird der Plan-Modus unterstützt?

Ja. Drücken Sie die `Tab`-Taste, um zwischen Build- und Plan-Modus zu wechseln.

### F: Wie konfiguriere ich mehrere Provider?

Fügen Sie in `opencode.json` mehrere Provider hinzu und wechseln Sie mit `/model provider/model`.

## Verwandte Links

- [Levolink AI Webseite](https://ai.levolink.com)
- [OpenCode offizielle Dokumentation](https://opencode.ai/docs/)
- [API Dokumentation](https://levolink.apifox.cn/)
- [Modell-Auswahlleitfaden](./model-selection-guide.md)
