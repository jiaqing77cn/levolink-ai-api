# Guía de Integración con CC Switch

> Usa CC Switch para gestionar centralmente las configuraciones de Levolink AI para Claude Code, Codex, Gemini CLI, OpenCode, OpenClaw y otras herramientas.

## ¿Qué es CC Switch?

CC Switch es una herramienta de escritorio multiplataforma para gestionar centralmente las configuraciones de API de múltiples herramientas de programación con IA. Soporta Claude Code, Claude Desktop, Codex, Gemini CLI, Grok Build, OpenCode, OpenClaw y Hermes, permitiendo cambiar de Provider con un solo clic sin necesidad de editar archivos de configuración manualmente.

## Instalación

### macOS

```bash
# Homebrew
brew install --cask cc-switch
```

### Windows

Descarga el instalador desde [ccswitch.io](https://ccswitch.io).

### Linux

Descarga el AppImage desde [GitHub Releases](https://github.com/farion1231/cc-switch/releases).

## Configurar Levolink AI

### 1. Añadir Provider

Abre CC Switch -> Haz clic en「Añadir Provider」-> Selecciona「Personalizado」:

| Campo | Valor |
|--------|-----|
| Nombre | Levolink AI |
| API Key | tu Levolink API Key |
| Base URL | `https://ai.levolink.com/v1` |
| Formato | OpenAI Compatible |

### 2. Configurar cada Herramienta

CC Switch generará automáticamente la configuración para cada herramienta:

**Claude Code:**
```bash
export ANTHROPIC_AUTH_TOKEN="tuKey"
export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"
```

**Codex:**
```bash
export OPENAI_API_KEY="tuKey"
export OPENAI_API_BASE="https://ai.levolink.com/v1"
```

**Gemini CLI:**
```bash
export GEMINI_API_KEY="tuKey"
export GEMINI_API_BASE="https://ai.levolink.com/v1"
```

**OpenCode:**
```json
{
  "provider": {
    "levolink": {
      "api_key": "tuKey",
      "base_url": "https://ai.levolink.com/v1"
    }
  }
}
```

### 3. Cambio con un Solo Clic

Selecciona la herramienta objetivo en la interfaz de CC Switch -> Selecciona「Levolink AI」-> Haz clic en「Aplicar」. CC Switch modificará automáticamente el archivo de configuración de la herramienta correspondiente.

## Configuración Recomendada

| Herramienta | Modelo Recomendado | Grupo |
|------|---------|------|
| Claude Code | `claude-sonnet-4-6` | Por defecto (1.0x) |
| Codex | `gpt-5.6-sol` | Codex exclusivo (0.8x) |
| Gemini CLI | `gemini-2.5-pro` | gemini-cli (1.0x) |
| OpenCode | `gpt-5.6-luna` | Codex exclusivo (0.8x) |
| OpenClaw | `claude-opus-4-8` | Por defecto (1.0x) |

## Gestión de Múltiples Providers

CC Switch permite configurar múltiples Providers simultáneamente, facilitando pruebas comparativas:

1. Añadir「Levolink AI - Oferta especial」(0.6x)
2. Añadir「Levolink AI - Por defecto」(1.0x)
3. Añadir「Levolink AI - CC exclusivo」(2.4x)

Cambia con un solo clic en la interfaz, sin necesidad de modificar código o variables de entorno.

## Preguntas Frecuentes

### P: La herramienta no refleja los cambios después de modificar la configuración en CC Switch

Asegúrate de cerrar completamente la herramienta objetivo y reiniciarla. Claude Code necesita volver a aplicar las variables de entorno con `source`.

### P: ¿Permite configurar diferentes Providers para diferentes herramientas simultáneamente?

Sí. CC Switch puede configurar de forma independiente el Provider y el modelo para cada herramienta.

### P: ¿CC Switch es gratuito?

CC Switch es una herramienta de código abierto, gratuita de usar.

## Enlaces Relacionados

- [Levolink AI - Sitio Oficial](https://ai.levolink.com)
- [Sitio Oficial de CC Switch](https://ccswitch.io)
- [GitHub de CC Switch](https://github.com/farion1231/cc-switch)
- [Documentación API](https://levolink.apifox.cn/)
