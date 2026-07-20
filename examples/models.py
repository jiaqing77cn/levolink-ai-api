"""
Levolink AI - Supported Models List
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
        "gpt-5.6-sol", "gpt-5.6-sol-max", "gpt-5.6-sol-ultra",
        "gpt-5.6-luna", "gpt-5.6-luna-max", "gpt-5.6-terra",
        "gpt-5.5", "gpt-5.4", "gpt-5.4-mini", "gpt-5.4-nano", "gpt-5.4-pro",
        "gpt-5.3-codex-spark", "gpt-5.2-chat", "gpt-5.2-codex",
        "gpt-5.1-codex", "gpt-5-codex", "gpt-5-chat", "gpt-5-mini", "gpt-5-nano", "gpt-5-pro",
        "gpt-image-2", "dall-e-3", "tts-1", "tts-1-hd", "whisper-1",
    ],
    # Anthropic
    "anthropic": [
        "claude-opus-4-8", "claude-opus-4-7", "claude-opus-4-6",
        "claude-opus-4-5-20251101", "claude-opus-4-1-20250805",
        "claude-sonnet-5", "claude-sonnet-4-6",
        "claude-sonnet-4-5-20250929", "claude-sonnet-4-20250514",
        "claude-fable-5", "claude-haiku-4-5-20251001",
    ],
    # Google
    "google": [
        "gemini-3.5-flash", "gemini-3.1-flash-lite", "gemini-3-pro-image",
        "gemini-2.5-pro", "gemini-2.5-flash", "gemini-2.5-flash-image",
        "gemini-2.5-flash-lite", "gemini-2.0-flash-lite",
    ],
    # DeepSeek
    "deepseek": [
        "deepseek-v3-1-250821", "deepseek-v3-1-think-250821",
        "deepseek-r1", "deepseek-r1-250528", "deepseek-reasoner",
        "deepseek-r1-distill-qwen-32b", "deepseek-r1-distill-qwen-7b",
    ],
    # Chinese Models
    "chinese": [
        "qwen3-max", "qwen3-coder", "qwen3-coder-plus", "qwen3.6-plus", "qwen3.7-max",
        "glm-4.6", "glm-4.5", "glm-4.5-air", "glm-4.5-flash",
        "kimi-k2", "kimi-k2.5", "kimi-k3",
        "doubao-seed-1-6-250615", "doubao-seed-1-8-251228", "doubao-seed-2-0-lite-260215",
        "MiniMax-M3", "MiniMax-M2.7",
    ],
    # Media Generation
    "media": [
        "midjourney", "suno-v4", "sora", "sora-2",
        "flux-1.1-pro", "flux-1-schnell", "flux-1-dev",
        "veo-3", "veo-2", "gpt-image-2",
        "qwen-image-max", "kling", "vidu",
    ],
}


def get_models_by_provider(provider: str) -> list[str]:
    """Get all models for a given provider."""
    return SUPPORTED_MODELS.get(provider.lower(), [])


def get_all_models() -> list[str]:
    """Get all supported models across all providers."""
    all_models = []
    for models in SUPPORTED_MODELS.values():
        all_models.extend(models)
    return sorted(set(all_models))


if __name__ == "__main__":
    for provider, models in SUPPORTED_MODELS.items():
        print(f"{provider}: {len(models)} models")
        for m in models[:5]:
            print(f"  - {m}")
        if len(models) > 5:
            print(f"  ... and {len(models) - 5} more")
        print()
    print(f"Total: {len(get_all_models())} models")
