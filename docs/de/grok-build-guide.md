# Grok Build Integrationsanleitung

> Verwenden Sie Levolink AI als Proxy in Grok Build, um Modelle wie GPT/Claude/Gemini aufzurufen.

## Was ist Grok Build?

Grok Build ist der von xAI entwickelte Terminal-AI-Programmierassistent und unterstützt interaktives TUI, Headless-Modus und das ACP-Protokoll. Durch benutzerdefinierte Modellkonfiguration kann Grok Build beliebige Modelle von Levolink AI aufrufen.

## Konfigurationsschritte

### 1. Grok Build installieren

**macOS / Linux:**

```bash
curl -fsSL https://x.ai/cli/install.sh | bash

> ⚠️ Skript vor der Installation überprüfen: curl -fsSL https://x.ai/cli/install.sh | less
```

**Windows (PowerShell):**

```powershell
irm https://x.ai/cli/install.ps1 | iex
```

### 2. Benutzerdefinierte Modelle konfigurieren

Bearbeiten Sie `~/.grok/config.toml` (Windows: `%USERPROFILE%\.grok\config.toml`):

```toml
# Levolink AI als Backend verwenden
[model.levolink-gpt]
model = "gpt-5.6-sol"
base_url = "https://ai.levolink.com/v1"
name = "GPT-5.6 Sol (Levolink)"
env_key = "LEVOLINK_API_KEY"

[model.levolink-claude]
model = "claude-sonnet-4-6"
base_url = "https://ai.levolink.com/v1"
name = "Claude Sonnet 4.6 (Levolink)"
env_key = "LEVOLINK_API_KEY"

[model.levolink-gemini]
model = "gemini-2.5-pro"
base_url = "https://ai.levolink.com/v1"
name = "Gemini 2.5 Pro (Levolink)"
env_key = "LEVOLINK_API_KEY"

[models]
default = "levolink-gpt"
```

### 3. API Key festlegen

```bash
export LEVOLINK_API_KEY="Ihr Levolink API Key"
```

### 4. Verwendung starten

```bash
cd your-project
grok
```

Im TUI mit `/model` das Modell wechseln:

```
/model levolink-claude
```

## Empfohlene Modellkonfiguration

| Verwendungszweck | Modell | Gruppenempfehlung |
|------|------|---------|
| Tägliche Programmierung | `gpt-5.6-luna` | Codex exklusiv (0.8x) |
| Komplexe Programmierung | `gpt-5.6-sol` | Codex exklusiv (0.8x) |
| Tiefgreifendes Reasoning | `claude-opus-4-8` | Standard (1.0x) |
| Lange Texte | `gemini-2.5-pro` | gemini-cli (1.0x) |

## Headless-Modus

```bash
# Aufgabe mit Levolink-Modell ausführen
grok -p "Explain this codebase" -m levolink-claude

# JSON-Ausgabe
grok -p "Analyze architecture" -m levolink-gpt --output-format streaming-json
```

## Häufig gestellte Fragen

### F: Grok Build meldet beim Start "model not found"

Führen Sie `grok inspect` aus, um zu überprüfen, ob die Konfiguration korrekt geladen wurde:

```bash
grok inspect
```

### F: Wie kann ich gleichzeitig Grok-Modelle und Levolink-Modelle verwenden?

Fügen Sie in `config.toml` sowohl die offiziellen xAI-Modelle als auch die Levolink-Modelle hinzu und wechseln Sie mit dem Befehl `/model`.

### F: Wird Streaming-Ausgabe unterstützt?

Ja. Alle Modelle von Levolink AI unterstützen Streaming-Ausgabe.

## Verwandte Links

- [Levolink AI Webseite](https://ai.levolink.com)
- [Grok Build offizielle Dokumentation](https://docs.x.ai/build/overview)
- [Grok Build GitHub](https://github.com/xai-org/grok-build)
- [API Dokumentation](https://levolink.apifox.cn/)
