# CC Switch Integrationsanleitung

> Verwenden Sie CC Switch, um die Levolink AI-Konfiguration für Claude Code, Codex, Gemini CLI, OpenCode, OpenClaw und andere Tools zentral zu verwalten.

## Was ist CC Switch?

CC Switch ist ein plattformübergreifendes Desktop-Tool zur zentralen Verwaltung von API-Konfigurationen für mehrere AI-Programmierwerkzeuge. Es unterstützt Claude Code, Claude Desktop, Codex, Gemini CLI, Grok Build, OpenCode, OpenClaw und Hermes und ermöglicht das Umschalten des API-Providers mit einem Klick, ohne manuelle Bearbeitung von Konfigurationsdateien.

## Installation

### macOS

```bash
# Homebrew
brew install --cask cc-switch
```

### Windows

Laden Sie das Installationspaket von [ccswitch.io](https://ccswitch.io) herunter.

### Linux

Laden Sie das AppImage von [GitHub Releases](https://github.com/farion1231/cc-switch/releases) herunter.

## Levolink AI konfigurieren

### 1. Provider hinzufügen

Öffnen Sie CC Switch -> Klicken Sie auf «Provider hinzufügen» -> Wählen Sie «Benutzerdefiniert»:

| Konfiguration | Wert |
|--------|-----|
| Name | Levolink AI |
| API Key | Ihr Levolink API Key |
| Base URL | `https://ai.levolink.com/v1` |
| Format | OpenAI Compatible |

### 2. Tools konfigurieren

CC Switch generiert automatisch die Konfiguration für jedes Tool:

**Claude Code:**
```bash
export ANTHROPIC_AUTH_TOKEN="IhrKey"
export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"
```

**Codex:**
```bash
export OPENAI_API_KEY="IhrKey"
export OPENAI_API_BASE="https://ai.levolink.com/v1"
```

**Gemini CLI:**
```bash
export GEMINI_API_KEY="IhrKey"
export GEMINI_API_BASE="https://ai.levolink.com/v1"
```

**OpenCode:**
```json
{
  "provider": {
    "levolink": {
      "api_key": "IhrKey",
      "base_url": "https://ai.levolink.com/v1"
    }
  }
}
```

### 3. Mit einem Klick umschalten

Wählen Sie in der CC Switch-Oberfläche das Ziel-Tool -> Wählen Sie «Levolink AI» -> Klicken Sie auf «Anwenden». CC Switch modifiziert automatisch die Konfigurationsdatei des entsprechenden Tools.

## Empfohlene Konfiguration

| Tool | Empfohlenes Modell | Gruppe |
|------|---------|------|
| Claude Code | `claude-sonnet-4-6` | Standard (1.0x) |
| Codex | `gpt-5.6-sol` | Codex exklusiv (0.8x) |
| Gemini CLI | `gemini-2.5-pro` | gemini-cli (1.0x) |
| OpenCode | `gpt-5.6-luna` | Codex exklusiv (0.8x) |
| OpenClaw | `claude-opus-4-8` | Standard (1.0x) |

## Multi-Provider-Verwaltung

CC Switch unterstützt die gleichzeitige Konfiguration mehrerer Provider für Vergleichstests:

1. «Levolink AI - Zeitlich begrenztes Sonderangebot» hinzufügen (0.6x)
2. «Levolink AI - Standard» hinzufügen (1.0x)
3. «Levolink AI - CC exklusiv» hinzufügen (2.4x)

In der Oberfläche mit einem Klick umschalten, ohne Code oder Umgebungsvariablen zu ändern.

## Häufig gestellte Fragen

### F: Nach dem Ändern der Konfiguration durch CC Switch wird das Tool nicht aktualisiert

Stellen Sie sicher, dass das Ziel-Tool vollständig beendet und neu gestartet wurde. Bei Claude Code müssen die Umgebungsvariablen neu geladen werden (`source`).

### F: Können verschiedene Tools mit unterschiedlichen Providern konfiguriert werden?

Ja. CC Switch kann für jedes Tool unabhängig einen Provider und ein Modell konfigurieren.

### F: Ist CC Switch kostenlos?

CC Switch ist ein Open-Source-Tool und kostenlos nutzbar.

## Verwandte Links

- [Levolink AI Webseite](https://ai.levolink.com)
- [CC Switch Webseite](https://ccswitch.io)
- [CC Switch GitHub](https://github.com/farion1231/cc-switch)
- [API Dokumentation](https://levolink.apifox.cn/)
