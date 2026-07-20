/**
 * Levolink AI - Supported Models (JavaScript)
 * ============================================
 * Complete list of AI models available through the Levolink AI API proxy.
 *
 * Usage:
 *   import { SUPPORTED_MODELS, getModelsByProvider } from "./models.js";
 *   console.log(getModelsByProvider("openai"));
 *
 * Docs: https://levolink.apifox.cn/
 */

export const SUPPORTED_MODELS = {
  openai: [
    "gpt-5.6-sol", "gpt-5.6-sol-max", "gpt-5.6-sol-ultra",
    "gpt-5.6-luna", "gpt-5.6-luna-max", "gpt-5.6-terra",
    "gpt-5.5", "gpt-5.4", "gpt-5.4-mini", "gpt-5.4-nano", "gpt-5.4-pro",
    "gpt-5.3-codex-spark", "gpt-5.2-chat", "gpt-5.2-codex",
    "gpt-5.1-codex", "gpt-5-codex", "gpt-5-chat", "gpt-5-mini", "gpt-5-nano", "gpt-5-pro",
    "gpt-image-2", "dall-e-3", "tts-1", "tts-1-hd", "whisper-1",
  ],
  anthropic: [
    "claude-opus-4-8", "claude-opus-4-7", "claude-opus-4-6",
    "claude-opus-4-5-20251101", "claude-opus-4-1-20250805",
    "claude-sonnet-5", "claude-sonnet-4-6",
    "claude-sonnet-4-5-20250929", "claude-sonnet-4-20250514",
    "claude-fable-5", "claude-haiku-4-5-20251001",
  ],
  google: [
    "gemini-3.5-flash", "gemini-3.1-flash-lite", "gemini-3-pro-image",
    "gemini-2.5-pro", "gemini-2.5-flash", "gemini-2.5-flash-image",
    "gemini-2.5-flash-lite", "gemini-2.0-flash-lite",
  ],
  deepseek: [
    "deepseek-v3-1-250821", "deepseek-v3-1-think-250821",
    "deepseek-r1", "deepseek-r1-250528", "deepseek-reasoner",
    "deepseek-r1-distill-qwen-32b", "deepseek-r1-distill-qwen-7b",
  ],
  chinese: [
    "qwen3-max", "qwen3-coder", "qwen3-coder-plus", "qwen3.6-plus", "qwen3.7-max",
    "glm-4.6", "glm-4.5", "glm-4.5-air", "glm-4.5-flash",
    "kimi-k2", "kimi-k2.5", "kimi-k3",
    "doubao-seed-1-6-250615", "doubao-seed-1-8-251228", "doubao-seed-2-0-lite-260215",
    "MiniMax-M3", "MiniMax-M2.7",
  ],
  media: [
    "midjourney", "suno-v4", "sora", "sora-2",
    "flux-1.1-pro", "flux-1-schnell", "flux-1-dev",
    "veo-3", "veo-2", "gpt-image-2",
    "qwen-image-max", "kling", "vidu",
  ],
};

export function getModelsByProvider(provider) {
  return SUPPORTED_MODELS[provider.toLowerCase()] || [];
}

export function getAllModels() {
  return [...new Set(Object.values(SUPPORTED_MODELS).flat())].sort();
}

// CLI
if (import.meta.url === `file://${process.argv[1]}`) {
  for (const [provider, models] of Object.entries(SUPPORTED_MODELS)) {
    console.log(`${provider}: ${models.length} models`);
    models.slice(0, 5).forEach((m) => console.log(`  - ${m}`));
    if (models.length > 5) console.log(`  ... and ${models.length - 5} more`);
    console.log();
  }
  console.log(`Total: ${getAllModels().length} models`);
}
