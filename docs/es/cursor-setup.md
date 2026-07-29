# Guía de Configuración de Cursor IDE

> Usar Levolink AI en Cursor IDE para llamar a GPT-5.6 / Claude 4.8 / Gemini 3.5.

## Pasos de Configuración

### 1. Abrir la Configuración de Cursor

`Cmd/Ctrl + ,` -> Buscar "OpenAI" -> Encontrar "OpenAI API Key"

### 2. Ingresar la Configuración

- **API Key**: Tu Levolink API Key
- **Base URL**: `https://ai.levolink.com/v1`

### 3. Modificar ~/.cursor/settings.json

```json
{
  "openai.apiKey": "Tu Levolink API Key",
  "openai.baseUrl": "https://ai.levolink.com/v1",
  "openai.model": "gpt-5.6-sol"
}
```

### 4. Usar Modelos Claude

En el selector de modelos de Cursor, introduce el nombre del modelo personalizado:
- `claude-sonnet-4-6` - Programación diaria
- `claude-opus-4-8` - Tareas complejas
- `gpt-5.6-sol` - Programación con GPT

## Configuración Recomendada

| Uso | Modelo | Grupo |
|-----|--------|-------|
| Autocompletado de código | gpt-5.6-luna | Codex exclusivo (0.8x) |
| Conversación | claude-sonnet-4-6 | Por defecto (1.0x) |
| Refactorización compleja | claude-opus-4-8 | CC exclusivo (2.4x) |
