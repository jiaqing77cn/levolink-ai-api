# OpenClaw Integrationsanleitung

> Verwenden Sie Levolink AI als Backend-Modellanbieter in OpenClaw.

## Was ist OpenClaw?

OpenClaw ist eine Open-Source-AI-Agent-Laufzeitumgebung und unterstützt Multi-Modell-Scheduling, ein Skill-System, zeitgesteuerte Aufgaben, ein Gedächtnissystem und mehr. Durch die Konfiguration eines OpenAI-kompatiblen API-Endpunkts kann Levolink AI eingebunden werden.

## Konfigurationsschritte

### 1. OpenClaw installieren

```bash
# Über npm installieren
npm install -g openclaw

# Oder über Docker
docker run -d openclaw/openclaw
```

### 2. Gateway konfigurieren

Bearbeiten Sie die OpenClaw Gateway-Konfigurationsdatei (normalerweise unter `~/.openclaw/config.yaml` oder im Projektverzeichnis als `config.yaml`):

```yaml
# Modellkonfiguration
model:
  # Standardmodell
  default: volces/glm-5.2

  # OpenAI-kompatibler Provider
  providers:
    - name: levolink
      api_key: "Ihr Levolink API Key"
      base_url: "https://ai.levolink.com/v1"
      models:
        - gpt-5.6-sol
        - gpt-5.6-luna
        - claude-sonnet-4-6
        - claude-opus-4-8
        - gemini-2.5-pro
        - deepseek-reasoner
```

### 3. Oder über Umgebungsvariablen konfigurieren

```bash
# Zu ~/.bash_profile oder ~/.zshrc hinzufügen
export OPENAI_API_KEY="Ihr Levolink API Key"
export OPENAI_API_BASE="https://ai.levolink.com/v1"

source ~/.bash_profile
```

### 4. OpenClaw starten

```bash
openclaw gateway start

# Status überprüfen
openclaw status
```

## Empfohlene Modellkonfiguration

| Verwendungszweck | Modell | Gruppenempfehlung |
|------|------|---------|
| Agent tägliche Aufgaben | `gpt-5.6-luna` | Codex exklusiv (0.8x) |
| Komplexes Reasoning | `claude-opus-4-8` | Standard (1.0x) |
| Programmieraufgaben | `claude-sonnet-4-6` | Standard (1.0x) |
| Lange Textverarbeitung | `gemini-2.5-pro` | gemini-cli (1.0x) |
| Preis-Leistungs-Verhältnis | `deepseek-reasoner` | Zeitlich begrenztes Sonderangebot (0.6x) |

## Modellwechsel in Sitzungen

OpenClaw unterstützt die Zuweisung unterschiedlicher Modelle an verschiedene Sitzungen:

```bash
# Modell in einer Sitzung wechseln
/model claude-opus-4-8

# Aktuelles Modell anzeigen
/status
```

## Multi-Modell-Scheduling

OpenClaw unterstützt die gleichzeitige Steuerung mehrerer Modelle, ideal für parallele Agent-Aufgaben:

```yaml
# Mehrere Provider gleichzeitig verwenden
model:
  providers:
    - name: levolink-gpt
      api_key: "IhrKey"
      base_url: "https://ai.levolink.com/v1"
    - name: levolink-claude
      api_key: "IhrKey"
      base_url: "https://ai.levolink.com/v1"
```

## Häufig gestellte Fragen

### F: OpenClaw meldet "model not available"

Überprüfen Sie, ob das Gateway gestartet wurde und der Modellname korrekt ist:

```bash
openclaw status
openclaw models list
```

### F: Wie setze ich das Standardmodell?

Setzen Sie `model.default` in der Konfigurationsdatei oder verwenden Sie den Befehl `/model` in einer Sitzung.

### F: Wird Streaming-Ausgabe unterstützt?

Ja. OpenClaw verwendet standardmäßig Streaming-Ausgabe.

### F: Wie kontrolliere ich die Kosten?

1. Verwenden Sie die Gruppe mit zeitlich begrenztem Sonderangebot (0.6x Faktor)
2. Wählen Sie für jede Aufgabe das passende Modell
3. Setzen Sie ein Token-Limit in der Konfiguration

## Verwandte Links

- [Levolink AI Webseite](https://ai.levolink.com)
- [OpenClaw offizielle Dokumentation](https://docs.openclaw.ai)
- [OpenClaw GitHub](https://github.com/openclaw/openclaw)
- [API Dokumentation](https://levolink.apifox.cn/)
- [Modell-Auswahlleitfaden](./model-selection-guide.md)
