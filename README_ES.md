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

> Last updated: 2026-08-08 15:02 (UTC+8)| [中文](./README.md) | [English](./README_EN.md) | [한국어](./README_KO.md) | [日本語](./README_JA.md) | Español | [Deutsch](./README_DE.md)

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
# Modelos de gama baja a menudo se equivocan: 8

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
| `gpt-5-codex` | Enterprise Azure 2 | 0.35x | $0.44 | $3.50 | Codex Exclusive | 0.8x | $1.00 | $8.00 | 8x |
| `gpt-5-mini` | Enterprise Azure 2 | 0.35x | $0.09 | $0.70 | Special-Premium GPT | 5.6x | $1.40 | $11.20 | 8x |
| `gpt-5-mini-2025-08-07` | Enterprise Azure 2 | 0.35x | $0.09 | $0.70 | Special-Premium GPT | 5.6x | $1.40 | $11.20 | 8x |
| `gpt-5-nano` | Enterprise Azure 2 | 0.35x | $0.02 | $0.14 | Special-Premium GPT | 5.6x | $0.28 | $2.24 | 8x |
| `gpt-5-nano-2025-08-07` | Enterprise Azure 2 | 0.35x | $0.02 | $0.14 | Special-Premium GPT | 5.6x | $0.28 | $2.24 | 8x |
| `gpt-5-pro` | Enterprise Azure 2 | 0.35x | $5.25 | $42.00 | Special-Premium GPT | 5.6x | $84.00 | $672.00 | 8x |
| `gpt-5.1-codex` | Sale 10% Off | 0.54x | $0.68 | $5.40 | Codex Exclusive | 0.8x | $1.00 | $8.00 | 8x |
| `gpt-5.1-codex-max` | Sale 10% Off | 0.54x | $0.68 | $5.40 | Pure Azure | 1.5x | $1.88 | $15.00 | 8x |
| `gpt-5.1-codex-mini` | Sale 10% Off | 0.54x | $0.14 | $1.08 | Pure Azure | 1.5x | $0.38 | $3.00 | 8x |
| `gpt-5.2-chat` | Enterprise Azure 2 | 0.35x | $0.61 | $4.90 | Special-Premium GPT | 5.6x | $9.80 | $78.40 | 8x |
| `gpt-5.2-chat-latest` | Enterprise Azure 2 | 0.35x | $0.61 | $4.90 | Special-Premium GPT | 5.6x | $9.80 | $78.40 | 8x |
| `gpt-5.2-codex` | Sale 10% Off | 0.54x | $0.95 | $7.56 | Special-Premium GPT | 5.6x | $9.80 | $78.40 | 8x |
| `gpt-5.3-chat-latest` | Enterprise Azure 2 | 0.35x | $0.61 | $4.90 | Special-Premium GPT | 5.6x | $9.80 | $78.40 | 8x |
| `gpt-5.3-codex` | Sale 10% Off | 0.54x | $0.95 | $7.56 | Special-Premium GPT | 5.6x | $9.80 | $78.40 | 8x |
| `gpt-5.3-codex-spark` | Codex Exclusive | 0.8x | $1.40 | $11.20 | Premium OpenAI | 8x | $14.00 | $112.00 | 8x |

<!-- GPT_PRICE_TABLE_END -->

### Serie Anthropic Claude

<!-- CLAUDE_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `claude-fable-5` | Default | 1x | $10.00 | $50.00 | Claude Code Exclusive | 2.4x | $24.00 | $120.00 | 5x |
| `claude-haiku-4-5-20251001` | Default | 1x | $1.00 | $5.00 | Claude Code Exclusive | 2.4x | $2.40 | $12.00 | 5x |
| `claude-opus-4-1-20250805` | Default | 1x | $15.00 | $75.00 | Relay Claude 1 | 4x | $60.00 | $300.00 | 5x |
| `claude-opus-4-5-20251101` | Default | 1x | $5.00 | $25.00 | Claude Code Exclusive | 2.4x | $12.00 | $60.00 | 5x |
| `claude-opus-4-6` | Default | 1x | $5.00 | $25.00 | Claude Code Exclusive | 2.4x | $12.00 | $60.00 | 5x |
| `claude-opus-4-7` | Default | 1x | $5.00 | $25.00 | Claude Code Exclusive | 2.4x | $12.00 | $60.00 | 5x |
| `claude-opus-4-8` | Default | 1x | $5.00 | $25.00 | Claude Code Exclusive | 2.4x | $12.00 | $60.00 | 5x |
| `claude-sonnet-4-20250514` | Default | 1x | $3.00 | $15.00 | Relay Claude 1 | 4x | $12.00 | $60.00 | 5x |
| `claude-sonnet-4-5-20250929` | Default | 1x | $3.00 | $15.00 | Claude Code Exclusive | 2.4x | $7.20 | $36.00 | 5x |
| `claude-sonnet-4-6` | Default | 1x | $3.00 | $15.00 | Claude Code Exclusive | 2.4x | $7.20 | $36.00 | 5x |
| `claude-sonnet-5` | Default | 1x | $2.00 | $10.00 | Claude Code Exclusive | 2.4x | $4.80 | $24.00 | 5x |

