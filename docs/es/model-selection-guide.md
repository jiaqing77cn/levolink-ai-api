# Guía de Selección de Modelos

> ¿Cómo elegir entre 228 modelos? Esta guía te ayuda a encontrar el modelo más adecuado.

## Selección por Caso de Uso

### 🧑‍💻 Programación con IA

| Modelo | Precio de Entrada | Precio de Salida | Características |
|--------|-------------------|------------------|-----------------|
| `gpt-5.6-sol` | $4.00/M | $24.00/M | El mejor de GPT para programación, alta calidad de código |
| `gpt-5.6-luna` | $0.80/M | $4.80/M | Versión ligera, suficiente para programación diaria |
| `claude-sonnet-4-6` | $3.00/M | $15.00/M | Programación con Claude, fuerte comprensión de contexto |
| `claude-opus-4-8` | $5.00/M | $25.00/M | Refactorización compleja, diseño de arquitectura |
| `deepseek-reasoner` | $2.40/M | $9.60/M | Mejor relación calidad-precio, fuerte razonamiento |

### 📝 Procesamiento de Textos Largos

| Modelo | Longitud de Contexto | Precio de Entrada | Características |
|--------|---------------------|-------------------|-----------------|
| `claude-opus-4-8` | 200K | $5.00/M | Mejor comprensión de textos largos |
| `gemini-2.5-pro` | 1M | $1.25/M | Contexto ultralargo, el más económico |
| `gpt-5.6-sol` | 128K | $4.00/M | Capacidades generales sólidas |

### 🌐 Conversación Diaria

| Modelo | Precio de Entrada | Precio de Salida | Características |
|--------|-------------------|------------------|-----------------|
| `gpt-5.6-luna` | $0.80/M | $4.80/M | Económico y fácil de usar |
| `claude-sonnet-5` | $2.00/M | $10.00/M | Mejor relación calidad-precio de Claude |
| `gemini-2.5-flash` | $0.30/M | $2.50/M | El más barato |

### 🇨🇳 Escenarios en Chino

| Modelo | Precio de Entrada | Precio de Salida | Características |
|--------|-------------------|------------------|-----------------|
| `qwen3-max` | $2.50/M | $10.00/M | Mejor comprensión del chino |
| `glm-4.6` | $2.00/M | $8.00/M | De Zhipu, excelente en chino |
| `kimi-k2` | $4.00/M | $16.00/M | De Moonshot, bueno en textos largos |
| `doubao-seed-1-6` | $0.50/M | $2.00/M | De ByteDance, el más económico |

### 🎨 Generación de Imágenes

| Modelo | Precio | Características |
|--------|--------|-----------------|
| `gpt-image-2` | Pago por uso | Modelo de imágenes más reciente de OpenAI |
| `midjourney` | Pago por uso | Mejor estilo artístico |
| `flux-1.1-pro` | Pago por uso | Modelo de código abierto, rápido |

## Selección por Presupuesto

### Presupuesto mensual < $10

- Modelo principal: `gemini-2.5-flash` ($0.30/M de entrada)
- Programación: `gpt-5.6-luna` ($0.80/M de entrada)
- Grupo: Oferta especial (0.6x)

### Presupuesto mensual $10-$50

- Modelo principal: `claude-sonnet-4-6` ($3.00/M de entrada)
- Programación: `gpt-5.6-sol` ($4.00/M de entrada)
- Grupo: Codex exclusivo (0.8x) + Por defecto (1.0x)

### Presupuesto mensual $50+

- Modelo principal: `claude-opus-4-8` ($5.00/M de entrada)
- Programación: `claude-opus-4-8` + Claude Code
- Grupo: CC exclusivo (2.4x) o AWS nivel empresarial (4.0x)

## Tabla de Comparación de Precios

Para la lista completa de precios, consulta la [tabla de precios del README](../../README_ES.md#-precios-de-modelos-en-tiempo-real) o la [página de precios de Levolink AI](https://ai.levolink.com/pricing).
