# Guía de Uso de la Calculadora de Costos

> Estima los costos de tus llamadas a la API de IA y elige la combinación de modelo y grupo más económica.

## Estimación Rápida de Costos

### Conceptos Básicos

| Término | Significado |
|---------|-------------|
| Token de Entrada | El texto que envías al modelo (incluyendo system prompt, contexto) |
| Token de Salida | El texto que devuelve el modelo |
| Multiplicador | Coeficiente de precio del grupo, cuanto más bajo más barato |
| Ratio Salida/Entrada | Precio de salida / precio de entrada (normalmente 3-8x) |

### Tokens Aproximados por Conversación

| Escenario | Tokens de Entrada | Tokens de Salida |
|-----------|-------------------|------------------|
| Pregunta-respuesta simple | 50-200 | 100-500 |
| Generación de código | 200-1000 | 500-2000 |
| Análisis de texto largo | 5000-50000 | 500-2000 |
| Programación con Claude Code | 5000-30000 | 2000-10000 |

## Estimación de Costo Mensual por Escenario

### Escenario 1: Conversación Diaria con IA (Uso Ligero)

- Promedio de 20 conversaciones por día
- Aprox. 500 entrada + 500 salida = 1000 tokens por conversación
- Uso mensual: aprox. 600.000 tokens (300.000 entrada + 300.000 salida)

| Modelo | Grupo | Costo Mensual |
|--------|-------|---------------|
| `gpt-5.6-luna` | Oferta especial (0.6x) | ~$0.36 |
| `gemini-2.5-flash` | Gemini-CLI mixto (1.0x) | ~$0.90 |
| `claude-sonnet-5` | Por defecto (1.0x) | ~$3.60 |

### Escenario 2: Asistente de Programación con IA (Uso Moderado)

- Promedio de 50 peticiones de código por día
- Aprox. 5000 entrada + 2000 salida = 7000 tokens por petición
- Uso mensual: aprox. 10,5 millones de tokens (7,5M entrada + 3M salida)

| Modelo | Grupo | Costo Mensual |
|--------|-------|---------------|
| `gpt-5.6-luna` | Codex exclusivo (0.8x) | ~$9.12 |
| `gpt-5.6-sol` | Codex exclusivo (0.8x) | ~$45.60 |
| `claude-sonnet-4-6` | Por defecto (1.0x) | ~$67.50 |
| `claude-opus-4-8` | Por defecto (1.0x) | ~$112.50 |

### Escenario 3: Programación Intensiva con Claude Code

- Promedio de 100 peticiones por día
- Aprox. 15000 entrada + 5000 salida = 20000 tokens por petición
- Uso mensual: aprox. 60 millones de tokens (45M entrada + 15M salida)

| Modelo | Grupo | Costo Mensual |
|--------|-------|---------------|
| `claude-sonnet-4-6` | Por defecto (1.0x) | ~$360 |
| `claude-sonnet-4-6` | CC exclusivo (2.4x) | ~$864 |
| `claude-opus-4-8` | Por defecto (1.0x) | ~$600 |
| `gpt-5.6-sol` | Codex exclusivo (0.8x) | ~$228 |

### Escenario 4: Procesamiento de Textos Largos

- Promedio de 10 análisis de documentos por día
- Aprox. 50000 entrada + 1000 salida por análisis
- Uso mensual: aprox. 15,3 millones de tokens (15M entrada + 300K salida)

| Modelo | Grupo | Costo Mensual |
|--------|-------|---------------|
| `gemini-2.5-pro` | Gemini-CLI mixto (1.0x) | ~$19.13 |
| `claude-opus-4-8` | Por defecto (1.0x) | ~$82.50 |
| `gpt-5.6-sol` | Codex exclusivo (0.8x) | ~$50.40 |

## Estrategias de Ahorro

### 1. Selección de Grupo

| Estrategia | Grupo | Multiplicador | Adecuado para |
|------------|-------|---------------|---------------|
| Máximo ahorro | Oferta especial | 0.6x | Pruebas, tareas no críticas |
| Mejor relación calidad-precio | Codex exclusivo | 0.8x | Programación diaria |
| Equilibrado | Por defecto | 1.0x | Entorno de producción |
| Alta estabilidad | CC exclusivo | 2.4x | Programación con Claude Code |

### 2. Combinación de Modelos

No uses solo un modelo. Estrategia recomendada:
- **Tareas simples** (traducción, resumen): Gemini 2.5 Flash ($0.30/M de entrada)
- **Programación diaria**: GPT-5.6 Luna ($0.80/M de entrada)
- **Programación compleja**: Claude Sonnet 4.6 o GPT-5.6 Sol
- **Textos ultralargos**: Gemini 2.5 Pro (contexto de 1M, $1.25/M de entrada)

### 3. Aprovechamiento de Caché

Levolink soporta precios con caché (estándar 10%). Para escenarios con contexto repetido (como Claude Code), la caché puede reducir significativamente los costos.

### 4. Establecer Límites de Tokens

Configura límites de max_tokens en la capa de aplicación para evitar gastos inesperados.

## Uso del Script Calculadora de Precios

El repositorio incluye un script calculadora de precios:

```bash
cd levolink-ai-api
python scripts/cost_calculator.py
```

Introduce tu uso estimado y calculará automáticamente el costo mensual para cada combinación de modelo/grupo.

## Enlaces Relacionados

- [Lista Completa de Precios](../../README_ES.md#-precios-de-modelos-en-tiempo-real)
- [Guía de Selección de Modelos](./model-selection-guide.md)
- [Página de Precios de Levolink AI](https://ai.levolink.com/pricing)
