# Gemini CLI Integrationsanleitung

> Verwenden Sie Levolink AI in Gemini CLI, um Modelle wie Gemini 3.5 Pro / Flash ohne VPN aufzurufen.

## Was ist Gemini CLI?

Gemini CLI ist der von Google entwickelte Terminal-AI-Assistent und unterstützt Codegenerierung, Dokumentanalyse, Aufgabenautomatisierung und mehr. Über den Levolink AI-Proxy können Nutzer aus China die Gemini-Modellreihe direkt verwenden.

## Konfigurationsschritte

### 1. Gemini CLI installieren

```bash
npm install -g @google/gemini-cli
```

### 2. Umgebungsvariablen konfigurieren

```bash
# Zu ~/.bash_profile oder ~/.zshrc hinzufügen
export GEMINI_API_KEY="Ihr Levolink API Key"
export GEMINI_API_BASE="https://ai.levolink.com/v1"

# Aktivieren
source ~/.bash_profile
```

### 3. Verwendung starten

```bash
cd your-project
gemini
```

## Empfohlene Modelle und Gruppen

| Verwendungszweck | Modell | Gruppe | Faktor |
|------|------|------|------|
| Tägliche Nutzung | `gemini-2.5-flash` | gemini-cli | 1.0x |
| Leichte Aufgaben | `gemini-2.5-flash-lite` | gemini-cli | 1.0x |
| Komplexe Aufgaben | `gemini-2.5-pro` | gemini-cli | 1.0x |
| Bildgenerierung | `gemini-3-pro-image` | 优质gemini | 2.4x |

## Modell angeben

```bash
# Bestimmtes Modell verwenden
gemini --model gemini-2.5-pro

# Oder im interaktiven Modus wechseln
> /model gemini-2.5-flash
```

## Windows-Konfiguration

```powershell
$env:GEMINI_API_KEY="Ihr Levolink API Key"
$env:GEMINI_API_BASE="https://ai.levolink.com/v1"
gemini
```

Dauerhaft setzen:

```powershell
[System.Environment]::SetEnvironmentVariable("GEMINI_API_KEY", "IhrKey", "User")
[System.Environment]::SetEnvironmentVariable("GEMINI_API_BASE", "https://ai.levolink.com/v1", "User")
```

## Häufig gestellte Fragen

### F: Gemini CLI meldet "Invalid API key"

Überprüfen Sie, ob die Umgebungsvariablen korrekt gesetzt sind:

```bash
echo $GEMINI_API_KEY
echo $GEMINI_API_BASE
# Stellen Sie sicher, dass die Base URL mit /v1 endet
```

### F: Antwortgeschwindigkeit ist langsam

Die Gemini-CLI-Gruppe (1.0x Faktor) ist für Gemini-Modelle optimiert und bietet eine höhere Geschwindigkeit.

### F: Wird Gemini 3.5 Pro unterstützt?

Ja. Verwenden Sie `--model gemini-3-pro-image` oder wechseln Sie im interaktiven Modus.

## Verwandte Links

- [Levolink AI Webseite](https://ai.levolink.com)
- [Gemini CLI offizielle Dokumentation](https://github.com/google-gemini/gemini-cli)
- [API Dokumentation](https://levolink.apifox.cn/)
- [Modell-Auswahlleitfaden](./model-selection-guide.md)
