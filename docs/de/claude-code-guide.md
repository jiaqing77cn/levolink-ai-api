# Claude Code Anleitung

> Die beste Lösung für die Nutzung von Claude Code in China, ohne VPN, mit geringer Latenz.

## Was ist Claude Code

Claude Code ist der offizielle KI-Programmierassistent von Anthropic, der direkt im Terminal verwendet werden kann und Code-Generierung, Refactoring, Bug-Fixing und Test-Erstellung unterstützt.

## Konfigurationsschritte

### 1. Claude Code installieren

```bash
npm install -g @anthropic-ai/claude-code
```

### 2. Umgebungsvariablen konfigurieren

```bash
# Zur ~/.bash_profile oder ~/.zshrc hinzufügen
export ANTHROPIC_AUTH_TOKEN="Dein Levolink API Key"
export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"

# Aktivieren
source ~/.bash_profile
```

### 3. Mit der Nutzung beginnen

```bash
cd your-project
claude
```

## Empfohlene Gruppen

| Gruppe | Multiplikator | Anwendungsbereich |
|------|------|---------|
| Standard (Azure+MJ) | 1.0x | Tägliche Nutzung, hohes Preis-Leistungs-Verhältnis |
| CC Exklusiv | 2.4x | Speziell für Claude Code optimiert, höchste Stabilität |
| anti/kiro | 1.2x | Preis-Leistungs-Sieger |

## Häufige Fragen

### F: Claude Code meldet "authentication failed"

Überprüfe, ob die Umgebungsvariablen korrekt gesetzt sind:
```bash
echo $ANTHROPIC_AUTH_TOKEN
echo $ANTHROPIC_BASE_URL
```

### F: Die Antwortgeschwindigkeit ist langsam

Versuche, die Gruppe zu wechseln. Die CC-exklusive Gruppe ist speziell für Claude Code optimiert und schneller.

### F: Wird Claude Opus 4.8 unterstützt?

Ja. Gib in Claude Code `/model` ein, um das Modell zu wechseln.

## Verwandte Links

- [Levolink AI Webseite](https://ai.levolink.com)
- [Claude Code offizielle Dokumentation](https://docs.anthropic.com/en/docs/claude-code)
- [API Dokumentation](https://levolink.apifox.cn/)
