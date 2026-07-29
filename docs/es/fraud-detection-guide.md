# Guía Completa de Detección de Adulteración en Proxies de IA

> Cómo detectar si un proxy de API de IA está usando modelos baratos haciéndose pasar por modelos caros.

## ¿Por qué es necesario detectarlo?

Algunos proxies, para maximizar ganancias, usan modelos baratos como GLM-4 haciéndose pasar por GPT-5, o Haiku haciéndose pasar por Opus. Los usuarios pagan el precio de un modelo premium pero reciben la salida de un modelo de bajo rendimiento.

## Métodos de Detección

### Método 1: Prueba de Razonamiento

Los modelos premium (GPT-5.6/Claude Opus 4.8) y los modelos económicos tienen una diferencia notable en capacidad de razonamiento.

```python
from openai import OpenAI

client = OpenAI(api_key="TuKey", base_url="https://ai.levolink.com/v1")

# Prueba 1: Problema clásico de razonamiento
resp = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": """
    A farmer has 17 sheep. All but 9 die. How many are left?
    Think step by step.
    """}]
)
print(resp.choices[0].message.content)
# Respuesta correcta de GPT-5.6: 9 (all but 9 died = 9 survived)
# Modelos de bajo rendimiento suelen responder: 8
```

### Método 2: Prueba de Contexto Largo

Los modelos premium soportan contextos de 200K+ tokens, mientras que los modelos económicos suelen tener solo 8K-32K.

```python
# Enviar un texto largo de 100K+ tokens con información específica al final
# Luego preguntar al modelo cuál es esa información
# Los modelos de bajo rendimiento perderán el contexto y no podrán responder

long_text = "Este es un texto muy largo..." * 5000  # Aprox. 100K tokens
long_text += "La contraseña es: PurpleDragon42"

resp = client.chat.completions.create(
    model="claude-opus-4-8",
    messages=[{"role": "user", "content": long_text + "\n\n¿Cuál es la contraseña?"}]
)
# Claude Opus 4.8 puede responder correctamente PurpleDragon42
# Los modelos de bajo rendimiento perderán el contexto
```

### Método 3: Prueba de Capacidad de Programación

```python
resp = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": """
    Implementa en Python una caché LRU thread-safe:
    1. Soporte expiración TTL
    2. Soporte límite maxsize
    3. Thread-safe
    4. Con estadísticas de hit rate
    """}]
)
# Claude Sonnet 4.6 dará una implementación completa
# Los modelos de bajo rendimiento darán código incompleto o con bugs
```

### Método 4: Verificación de Tokens Facturados

```python
import tiktoken

# Usar tiktoken para contar tokens
enc = tiktoken.encoding_for_model("gpt-5.6-sol")
text = "Hello, world! " * 1000
tokens = enc.encode(text)
print(f"Tokens reales: {len(tokens)}")

# Enviar petición, comparar tokens facturados
resp = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": text}]
)
print(f"prompt_tokens devueltos por la API: {resp.usage.prompt_tokens}")
# Si la API devuelve significativamente más que los reales, la facturación es sospechosa
```

### Método 5: Comparación de Velocidad de Respuesta

```python
import time

start = time.time()
resp = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": "Say hello"}]
)
elapsed = time.time() - start

# Latencia normal: 0.5-2s
# Si >5s podría estar redirigiendo a un modelo de bajo rendimiento
# Si <0.1s podría ser una respuesta en caché
print(f"Latencia: {elapsed:.2f}s")
```

## Transparencia de Levolink AI

Levolink AI ofrece 33 grupos, cada uno con el canal backend claramente etiquetado:

| Grupo | Backend | Multiplicador | Transparencia |
|-------|---------|---------------|---------------|
| Oferta especial | Canal mixto | 0.6x | El más barato, la calidad puede variar |
| Codex exclusivo | Optimizado para GPT | 0.8x | La mejor relación calidad-precio |
| Por defecto | Azure + MJ | 1.0x | Calidad estándar |
| CC exclusivo | Optimizado para Claude | 2.4x | El mejor para Claude Code |
| Nivel empresarial AWS | AWS Bedrock | 4.0x | Estabilidad de nivel empresarial |
| Oficial directo | Conexión directa oficial | 16.0x | 100% calidad oficial |

Los usuarios pueden elegir según sus necesidades, con precios transparentes y sin adulteración.
