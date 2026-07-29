# Guía de Integración con Grok Build

> Usa Levolink AI en Grok Build para invocar modelos como GPT/Claude/Gemini a través de intermediario.

## ¿Qué es Grok Build?

Grok Build es el asistente de programación con IA para terminal de xAI, que soporta TUI interactivo, modo headless y protocolo ACP. Mediante configuración personalizada de modelos, Grok Build puede invocar cualquier modelo disponible en Levolink AI.

## Pasos de Configuración

### 1. Instalar Grok Build

**macOS / Linux:**

```bash
curl -fsSL https://x.ai/cli/install.sh | bash

> ⚠️ Se recomienda revisar el script antes de instalar: curl -fsSL https://x.ai/cli/install.sh | less
```

**Windows (PowerShell):**

```powershell
irm https://x.ai/cli/install.ps1 | iex
```

### 2. Configurar Modelos Personalizados

Edita `~/.grok/config.toml` (Windows: `%USERPROFILE%\.grok\config.toml`):

```toml
# Usar Levolink AI como backend
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

### 3. Configurar API Key

```bash
export LEVOLINK_API_KEY="tu Levolink API Key"
```

### 4. Comenzar a Usar

```bash
cd your-project
grok
```

Usa `/model` en el TUI para cambiar de modelo:

```
/model levolink-claude
```

## Configuración de Modelos Recomendados

| Uso | Modelo | Grupo Recomendado |
|------|------|---------|
| Programación diaria | `gpt-5.6-luna` | Codex exclusivo (0.8x) |
| Programación compleja | `gpt-5.6-sol` | Codex exclusivo (0.8x) |
| Razonamiento profundo | `claude-opus-4-8` | Por defecto (1.0x) |
| Textos largos | `gemini-2.5-pro` | gemini-cli (1.0x) |

## Modo Headless

```bash
# Usar modelo de Levolink para ejecutar tareas
grok -p "Explain this codebase" -m levolink-claude

# Salida en formato JSON
grok -p "Analyze architecture" -m levolink-gpt --output-format streaming-json
```

## Preguntas Frecuentes

### P: Grok Build muestra "model not found" al iniciar

Ejecuta `grok inspect` para verificar que la configuración se haya cargado correctamente:

```bash
grok inspect
```

### P: ¿Cómo usar simultáneamente modelos de Grok y Levolink?

Añade tanto los modelos oficiales de xAI como los de Levolink en `config.toml`, y cambia entre ellos con el comando `/model`.

### P: ¿Soporta salida en streaming?

Sí. Todos los modelos de Levolink AI soportan salida en streaming.

## Enlaces Relacionados

- [Levolink AI - Sitio Oficial](https://ai.levolink.com)
- [Documentación Oficial de Grok Build](https://docs.x.ai/build/overview)
- [GitHub de Grok Build](https://github.com/xai-org/grok-build)
- [Documentación API](https://levolink.apifox.cn/)