<!-- CLAUDE_PRICE_TABLE_END -->

### Serie Google Gemini

<!-- GEMINI_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `gemini-2.0-flash-lite` | Relay Gemini | 3.6x | $0.27 | $1.08 | Premium Gemini | 6x | $0.45 | $1.80 | 4x |
| `gemini-2.5-flash` | Gemini CLI | 1x | $0.30 | $2.50 | Premium Gemini | 6x | $1.80 | $15.01 | 8.34x |
| `gemini-2.5-flash-image` | Premium Gemini | 2.4x | $0.00 | $0.00 | Premium Gemini | 6x | $0.00 | $0.00 | 0x |
| `gemini-2.5-flash-lite` | Gemini CLI | 1x | $0.10 | $0.40 | Premium Gemini | 6x | $0.60 | $2.40 | 4x |
| `gemini-2.5-pro` | Gemini CLI | 1x | $1.25 | $10.00 | Premium Gemini | 6x | $7.50 | $60.00 | 8x |
| `gemini-3-pro-image` | Premium Gemini | 2.4x | $0.00 | $0.00 | Premium Gemini | 6x | $0.00 | $0.00 | 0x |
| `gemini-3.1-flash-image` | Premium Gemini | 2.4x | $0.00 | $0.00 | Premium Gemini | 6x | $0.00 | $0.00 | 0x |
| `gemini-3.1-flash-lite` | Gemini CLI | 1x | $0.25 | $1.50 | Premium Gemini | 6x | $1.50 | $9.00 | 6x |

<!-- GEMINI_PRICE_TABLE_END -->

### Serie DeepSeek

<!-- DEEPSEEK_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `deepseek-r1` | UChat Qwen | 0.6x | $2.40 | $9.60 | Pure Azure | 1.5x | $6.00 | $24.00 | 4x |
| `deepseek-r1-0528` | UChat Qwen | 0.6x | $2.40 | $9.60 | Pure Azure | 1.5x | $6.00 | $24.00 | 4x |
| `deepseek-r1-2025-01-20` | UChat Qwen | 0.6x | $2.40 | $9.60 | Pure Azure | 1.5x | $6.00 | $24.00 | 4x |
| `deepseek-r1-250120` | UChat Qwen | 0.6x | $2.40 | $9.60 | Pure Azure | 1.5x | $6.00 | $24.00 | 4x |
| `deepseek-r1-250528` | UChat Qwen | 0.6x | $2.40 | $9.60 | Pure Azure | 1.5x | $6.00 | $24.00 | 4x |
| `deepseek-r1-distill-qwen-32b` | Special-Domestic 40% | 0.8x | $1.60 | $4.80 | Pure Azure | 1.5x | $3.00 | $9.00 | 3x |
| `deepseek-r1-distill-qwen-7b` | Special-Domestic 40% | 0.8x | $0.40 | $0.80 | Pure Azure | 1.5x | $0.75 | $1.50 | 2x |
| `deepseek-reasoner` | UChat Qwen | 0.6x | $2.40 | $9.60 | Pure Azure | 1.5x | $6.00 | $24.00 | 4x |

<!-- DEEPSEEK_PRICE_TABLE_END -->

### Modelos chinos (Qwen/Doubao/GLM/Kimi/MiniMax)

<!-- CN_MODEL_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `qwen3-max` | Flash Sale | 0.6x | $1.50 | $6.00 | Pure Azure | 1.5x | $3.75 | $15.00 | 4x |
| `qwen3-max-2026-01-23` | Alibaba 40% | 0.8x | $2.00 | $8.00 | Pure Azure | 1.5x | $3.75 | $15.00 | 4x |
| `qwen3-coder` | Special-Domestic 40% | 0.8x | $4.80 | $19.20 | Pure Azure | 1.5x | $9.00 | $36.00 | 4x |
| `qwen3-coder-plus` | Flash Sale | 0.6x | $2.40 | $9.60 | Special-HC1 | 1.32x | $5.28 | $21.12 | 4x |
| `qwen3.6-plus` | Default | 1x | $2.00 | $12.00 | Pure Azure | 1.5x | $3.00 | $18.00 | 6x |
| `qwen3.7-max` | Flash Sale | 0.6x | $7.20 | $21.60 | Pure Azure | 1.5x | $18.00 | $54.00 | 3x |
| `glm-4.6` | Flash Sale | 0.6x | $1.20 | $4.80 | Pure Azure | 1.5x | $3.00 | $12.00 | 4x |
| `glm-4.5` | Flash Sale | 0.6x | $0.96 | $3.84 | Pure Azure | 1.5x | $2.40 | $9.60 | 4x |
| `glm-4.5-air` | Flash Sale | 0.6x | $0.48 | $3.60 | Pure Azure | 1.5x | $1.20 | $9.00 | 7.5x |
| `kimi-k2` | Special-Domestic 40% | 0.8x | $3.20 | $12.80 | Special-Premium GPT | 5.6x | $22.40 | $89.60 | 4x |
| `kimi-k2.5` | Special-Domestic 40% | 0.8x | $3.20 | $16.80 | Pure Azure | 1.5x | $6.00 | $31.50 | 5.25x |
| `kimi-k3` | Pure Azure | 1.5x | $30.00 | $150.00 | Official Relay | 3x | $60.00 | $300.00 | 5x |

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
   - Alipay / WeChat Pay / Crypto Pay / Stripe / Global Pay
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

