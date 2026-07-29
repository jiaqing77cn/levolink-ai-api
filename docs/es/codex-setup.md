# Guía de Configuración de OpenAI Codex

> La mejor solución para usar OpenAI Codex CLI en China, sin necesidad de VPN, a través del proxy de Levolink AI.

## ¿Qué es Codex CLI?

OpenAI Codex CLI es el asistente de programación con IA para terminal de OpenAI, que soporta generación de código, refactorización, corrección de bugs, escritura de pruebas, etc. Similar a Claude Code, pero basado en modelos GPT.

## Pasos de Configuración

### 1. Instalar Codex CLI

```bash
npm install -g @openai/codex
```

### 2. Configurar Variables de Entorno

```bash
# Añadir a ~/.bash_profile o ~/.zshrc
export OPENAI_API_KEY="Tu Levolink API Key"
export OPENAI_API_BASE="https://ai.levolink.com/v1"

# Aplicar cambios
source ~/.bash_profile
```

### 3. Comenzar a Usar

```bash
cd tu-proyecto
codex
```

## Grupos y Modelos Recomendados

| Uso | Modelo | Grupo | Multiplicador | Precio de Entrada |
|-----|--------|-------|---------------|-------------------|
| Programación diaria | `gpt-5.6-luna` | Codex exclusivo | 0.8x | $0.64/M |
| Programación compleja | `gpt-5.6-sol` | Codex exclusivo | 0.8x | $3.20/M |
| Tareas ligeras | `gpt-5.4-mini` | Oferta especial | 0.6x | $0.27/M |
| Autocompletado de código | `gpt-5-codex` | Codex exclusivo | 0.8x | $0.80/M |

## Configuración en Windows

### PowerShell

```powershell
$env:OPENAI_API_KEY="Tu Levolink API Key"
$env:OPENAI_API_BASE="https://ai.levolink.com/v1"
codex
```

### Configuración Permanente

```powershell
[System.Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "TuKey", "User")
[System.Environment]::SetEnvironmentVariable("OPENAI_API_BASE", "https://ai.levolink.com/v1", "User")
```

## Preguntas Frecuentes

### P: Codex muestra el error "Invalid API key"

Verifica que las variables de entorno sean correctas:
```bash
echo $OPENAI_API_KEY
echo $OPENAI_API_BASE
# Asegúrate de que el Base URL termine con /v1
```

### P: La velocidad de respuesta es lenta

Cambia al grupo Codex exclusivo (0.8x), que está optimizado para los modelos de programación GPT.

### P: ¿Soporta GPT-5.6 Sol?

Sí. Especifica el modelo en Codex con `--model gpt-5.6-sol`.

### P: ¿Cuál es la diferencia con Claude Code?

| Dimensión | Codex CLI | Claude Code |
|-----------|-----------|-------------|
| Modelo | Serie GPT | Serie Claude |
| Estilo de programación | Directo y eficiente | Razonamiento profundo |
| Contexto | 128K | 200K |
| Casos de uso | Prototipos rápidos, scripts | Refactorización compleja, diseño de arquitectura |

Ambos se usan a través del proxy de Levolink AI, con una sola Key puedes alternar entre ellos.

## Enlaces Relacionados

- [Levolink AI - Sitio Oficial](https://ai.levolink.com)
- [Documentación Oficial de Codex CLI](https://github.com/openai/codex)
- [Documentación de la API](https://levolink.apifox.cn/)
- [Guía de Selección de Modelos](./model-selection-guide.md)
