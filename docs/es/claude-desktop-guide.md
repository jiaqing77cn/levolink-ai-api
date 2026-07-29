# Guía de Integración con Claude Desktop

> Usa Levolink AI en la aplicación de escritorio Claude Desktop, con acceso a modelos Claude sin necesidad de VPN.

## ¿Qué es Claude Desktop?

Claude Desktop es el cliente de escritorio oficial de Anthropic, compatible con macOS y Windows. Mediante la configuración de variables de entorno, Claude Desktop puede acceder a los modelos Claude a través de Levolink AI como intermediario.

## Pasos de Configuración

### 1. Configurar Variables de Entorno

**macOS:**

```bash
# Añadir a ~/.zshrc o ~/.bash_profile
export ANTHROPIC_API_KEY="tu Levolink API Key"
export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"

# Aplicar cambios
source ~/.zshrc
```

**Windows:**

```powershell
# Configuración permanente en PowerShell
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "tuKey", "User")
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_BASE_URL", "https://ai.levolink.com/v1", "User")
```

### 2. Reiniciar Claude Desktop

Cierra completamente Claude Desktop (no minimizar), luego reinicia la aplicación. La aplicación leerá las nuevas variables de entorno.

### 3. Verificar Conexión

Envía un mensaje en Claude Desktop. Si recibes una respuesta correctamente, significa que la conexión a través de Levolink AI se ha establecido correctamente.

## Configuración de MCP Server

Claude Desktop es compatible con MCP (Model Context Protocol), lo que permite integrar más herramientas:

Edita el archivo de configuración:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "levolink": {
      "command": "curl",
      "args": ["https://ai.levolink.com/v1/chat/completions"]
    }
  }
}
```

## Modelos Recomendados

| Uso | Modelo | Grupo Recomendado |
|------|------|---------|
| Conversación diaria | `claude-sonnet-4-6` | Por defecto (1.0x) |
| Tareas complejas | `claude-opus-4-8` | Por defecto (1.0x) |
| Tareas ligeras | `claude-haiku-4-5` | Por defecto (1.0x) |

## Preguntas Frecuentes

### P: ¿Claude Desktop no lee las variables de entorno después de iniciar?

Asegúrate de cerrar completamente la aplicación (clic derecho en el icono de la bandeja -> Quit), luego inicia desde la terminal:

```bash
open -a "Claude"
```

### P: ¿Aparece "connection error"?

Verifica que el API Key sea correcto y que el Base URL termine con `/v1`.

### P: ¿Es compatible con Claude Opus 4.8?

Sí. Escribe `/model claude-opus-4-8` en la conversación para cambiar de modelo.

## Enlaces Relacionados

- [Levolink AI - Sitio Oficial](https://ai.levolink.com)
- [Descarga Oficial de Claude Desktop](https://claude.ai/download)
- [Documentación API](https://levolink.apifox.cn/)