📖 Guía completa: [Configuración de Claude Code](docs/es/claude-code-guide.md)

### OpenAI Codex

```bash
npm install -g @openai/codex
export OPENAI_API_KEY="***"
export OPENAI_API_BASE="https://ai.levolink.com/v1"
```

📖 Guía completa: [Configuración de Codex](docs/es/codex-setup.md)

### Gemini CLI

```bash
npm install -g @google/gemini-cli
export GEMINI_API_KEY="***"
export GEMINI_API_BASE="https://ai.levolink.com/v1"
```

📖 Guía completa: [Configuración de Cursor IDE](docs/es/cursor-setup.md) (también aplica para Gemini CLI)

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

> Basado en información pública al 2026-07-29. Solo como referencia.

| | [Levolink AI](https://ai.levolink.com) | OpenRouter | SiliconFlow | Otros proxies | Autoconstruido |
|--|-------------|-----------|-------------|---------------|------------|
| Número de modelos | **228+** | ~400 | ~200 | ~100 | Manual |
| Opciones de grupos | **33 grupos** | Ninguna (por proveedor) | Ninguna | 1-3 | - |
| CDN en China | ✅ Multi-nodo | ❌ Sin nodos en China | ✅ Único | ✅ | ❌ |
| Recarga mínima | **¥1** | ~¥35 | ¥50 | ¥20 | - |
| Pago por uso | ✅ | ✅ | ✅ | ✅ | ❌ |
| Claude Code ready | ✅ | ✅ | ✅ | ✅ | ❌ |
| OpenAI compatible | ✅ | ✅ | ✅ | ✅ | Necesita adaptador |
| Transparencia de precios | ✅ 33 grupos | Por modelo, elección limitada | Precio único | Precio único | - |
| Factura | ✅ | ❌ Sin factura china | ✅ | ❌ | - |
| Código abierto en GitHub | ✅ Precios automáticos | ❌ | ❌ | ❌ | - |

---

## ❓ Preguntas frecuentes

**¿Las respuestas son idénticas a las de la API oficial?**

Sí. Levolink AI solo reenvía las solicitudes a los modelos oficiales: las respuestas son consistentes con la API oficial.

**¿Mi cuenta puede ser baneada?**

No. Usas la clave de Levolink AI, no el sistema de cuentas oficial, tu cuenta oficial no está en riesgo.

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
| [Guía de Claude Code](docs/es/claude-code-guide.md) | Configuración completa de Claude Code para China |
| [Guía de Claude Desktop](docs/es/claude-desktop-guide.md) | Configurar Claude Desktop con Levolink AI |
| [Guía de Codex](docs/es/codex-setup.md) | Configuración de OpenAI Codex CLI para China |
| [Guía de Gemini CLI](docs/es/gemini-cli-guide.md) | Gemini CLI con Levolink AI para modelos Gemini |
| [Configuración de Cursor IDE](docs/es/cursor-setup.md) | Usar GPT-5.6 / Claude 4.8 / Gemini en Cursor |
| [Guía de Grok Build](docs/es/grok-build-guide.md) | xAI Grok Build con modelos personalizados de Levolink AI |
| [Guía de OpenCode](docs/es/opencode-guide.md) | OpenCode agente open-source con Levolink AI |
| [Guía de OpenClaw](docs/es/openclaw-guide.md) | OpenClaw Agent runtime con Levolink AI |
| [Guía de CC Switch](docs/es/cc-switch-guide.md) | Gestión unificada de configuración para múltiples herramientas IA |
| [Guía de integración con Dify](docs/es/dify-integration.md) | Conectar Dify con Levolink AI |
| [Guía de selección de modelos](docs/es/model-selection-guide.md) | ¿Cuál de los 228 modelos elegir? Por caso de uso y presupuesto |
| [Guía de detección de fraude](docs/es/fraud-detection-guide.md) | 5 métodos para detectar sustitución de modelos en proxies de API |
| [Guía de calculadora de costos](docs/es/cost-calculator-guide.md) | Estima costos de API y optimiza el gasto |

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

## 📢 Aviso de Marcas Registradas

GPT y OpenAI son marcas registradas de OpenAI. Claude es una marca registrada de Anthropic PBC. Gemini es una marca registrada de Google LLC. DeepSeek es una marca registrada de DeepSeek. Este repositorio describe únicamente la compatibilidad y no implica afiliación oficial ni respaldo por parte de estas empresas.
