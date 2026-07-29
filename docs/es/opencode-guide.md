# Guía de Integración con OpenCode

> Usa Levolink AI en OpenCode para acceder a más de 500 modelos de IA, sin necesidad de VPN.

## ¿Qué es OpenCode?

OpenCode es un asistente de programación con IA de código abierto (180K+ Stars), que soporta terminal, escritorio y plugin de IDE. Mediante la configuración de un endpoint compatible con OpenAI, se puede integrar Levolink AI.

## Pasos de Configuración

### 1. Instalar OpenCode

```bash
# Método de instalación recomendado
curl -fsSL https://opencode.ai/install | bash

# O a través de npm
npm install -g opencode-ai
```

### 2. Configurar Levolink AI como Provider

Crea un archivo `opencode.json` en el directorio raíz del proyecto:

```json
{
  "provider": {
    "levolink": {
      "name": "Levolink AI",
      "api_key": "tu Levolink API Key",
      "base_url": "https://ai.levolink.com/v1",
      "models": {
        "gpt-5.6-sol": { "name": "GPT-5.6 Sol" },
        "claude-sonnet-4-6": { "name": "Claude Sonnet 4.6" },
        "gemini-2.5-pro": { "name": "Gemini 2.5 Pro" },
        "deepseek-reasoner": { "name": "DeepSeek R1" }
      }
    }
  },
  "model": "levolink/gpt-5.6-sol"
}
```

### 3. O Configurar a través del TUI

```bash
cd your-project
opencode
```

Ejecuta en el TUI de OpenCode:

```
/connect
```

Selecciona "Custom OpenAI Compatible" e introduce:
- **API Key**: tu Levolink API Key
- **Base URL**: `https://ai.levolink.com/v1`

### 4. Inicializar Proyecto

```
/init
```

OpenCode analizará la estructura del proyecto y generará un archivo `AGENTS.md`.

## Modelos Recomendados

| Uso | Modelo | Grupo Recomendado |
|------|------|---------|
| Programación diaria | `gpt-5.6-luna` | Codex exclusivo (0.8x) |
| Programación compleja | `claude-sonnet-4-6` | Por defecto (1.0x) |
| Razonamiento profundo | `claude-opus-4-8` | Por defecto (1.0x) |
| Textos largos | `gemini-2.5-pro` | gemini-cli (1.0x) |
| Relación calidad-precio | `deepseek-reasoner` | Oferta especial (0.6x) |

## Ejemplos de Uso

```
# Modo Plan (presiona Tab para cambiar)
> Refactoriza la lógica de autenticación en src/api/index.ts

# Modo Build
> Ejecuta los cambios según el plan

# Deshacer cambios
/undo
```

## Preguntas Frecuentes

### P: OpenCode muestra el error "provider not found"

Verifica que `opencode.json` esté en el directorio raíz del proyecto y que el formato JSON sea correcto.

### P: ¿Cómo cambiar de modelo?

Escribe `/model levolink/claude-sonnet-4-6` en el TUI para cambiar de modelo.

### P: ¿Soporta el modo Plan?

Sí. Presiona la tecla `Tab` para alternar entre los modos Build y Plan.

### P: ¿Cómo configurar múltiples Providers?

Añade múltiples providers en `opencode.json` y cambia entre ellos con `/model provider/model`.

## Enlaces Relacionados

- [Levolink AI - Sitio Oficial](https://ai.levolink.com)
- [Documentación Oficial de OpenCode](https://opencode.ai/docs/)
- [Documentación API](https://levolink.apifox.cn/)
- [Guía de Selección de Modelos](./model-selection-guide.md)
