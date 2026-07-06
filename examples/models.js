/**
 * Levolink AI — Supported Models (JavaScript)
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
    "gpt-5", "gpt-4o", "gpt-4o-mini", "gpt-4", "gpt-4-turbo",
    "gpt-3.5-turbo", "gpt-3.5-turbo-16k", "o1", "o1-mini", "o3-mini",
    "dall-e-3", "tts-1", "tts-1-hd", "whisper-1",
  ],
  anthropic: [
    "claude-opus-4-20250514", "claude-sonnet-4-20250514",
    "claude-haiku-4-20250514", "claude-3-5-sonnet-20241022",
    "claude-3-5-haiku-20241022", "claude-3-opus-20240229",
  ],
  google: [
    "gemini-2.5-pro", "gemini-2.0-flash", "gemini-2.0-flash-lite",
    "gemini-1.5-pro", "gemini-1.5-flash", "gemini-1.5-flash-8b",
  ],
  deepseek: [
    "deepseek-chat", "deepseek-coder", "deepseek-reasoner",
    "deepseek-v4", "deepseek-r1",
  ],
  chinese: [
    "qwen3-235b-a22b", "qwen3-30b-a3b", "qwen2.5-72b-instruct",
    "doubao-pro-32k", "doubao-pro-128k", "glm-4-plus", "glm-4-flash",
    "moonshot-v1-8k", "moonshot-v1-32k", "moonshot-v1-128k",
    "minimax-abab6.5s", "minimax-abab6.5",
  ],
  media: [
    "midjourney", "suno-v3.5", "suno-v4", "sora", "sora-2",
    "flux-1.1-pro", "flux-1-schnell", "flux-1-dev", "veo-3", "veo-2",
  ],
};

export function getModelsByProvider(provider) {
  return SUPPORTED_MODELS[provider.toLowerCase()] || [];
}

export function getAllModels() {
  return Object.values(SUPPORTED_MODELS).flat();
}

export function getProvider(modelName) {
  for (const [provider, models] of Object.entries(SUPPORTED_MODELS)) {
    if (models.includes(modelName)) return provider;
  }
  return "unknown";
}

// CLI output
if (import.meta.url === `file://${process.argv[1]}`) {
  const all = getAllModels();
  console.log(`Levolink AI supports ${all.length}+ models across ${Object.keys(SUPPORTED_MODELS).length} providers:\n`);
  for (const [provider, models] of Object.entries(SUPPORTED_MODELS)) {
    const preview = models.slice(0, 5).join(", ");
    const ellipsis = models.length > 5 ? "..." : "";
    console.log(`  ${provider.padEnd(12)} (${String(models.length).padStart(2)} models): ${preview}${ellipsis}`);
  }
}
