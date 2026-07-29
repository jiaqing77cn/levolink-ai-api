# Claude Desktop Integrationsanleitung

> Verwenden Sie Levolink AI in der Claude Desktop-App, um Claude-Modelle ohne VPN direkt aufzurufen.

## Was ist Claude Desktop?

Claude Desktop ist der offizielle Desktop-Client von Anthropic und unterstützt macOS sowie Windows. Durch die Konfiguration von Umgebungsvariablen kann Claude Desktop über Levolink AI als Proxy auf Claude-Modelle zugreifen.

## Konfigurationsschritte

### 1. Umgebungsvariablen festlegen

**macOS:**

```bash
# Zu ~/.zshrc oder ~/.bash_profile hinzufügen
export ANTHROPIC_API_KEY="Ihr Levolink API Key"
export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"

# Aktivieren
source ~/.zshrc
```

**Windows:**

```powershell
# PowerShell dauerhaft setzen
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "IhrKey", "User")
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_BASE_URL", "https://ai.levolink.com/v1", "User")
```

### 2. Claude Desktop neu starten

Beenden Sie Claude Desktop vollständig (nicht nur minimieren) und starten Sie es neu. Die App liest dann die neuen Umgebungsvariablen ein.

### 3. Verbindung überprüfen

Senden Sie eine Nachricht in Claude Desktop. Wenn Sie eine normale Antwort erhalten, wurde die Weiterleitung über Levolink AI erfolgreich eingerichtet.

## MCP Server konfigurieren

Claude Desktop unterstützt MCP (Model Context Protocol), um weitere Tools einzubinden:

Bearbeiten Sie die Konfigurationsdatei:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "levolink": {
      "command": "curl",
      "args": ["https://ai.levolink.com/v1/chat/completions"]
    }
  }
}
```

## Empfohlene Modelle

| Verwendungszweck | Modell | Gruppenempfehlung |
|------|------|---------|
| Tägliche Konversation | `claude-sonnet-4-6` | Standard (1.0x) |
| Komplexe Aufgaben | `claude-opus-4-8` | Standard (1.0x) |
| Leichte Aufgaben | `claude-haiku-4-5` | Standard (1.0x) |

## Häufig gestellte Fragen

### F: Claude Desktop liest nach dem Start die Umgebungsvariablen nicht?

Stellen Sie sicher, dass die App vollständig beendet wurde (Rechtsklick auf das Tray-Icon -> Quit) und starten Sie sie dann vom Terminal aus:

```bash
open -a "Claude"
```

### F: Fehlermeldung "connection error"?

Überprüfen Sie, ob der API Key korrekt ist und die Base URL mit `/v1` endet.

### F: Wird Claude Opus 4.8 unterstützt?

Ja. Geben Sie im Gespräch `/model claude-opus-4-8` ein, um das Modell zu wechseln.

## Verwandte Links

- [Levolink AI Webseite](https://ai.levolink.com)
- [Claude Desktop offizieller Download](https://claude.ai/download)
- [API Dokumentation](https://levolink.apifox.cn/)
