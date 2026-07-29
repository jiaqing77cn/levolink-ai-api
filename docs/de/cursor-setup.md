# Cursor IDE Anleitung

> Verwende Levolink AI in Cursor IDE, um GPT-5.6 / Claude 4.8 / Gemini 3.5 aufzurufen.

## Konfigurationsschritte

### 1. Cursor-Einstellungen öffnen

`Cmd/Ctrl + ,` -> Suche nach "OpenAI" -> Finde "OpenAI API Key"

### 2. Konfiguration eintragen

- **API Key**: Dein Levolink API Key
- **Base URL**: `https://ai.levolink.com/v1`

### 3. ~/.cursor/settings.json anpassen

```json
{
  "openai.apiKey": "Dein Levolink API Key",
  "openai.baseUrl": "https://ai.levolink.com/v1",
  "openai.model": "gpt-5.6-sol"
}
```

### 4. Claude-Modelle verwenden

Gib in Cursors Modellauswahl einen benutzerdefinierten Modellnamen ein:
- `claude-sonnet-4-6` - Tägliche Programmierung
- `claude-opus-4-8` - Komplexe Aufgaben
- `gpt-5.6-sol` - GPT-Programmierung

## Empfohlene Konfiguration

| Verwendung | Modell | Gruppe |
|------|------|------|
| Code-Vervollständigung | gpt-5.6-luna | Codex Exklusiv (0.8x) |
| Konversation | claude-sonnet-4-6 | Standard (1.0x) |
| Komplexes Refactoring | claude-opus-4-8 | CC Exklusiv (2.4x) |
