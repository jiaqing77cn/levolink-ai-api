/**
 * Levolink AI — Node.js Quickstart
 * =================================
 * Access 500+ AI models (Claude/GPT/Gemini/DeepSeek) via one OpenAI-compatible API.
 *
 * Install:  npm install openai
 * Usage:    node quickstart.js
 * Docs:     https://levolink.apifox.cn/
 */

import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.LEVOLINK_API_KEY || "your-api-key",
  baseURL: "https://ai.levolink.com/v1",
});

async function chat(model, message, options = {}) {
  const resp = await client.chat.completions.create({
    model,
    messages: [{ role: "user", content: message }],
    ...options,
  });
  return resp.choices[0].message.content;
}

async function main() {
  // Example 1: GPT-4o
  console.log("=== GPT-4o ===");
  console.log(await chat("gpt-4o", "Write a JavaScript quicksort in 5 lines."));

  // Example 2: Claude Sonnet 4.6
  console.log("\n=== Claude Sonnet 4.6 ===");
  console.log(
    await chat("claude-sonnet-4-20250514", "Explain recursion briefly.", {
      extra_body: { anthropic_version: "vertex-2023-10-01" },
    })
  );

  // Example 3: DeepSeek R1
  console.log("\n=== DeepSeek R1 ===");
  console.log(await chat("deepseek-reasoner", "Write a hello world in Rust."));
}

main().catch(console.error);
