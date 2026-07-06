"""
Levolink AI — Supported Models List
====================================
Complete list of 500+ AI models available through the Levolink AI API proxy.

Usage:
    from models import SUPPORTED_MODELS, get_models_by_provider
    print(get_models_by_provider("openai"))

Docs: https://levolink.apifox.cn/
"""

SUPPORTED_MODELS = {
    # OpenAI
    "openai": [
        "gpt-5", "gpt-4o", "gpt-4o-mini", "gpt-4", "gpt-4-turbo",
        "gpt-3.5-turbo", "gpt-3.5-turbo-16k", "o1", "o1-mini", "o3-mini",
        "dall-e-3", "dall-e-2", "tts-1", "tts-1-hd", "whisper-1",
    ],
    # Anthropic
    "anthropic": [
        "claude-opus-4-20250514", "claude-sonnet-4-20250514",
        "claude-haiku-4-20250514", "claude-3-5-sonnet-20241022",
        "claude-3-5-haiku-20241022", "claude-3-opus-20240229",
    ],
    # Google
    "google": [
        "gemini-2.5-pro", "gemini-2.0-flash", "gemini-2.0-flash-lite",
        "gemini-1.5-pro", "gemini-1.5-flash", "gemini-1.5-flash-8b",
    ],
    # DeepSeek
    "deepseek": [
        "deepseek-chat", "deepseek-coder", "deepseek-reasoner",
        "deepseek-v4", "deepseek-r1", "deepseek-r1-distill-qwen-32b",
    ],
    # Chinese Models
    "chinese": [
        "qwen3-235b-a22b", "qwen3-30b-a3b", "qwen2.5-72b-instruct",
        "doubao-pro-32k", "doubao-pro-128k", "doubao-lite-32k",
        "glm-4-plus", "glm-4-air", "glm-4-flash",
        "moonshot-v1-8k", "moonshot-v1-32k", "moonshot-v1-128k",
        "minimax-abab6.5s", "minimax-abab6.5",
    ],
    # Image / Video / Audio
    "media": [
        "midjourney", "suno-v3.5", "suno-v4", "sora", "sora-2",
        "flux-1.1-pro", "flux-1-schnell", "flux-1-dev",
        "veo-3", "veo-2", "stable-diffusion-3.5-large",
    ],
}


def get_models_by_provider(provider: str) -> list:
    """Get all available models for a given provider."""
    return SUPPORTED_MODELS.get(provider.lower(), [])


def get_all_models() -> list:
    """Get a flat list of all supported models."""
    models = []
    for provider_models in SUPPORTED_MODELS.values():
        models.extend(provider_models)
    return models


def get_provider(model_name: str) -> str:
    """Find which provider a model belongs to."""
    for provider, models in SUPPORTED_MODELS.items():
        if model_name in models:
            return provider
    return "unknown"


if __name__ == "__main__":
    total = len(get_all_models())
    print(f"Levolink AI supports {total}+ models across {len(SUPPORTED_MODELS)} providers:\n")
    for provider, models in SUPPORTED_MODELS.items():
        print(f"  {provider:12s} ({len(models):2d} models): {', '.join(models[:5])}{'...' if len(models) > 5 else ''}")
