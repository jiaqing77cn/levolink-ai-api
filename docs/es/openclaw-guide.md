# Guía de Integración con OpenClaw

> Usa Levolink AI como proveedor de modelos backend en OpenClaw.

## ¿Qué es OpenClaw?

OpenClaw es un runtime de Agent de IA de código abierto, que soporta programación multi-modelo, sistema de habilidades, tareas programadas, sistema de memoria, etc. Mediante la configuración de un endpoint compatible con OpenAI, se puede integrar Levolink AI.

## Pasos de Configuración

### 1. Instalar OpenClaw

```bash
# Instalar con npm
npm install -g openclaw

# O usar Docker
docker run -d openclaw/openclaw
```

### 2. Configurar Gateway

Edita el archivo de configuración del Gateway de OpenClaw (normalmente en `~/.openclaw/config.yaml` o en el directorio del proyecto `config.yaml`):

```yaml
# Configuración de modelos
model:
  # Modelo por defecto
  default: volces/glm-5.2

  # Proveedor compatible con OpenAI
  providers:
    - name: levolink
      api_key: "tu Levolink API Key"
      base_url: "https://ai.levolink.com/v1"
      models:
        - gpt-5.6-sol
        - gpt-5.6-luna
        - claude-sonnet-4-6
        - claude-opus-4-8
        - gemini-2.5-pro
        - deepseek-reasoner
```

### 3. O Configurar a través de Variables de Entorno

```bash
# Añadir a ~/.bash_profile o ~/.zshrc
export OPENAI_API_KEY="tu Levolink API Key"
export OPENAI_API_BASE="https://ai.levolink.com/v1"

source ~/.bash_profile
```

### 4. Iniciar OpenClaw

```bash
openclaw gateway start

# Verificar estado
openclaw status
```

## Configuración de Modelos Recomendados

| Uso | Modelo | Grupo Recomendado |
|------|------|---------|
| Tareas diarias del Agent | `gpt-5.6-luna` | Codex exclusivo (0.8x) |
| Razonamiento complejo | `claude-opus-4-8` | Por defecto (1.0x) |
| Tareas de programación | `claude-sonnet-4-6` | Por defecto (1.0x) |
| Procesamiento de textos largos | `gemini-2.5-pro` | gemini-cli (1.0x) |
| Opción económica | `deepseek-reasoner` | Oferta especial (0.6x) |

## Cambio de Modelo en Sesión

OpenClaw permite especificar diferentes modelos para diferentes sesiones:

```bash
# Cambiar modelo en una sesión
/model claude-opus-4-8

# Ver modelo actual
/status
```

## Programación Multi-modelo

OpenClaw soporta la programación simultánea de múltiples modelos, ideal para tareas paralelas del Agent:

```yaml
# Configurar múltiples providers simultáneamente
model:
  providers:
    - name: levolink-gpt
      api_key: "tuKey"
      base_url: "https://ai.levolink.com/v1"
    - name: levolink-claude
      api_key: "tuKey"
      base_url: "https://ai.levolink.com/v1"
```

## Preguntas Frecuentes

### P: OpenClaw muestra el error "model not available"

Verifica que el Gateway esté iniciado y que el nombre del modelo sea correcto:

```bash
openclaw status
openclaw models list
```

### P: ¿Cómo establecer el modelo por defecto?

Configura `model.default` en el archivo de configuración, o usa el comando `/model` en la sesión.

### P: ¿Soporta salida en streaming?

Sí. OpenClaw usa salida en streaming por defecto.

### P: ¿Cómo controlar los costes?

1. Usa el grupo de oferta especial (multiplicador 0.6x)
2. Selecciona el modelo adecuado para cada tarea
3. Configura límites de tokens en la configuración

## Enlaces Relacionados

- [Levolink AI - Sitio Oficial](https://ai.levolink.com)
- [Documentación Oficial de OpenClaw](https://docs.openclaw.ai)
- [GitHub de OpenClaw](https://github.com/openclaw/openclaw)
- [Documentación API](https://levolink.apifox.cn/)
- [Guía de Selección de Modelos](./model-selection-guide.md)
