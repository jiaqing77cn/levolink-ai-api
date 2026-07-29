<h1 align="center">🚀 Proxy de IA API en China | Claude/GPT/Gemini/DeepSeek sin VPN | Levolink AI</h1>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License"/>
  <img src="https://img.shields.io/badge/500%2B-Models-34d399?style=flat" alt="Models"/>
  <img src="https://img.shields.io/badge/CDN-China%20Accel-3b82f6?style=flat" alt="CDN"/>
  <img src="https://img.shields.io/badge/OpenAI-Compatible-10a37f?style=flat" alt="OpenAI Compatible"/>
</p>

<div align="center">

**Sin VPN · Baja Latencia · 500+ Modelos · OpenAI Compatible · Claude Code Ready**

[🌐 Sitio Web](https://ai.levolink.com) · [📋 Precios](https://ai.levolink.com/pricing) · [📖 Docs API](https://levolink.apifox.cn/) · [💬 Contacto](https://ai.levolink.com)

</div>

> Last updated: 2026-07-28 09:51 (UTC+8) | [中文](./README.md) | [English](./README_EN.md) | [한국어](./README_KO.md) | [日本語](./README_JA.md) | Español | [Deutsch](./README_DE.md)

---

## 📋 Tabla de Contenidos

- [🖥️ Vista previa del producto](#-vista-previa-del-producto)
- [🔍 Cómo elegir un proxy de API](#-cómo-elegir-un-proxy-de-api)
- [💰 Precios de modelos en tiempo real](#-precios-de-modelos-en-tiempo-real)
- [🛠️ Guía de integración](#-guía-de-integración)
- [📊 Comparación](#-comparación)
- [❓ Preguntas frecuentes](#-preguntas-frecuentes)
- [📖 Guías detalladas](#-guías-detalladas)
- [🤝 Contribuir](#-contribuir)

---

## 🖥️ Vista previa del producto

![Página principal de Levolink AI - panel de proxy de API con 500+ modelos de IA](https://raw.githubusercontent.com/jiaqing77cn/levolink-ai-api/main/assets/homepage.jpg)

![Panel de Levolink AI - crear claves API, ver uso, recargar cuenta](https://raw.githubusercontent.com/jiaqing77cn/levolink-ai-api/main/assets/console.jpg)

---

## 🔍 Cómo elegir un proxy de API

Seis dimensiones para evaluar al elegir un proxy de API de IA:

| Dimensión | Qué verificar | Señales de alerta |
|-----------|--------------|-----------|
| **Estabilidad** | ¿Caídas frecuentes? ¿Alta latencia? | Desconexiones, sin anuncios |
| **Velocidad** | ¿Es aceptable la latencia de respuesta? | >5s de retraso en el primer token |
| **Cobertura de modelos** | ¿Disponibles los modelos más recientes? | Lentitud para añadir nuevos modelos |
| **Transparencia de precios** | ¿Facturación clara? ¿Registros de uso? | Sin registros de llamadas, opaco |
| **Sustitución de modelos** | ¿Usa modelos baratos para hacerse pasar por premium? | Precios anormalmente bajos, mala calidad |
| **Riesgo de cierre** | ¿Operado por una empresa? ¿Tiene soporte? | Operador en solitario, sin servicio al cliente |

### ⚠️ Lista de trampas a evitar

1. **Trampa del precio de caché**: El precio normal de caché es 10%, algunos cobran 15%-30%
2. **Detección de sustitución de modelos**: Compara las respuestas entre el oficial y el proxy con los mismos prompts
3. **Fraude en conteo de tokens**: Envía solicitudes con cantidades de tokens conocidas, verifica si la facturación está inflada
4. **Trampa de precio bajo**: Precios muy por debajo del mercado probablemente significan GLM haciéndose pasar por GPT
5. **Riesgo de estafa de cierre**: ¡No recargues grandes cantidades! Paga sobre la marcha

### 🔬 Cómo detectar sustitución de modelos

```python
# Método 1: Prueba de capacidad - usa prompts de razonamiento
prompt = "A farmer has 17 sheep. All but 9 die. How many are left?"
# GPT/Claude respuesta correcta: 9
# Modelos de gama baja часто se equivocan: 8

# Método 2: Prueba de contexto largo
# Envía un texto largo de 50K+ tokens, pregunta sobre detalles al final
# Los modelos de gama baja pierden el contexto

# Método 3: Prueba de capacidad de código
prompt = "Implement an LRU cache with TTL expiration in Python"
# Compara la calidad del código entre el oficial y el proxy
```

---

## 💰 Precios de modelos en tiempo real

> Los precios se obtienen automáticamente desde [Levolink API](https://ai.levolink.com/api/pricing) mediante GitHub Actions, actualizados cada hora.
>
> Unidad: USD / Millón de Tokens | Relación Salida/Entrada = precio de salida ÷ precio de entrada

### Serie OpenAI GPT

<!-- GPT_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `gpt-5-codex` | enterprise-a… | 0.35x | $0.15 | $1.22 | Codex专属 | 0.8x | $0.35 | $2.80 | 8x |
| `gpt-5-mini` | enterprise-a… | 0.35x | $0.03 | $0.24 | 特供-优质gpt | 5.6x | $0.49 | $3.92 | 8x |
| `gpt-5-mini-2025-08-07` | enterprise-a… | 0.35x | $0.03 | $0.24 | 特供-优质gpt | 5.6x | $0.49 | $3.92 | 8x |
| `gpt-5-nano` | enterprise-a… | 0.35x | $0.01 | $0.05 | 特供-优质gpt | 5.6x | $0.10 | $0.78 | 8x |
| `gpt-5-nano-2025-08-07` | enterprise-a… | 0.35x | $0.01 | $0.05 | 特供-优质gpt | 5.6x | $0.10 | $0.78 | 8x |
| `gpt-5-pro` | enterprise-a… | 0.35x | $1.84 | $14.70 | 特供-优质gpt | 5.6x | $29.40 | $235.20 | 8x |
| `gpt-5.1-codex` | 特价9折 | 0.54x | $0.36 | $2.92 | Codex专属 | 0.8x | $0.54 | $4.32 | 8x |
| `gpt-5.1-codex-max` | 特价9折 | 0.54x | $0.36 | $2.92 | 纯AZ | 1.5x | $1.01 | $8.10 | 8x |
| `gpt-5.1-codex-mini` | enterprise-a… | 0.35x | $0.03 | $0.24 | 纯AZ | 1.5x | $0.13 | $1.05 | 8x |
| `gpt-5.2-chat` | enterprise-a… | 0.35x | $0.21 | $1.71 | 特供-优质gpt | 5.6x | $3.43 | $27.44 | 8x |
| `gpt-5.2-chat-latest` | enterprise-a… | 0.35x | $0.21 | $1.71 | 特供-优质gpt | 5.6x | $3.43 | $27.44 | 8x |
| `gpt-5.2-codex` | 特价9折 | 0.54x | $0.51 | $4.08 | 特供-优质gpt | 5.6x | $5.29 | $42.34 | 8x |
| `gpt-5.3-chat-latest` | enterprise-a… | 0.35x | $0.21 | $1.71 | 特供-优质gpt | 5.6x | $3.43 | $27.44 | 8x |
| `gpt-5.3-codex` | 特价9折 | 0.54x | $0.51 | $4.08 | 特供-优质gpt | 5.6x | $5.29 | $42.34 | 8x |
| `gpt-5.3-codex-spark` | Codex专属 | 0.8x | $1.12 | $8.96 | Premium OpenAI | 8x | $11.20 | $89.60 | 8x |

<!-- GPT_PRICE_TABLE_END -->

### Serie Anthropic Claude

<!-- CLAUDE_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `claude-fable-5` | default | 1x | $10.00 | $50.00 | Claude Code专… | 2.4x | $24.00 | $120.00 | 5x |
| `claude-haiku-4-5-20251001` | default | 1x | $1.00 | $5.00 | Claude Code专… | 2.4x | $2.40 | $12.00 | 5x |
| `claude-opus-4-1-20250805` | default | 1x | $15.00 | $75.00 | Claude Code专… | 2.4x | $36.00 | $180.00 | 5x |
| `claude-opus-4-5-20251101` | default | 1x | $5.00 | $25.00 | Claude Code专… | 2.4x | $12.00 | $60.00 | 5x |
| `claude-opus-4-6` | default | 1x | $5.00 | $25.00 | Claude Code专… | 2.4x | $12.00 | $60.00 | 5x |
| `claude-opus-4-7` | default | 1x | $5.00 | $25.00 | Claude Code专… | 2.4x | $12.00 | $60.00 | 5x |
| `claude-opus-4-8` | default | 1x | $5.00 | $25.00 | Claude Code专… | 2.4x | $12.00 | $60.00 | 5x |
| `claude-sonnet-4-20250514` | default | 1x | $3.00 | $15.00 | Claude Code专… | 2.4x | $7.20 | $36.00 | 5x |
| `claude-sonnet-4-5-20250929` | default | 1x | $3.00 | $15.00 | Claude Code专… | 2.4x | $7.20 | $36.00 | 5x |
| `claude-sonnet-4-6` | default | 1x | $3.00 | $15.00 | Claude Code专… | 2.4x | $7.20 | $36.00 | 5x |
| `claude-sonnet-5` | default | 1x | $2.00 | $10.00 | Claude Code专… | 2.4x | $4.80 | $24.00 | 5x |

<!-- CLAUDE_PRICE_TABLE_END -->

### Serie Google Gemini

<!-- GEMINI_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `gemini-2.0-flash-lite` | 官转gemini | 3.6x | $0.97 | $3.89 | Premium Gemini | 6x | $1.62 | $6.48 | 4x |
| `gemini-2.5-flash` | gemini-cli | 1x | $0.30 | $2.50 | Premium Gemini | 6x | $1.80 | $15.01 | 8.34x |
| `gemini-2.5-flash-image` | 优质gemini | 2.4x | $0.00 | $0.00 | Premium Gemini | 6x | $0.00 | $0.00 | 0x |
| `gemini-2.5-flash-lite` | gemini-cli | 1x | $0.10 | $0.40 | Premium Gemini | 6x | $0.60 | $2.40 | 4x |
| `gemini-2.5-pro` | gemini-cli | 1x | $1.25 | $10.00 | Premium Gemini | 6x | $7.50 | $60.00 | 8x |
| `gemini-3-pro-image` | 优质gemini | 2.4x | $0.00 | $0.00 | Premium Gemini | 6x | $0.00 | $0.00 | 0x |
| `gemini-3.1-flash-image` | 优质gemini | 2.4x | $0.00 | $0.00 | Premium Gemini | 6x | $0.00 | $0.00 | 0x |
| `gemini-3.1-flash-lite` | gemini-cli | 1x | $0.25 | $1.50 | Premium Gemini | 6x | $1.50 | $9.00 | 6x |

<!-- GEMINI_PRICE_TABLE_END -->

### Serie DeepSeek

<!-- DEEPSEEK_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `deepseek-r1` | uchat_qwen | 0.6x | $1.44 | $5.76 | 纯AZ | 1.5x | $3.60 | $14.40 | 4x |
| `deepseek-r1-0528` | uchat_qwen | 0.6x | $1.44 | $5.76 | 纯AZ | 1.5x | $3.60 | $14.40 | 4x |
| `deepseek-r1-2025-01-20` | uchat_qwen | 0.6x | $1.44 | $5.76 | 纯AZ | 1.5x | $3.60 | $14.40 | 4x |
| `deepseek-r1-250120` | uchat_qwen | 0.6x | $1.44 | $5.76 | 纯AZ | 1.5x | $3.60 | $14.40 | 4x |
| `deepseek-r1-250528` | uchat_qwen | 0.6x | $1.44 | $5.76 | 纯AZ | 1.5x | $3.60 | $14.40 | 4x |
| `deepseek-r1-distill-qwen-32b` | 特供-国产4折 | 0.8x | $1.28 | $3.84 | 纯AZ | 1.5x | $2.40 | $7.20 | 3x |
| `deepseek-r1-distill-qwen-7b` | 特供-国产4折 | 0.8x | $0.32 | $0.64 | 纯AZ | 1.5x | $0.60 | $1.20 | 2x |
| `deepseek-reasoner` | uchat_qwen | 0.6x | $1.44 | $5.76 | 纯AZ | 1.5x | $3.60 | $14.40 | 4x |

<!-- DEEPSEEK_PRICE_TABLE_END -->

### Modelos chinos (Qwen/Doubao/GLM/Kimi/MiniMax)

<!-- CN_MODEL_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `qwen3-max` | 限时特价 | 0.6x | $0.90 | $3.60 | 纯AZ | 1.5x | $2.25 | $9.00 | 4x |
| `qwen3-max-2026-01-23` | 阿里4折 | 0.8x | $1.60 | $6.40 | 纯AZ | 1.5x | $3.00 | $12.00 | 4x |
| `qwen3-coder` | 特供-国产4折 | 0.8x | $3.84 | $15.36 | 纯AZ | 1.5x | $7.20 | $28.80 | 4x |
| `qwen3-coder-plus` | 限时特价 | 0.6x | $1.44 | $5.76 | 特供-HC1 | 1.32x | $3.17 | $12.67 | 4x |
| `qwen3.6-plus` | default | 1x | $2.00 | $12.00 | 纯AZ | 1.5x | $3.00 | $18.00 | 6x |
| `qwen3.7-max` | 限时特价 | 0.6x | $4.32 | $12.96 | 纯AZ | 1.5x | $10.80 | $32.40 | 3x |
| `glm-4.6` | 限时特价 | 0.6x | $0.72 | $2.88 | 纯AZ | 1.5x | $1.80 | $7.20 | 4x |
| `glm-4.5` | 限时特价 | 0.6x | $0.58 | $2.30 | 纯AZ | 1.5x | $1.44 | $5.76 | 4x |
| `glm-4.5-air` | 限时特价 | 0.6x | $0.29 | $2.16 | 纯AZ | 1.5x | $0.72 | $5.40 | 7.5x |
| `kimi-k2` | enterprise-a… | 0.45x | $0.81 | $3.24 | 特供-优质gpt | 5.6x | $10.08 | $40.32 | 4x |
| `kimi-k2.5` | 特供-国产4折 | 0.8x | $2.56 | $13.44 | 纯AZ | 1.5x | $4.80 | $25.20 | 5.25x |
| `kimi-k3` | 纯AZ | 1.5x | $45.00 | $225.00 | 官转 | 3x | $90.00 | $450.00 | 5x |

<!-- CN_MODEL_PRICE_TABLE_END -->

> 💡 Precios completos con los 33 grupos y 228 modelos en [Levolink AI Pricing](https://ai.levolink.com/pricing)

### Niveles de grupos

| Tipo de grupo | Ratio | Mejor para |
|------------|-------|----------|
| Oferta flash | 0.6x | Pruebas, uso de bajo costo |
| Codex Exclusive | 0.8x | Programación con GPT, uso diario |
| Default | 1.0x | Calidad estándar, equilibrado |
| anti/kiro | 1.2x | Claude económico |
| Claude Code Exclusive | 2.4x | Programación con Claude Code |
| Canal Azure | 3.0x | GPT estable |
| AWS Enterprise | 4.0x | Claude de nivel empresarial |
| Vertex/Direct | 6.0x | Máxima calidad |
| Official Premium | 16.0x | Calidad oficial completa |

---

## 🛠️ Guía de integración

### Inicio rápido

1. Visita [Levolink AI](https://ai.levolink.com) -> Regístrate -> Consola -> Crear Key
2. Recarga (mínimo 1 yuan)
3. Elige tu método de integración:

### Python (OpenAI SDK)

```python
from openai import OpenAI

client = OpenAI(
    api_key="***",
    base_url="https://ai.levolink.com/v1"
)

# GPT-5.6 Sol
resp = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": "Write a Python quicksort"}]
)

# Claude Sonnet 4.6
resp = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": "Explain quantum computing"}],
    extra_body={"anthropic_version": "vertex-2023-10-01"}
)

# DeepSeek R1
resp = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[{"role": "user", "content": "Implement a web server in Python"}]
)
```

### Node.js / curl

```bash
curl https://ai.levolink.com/v1/chat/completions \
  -H "Authorization: Bearer ***" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.6-sol",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

Ejemplos completos en el directorio [`examples/`](./examples/) (incluye [Python](examples/quickstart.py) / [Node.js](examples/quickstart.js) / [Shell](examples/quickstart.sh)).

### Claude Code

```bash
npm install -g @anthropic-ai/claude-code

echo 'export ANTHROPIC_AUTH_TOKEN="***"' >> ~/.bash_profile
echo 'export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"' >> ~/.bash_profile
source ~/.bash_profile

cd your-project && claude
```

📖 Guía completa: [Configuración de Claude Code](docs/claude-code-guide.md)

### OpenAI Codex

```bash
npm install -g @openai/codex
export OPENAI_API_KEY="***"
export OPENAI_API_BASE="https://ai.levolink.com/v1"
```

📖 Guía completa: [Configuración de Codex](docs/codex-setup.md)

### Gemini CLI

```bash
npm install -g @google/gemini-cli
export GEMINI_API_KEY="***"
export GEMINI_API_BASE="https://ai.levolink.com/v1"
```

📖 Guía completa: [Configuración de Cursor IDE](docs/cursor-setup.md) (también aplica para Gemini CLI)

### Integraciones con herramientas

| Herramienta | Configuración |
|------|-------|
| **Dify / FastGPT** | API Key + Base URL: `https://ai.levolink.com/v1` |
| **n8n** | HTTP Request -> URL: `https://ai.levolink.com/v1/chat/completions` |
| **LangChain** | `ChatOpenAI(openai_api_key="key", openai_api_base="https://ai.levolink.com/v1")` |
| **NextChat** | Ajustes -> API personalizada -> URL: `https://ai.levolink.com/v1` |
| **Cursor IDE** | Ajustes -> Variables de entorno -> `ANTHROPIC_BASE_URL=https://ai.levolink.com/v1` |
| **OpenClaw** | `openai_api_key: key` + `openai_api_base: https://ai.levolink.com/v1` |

### Casos de uso

- **Programación con IA** - Claude Code / Codex con Claude 4.8 / GPT-5.6 para refactoring, corrección de bugs
- **Procesamiento de documentos largos** - Análisis de 100K+ palabras, revisión de contratos, resumen de papers
- **Agentes de IA** - Una clave para todos los modelos, tareas multi-agente en paralelo
- **Bases de conocimiento RAG** - DeepSeek / GPT con bases de datos vectoriales para Q&A empresarial
- **Flujos de trabajo automatizados** - Integración con n8n / FastGPT / Dify para automatización completa

---

## 📊 Comparativa 2026

| | [Levolink AI](https://ai.levolink.com) | SiliconFlow | Otros proxies | Autoconstruido |
|--|-------------|-------------|---------------|------------|
| Número de modelos | **500+** | ~200 | ~100 | Manual |
| Opciones de grupos | **33 grupos** | Ninguna | 1-3 | - |
| CDN en China | ✅ Multi-nodo | ✅ Único | ✅ | ❌ |
| Recarga mínima | **1 yuan** | 50 yuan | 20 yuan | - |
| Pago por uso | ✅ | ✅ | ✅ | ❌ |
| Claude Code ready | ✅ | ✅ | ✅ | ❌ |
| OpenAI compatible | ✅ | ✅ | ✅ | Necesita adaptador |
| Transparencia de precios | ✅ 33 grupos | Precio único | Precio único | - |
| Factura | ✅ | ✅ | ❌ | - |
| Código abierto en GitHub | ✅ Precios automáticos | ❌ | ❌ | - |

---

## ❓ Preguntas frecuentes

**¿Las respuestas son idénticas a las de la API oficial?**

Sí. Levolink AI solo reenvía las solicitudes a los modelos oficiales: las respuestas son idénticas byte a byte.

**¿Mi cuenta puede ser baneada?**

No. Usas la clave de Levolink AI, no el sistema de cuentas oficial, sin riesgo de baneo.

**¿Cuál es la diferencia entre los grupos?**

Los diferentes grupos corresponden a diferentes canales de backend (Azure/AWS/Vertex/Official Direct, etc.) con calidad y precio variables. Los grupos más económicos ofrecen mejor relación calidad-precio; los grupos más caros ofrecen máxima estabilidad. Comienza con el grupo default y ajusta según sea necesario.

**¿Es compatible con streaming?**

Sí, todos los modelos soportan `stream: true` con baja latencia.

**¿Qué tan rápido es desde China?**

Nodos CDN en China, latencia típicamente de 40-200ms, mucho más rápido que conectarse directamente a las APIs oficiales.

**¿Hay una capa gratuita?**

Los nuevos usuarios reciben créditos de prueba. Empieza gratis, recarga cuando quieras.

**¿Puedo obtener factura?**

Sí. Ajustes -> Verificación de identidad -> Billetera -> Factura. Factura electrónica emitida en un plazo de 5 días hábiles.

**¿Qué grupo debería elegir?**

- Económico: Oferta flash (0.6x) / Codex Exclusive (0.8x)
- Equilibrado: Default (1.0x)
- Alta calidad: Claude Code Exclusive (2.4x) / Azure (3.0x)
- Máxima calidad: Vertex (6.0x) / Official Premium (16.0x)

---

## 📖 Guías detalladas

| Guía | Contenido |
|-------|---------|
| [Guía de configuración de Claude Code](docs/claude-code-guide.md) | Configuración completa de Claude Code para China |
| [Configuración de Cursor IDE](docs/cursor-setup.md) | Usar GPT-5.6 / Claude 4.8 / Gemini en Cursor |
| [Guía de selección de modelos](docs/model-selection-guide.md) | ¿Cuál de los 228 modelos elegir? Por caso de uso y presupuesto |
| [Guía de detección de fraude](docs/fraud-detection-guide.md) | 5 métodos para detectar sustitución de modelos en proxies de API |
| [Guía de configuración de Codex](docs/codex-setup.md) | Configuración de OpenAI Codex CLI para China |
| [Guía de integración con Dify](docs/dify-integration.md) | Conectar Dify con Levolink AI |
| [Guía de calculadora de costos](docs/cost-calculator-guide.md) | Estima costos de API y optimiza el gasto |

---

## 🤝 Contribuir

- 🐛 Reportar bug -> [Abrir un Issue](https://github.com/jiaqing77cn/levolink-ai-api/issues)
- 📝 Mejorar docs -> Enviar un PR
- 💡 Solicitud de función -> [Iniciar una Discussion](https://github.com/jiaqing77cn/levolink-ai-api/discussions)
- 📄 Guía de contribución -> Ver [CONTRIBUTING.md](./CONTRIBUTING.md)
- 📋 Registro de cambios -> Ver [CHANGELOG.md](./CHANGELOG.md)

---

## 📜 Licencia

MIT License · Copyright (c) 2026 [Levolink AI](https://ai.levolink.com)
