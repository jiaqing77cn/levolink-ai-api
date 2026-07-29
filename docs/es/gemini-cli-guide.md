# Guía de Integración con Gemini CLI

> Usa Levolink AI en Gemini CLI para invocar modelos como Gemini 3.5 Pro / Flash sin necesidad de VPN.

## ¿Qué es Gemini CLI?

Gemini CLI es el asistente de IA para terminal de Google, que soporta generación de código, análisis de documentos, automatización de tareas, etc. A través de Levolink AI, los usuarios en China pueden usar directamente los modelos de la serie Gemini.

## Pasos de Configuración

### 1. Instalar Gemini CLI

```bash
npm install -g @google/gemini-cli
```

### 2. Configurar Variables de Entorno

```bash
# Añadir a ~/.bash_profile o ~/.zshrc
export GEMINI_API_KEY="tu Levolink API Key"
export GEMINI_API_BASE="https://ai.levolink.com/v1"

# Aplicar cambios
source ~/.bash_profile
```

### 3. Comenzar a Usar

```bash
cd your-project
gemini
```

## Modelos y Grupos Recomendados

| Uso | Modelo | Grupo | Multiplicador |
|------|------|------|------|
| Uso diario | `gemini-2.5-flash` | gemini-cli | 1.0x |
| Tareas ligeras | `gemini-2.5-flash-lite` | gemini-cli | 1.0x |
| Tareas complejas | `gemini-2.5-pro` | gemini-cli | 1.0x |
| Generación de imágenes | `gemini-3-pro-image` | 优质gemini | 2.4x |

## Especificar Modelo

```bash
# Usar un modelo específico
gemini --model gemini-2.5-pro

# O cambiar en modo interactivo
> /model gemini-2.5-flash
```

## Configuración en Windows

```powershell
$env:GEMINI_API_KEY="tu Levolink API Key"
$env:GEMINI_API_BASE="https://ai.levolink.com/v1"
gemini
```

Configuración permanente:

```powershell
[System.Environment]::SetEnvironmentVariable("GEMINI_API_KEY", "tuKey", "User")
[System.Environment]::SetEnvironmentVariable("GEMINI_API_BASE", "https://ai.levolink.com/v1", "User")
```

## Preguntas Frecuentes

### P: Gemini CLI muestra el error "Invalid API key"

Verifica que las variables de entorno estén configuradas correctamente:

```bash
echo $GEMINI_API_KEY
echo $GEMINI_API_BASE
# Asegúrate de que el Base URL termine con /v1
```

### P: La respuesta es lenta

El grupo gemini-cli (multiplicador 1.0x) está optimizado para los modelos Gemini, ofreciendo mayor velocidad.

### P: ¿Es compatible con Gemini 3.5 Pro?

Sí. Usa `--model gemini-3-pro-image` o cámbialo en el modo interactivo.

## Enlaces Relacionados

- [Levolink AI - Sitio Oficial](https://ai.levolink.com)
- [Documentación Oficial de Gemini CLI](https://github.com/google-gemini/gemini-cli)
- [Documentación API](https://levolink.apifox.cn/)
- [Guía de Selección de Modelos](./model-selection-guide.md)
