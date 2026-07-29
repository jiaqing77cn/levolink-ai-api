# Guía de Integración con Claude Code

> La mejor solución para usar Claude Code en China, sin necesidad de VPN, con baja latencia.

## ¿Qué es Claude Code?

Claude Code es el asistente de programación con IA oficial de Anthropic, que se puede usar directamente en la terminal, y soporta generación de código, refactorización, corrección de bugs, escritura de pruebas, etc.

## Pasos de Configuración

### 1. Instalar Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

### 2. Configurar Variables de Entorno

```bash
# Añadir a ~/.bash_profile o ~/.zshrc
export ANTHROPIC_AUTH_TOKEN="Tu Levolink API Key"
export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"

# Aplicar cambios
source ~/.bash_profile
```

### 3. Comenzar a Usar

```bash
cd tu-proyecto
claude
```

## Grupos Recomendados

| Grupo | Multiplicador | Caso de Uso |
|-------|---------------|-------------|
| Por defecto (Azure+MJ) | 1.0x | Uso diario, alta relación calidad-precio |
| CC exclusivo | 2.4x | Optimizado específicamente para Claude Code, mayor estabilidad |
| anti/kiro | 1.2x | Opción de mejor relación calidad-precio |

## Preguntas Frecuentes

### P: Claude Code muestra el error "authentication failed"

Verifica que las variables de entorno estén configuradas correctamente:
```bash
echo $ANTHROPIC_AUTH_TOKEN
echo $ANTHROPIC_BASE_URL
```

### P: La velocidad de respuesta es lenta

Intenta cambiar de grupo. El grupo CC exclusivo está optimizado para Claude Code y ofrece mayor velocidad.

### P: ¿Soporta Claude Opus 4.8?

Sí. Escribe `/model` en Claude Code para cambiar de modelo.

## Enlaces Relacionados

- [Levolink AI - Sitio Oficial](https://ai.levolink.com)
- [Documentación Oficial de Claude Code](https://docs.anthropic.com/en/docs/claude-code)
- [Documentación de la API](https://levolink.apifox.cn/)
