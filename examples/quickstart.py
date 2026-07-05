"""
Levolink AI — Python Quickstart
================================
Access 500+ AI models (Claude/GPT/Gemini/DeepSeek) via one OpenAI-compatible API.

Install:  pip install openai
Usage:    python quickstart.py
Docs:     https://levolink.apifox.cn/
"""

import os
from openai import OpenAI

# --- Configuration ---
API_KEY = os.environ.get("LEVOLINK_API_KEY", "your-api-key")
BASE_URL = "https://ai.levolink.com/v1"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)


def chat(model: str, message: str, **kwargs):
    """Send a chat completion request to any supported model."""
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": message}],
        **kwargs,
    )
    return resp.choices[0].message.content


def stream_chat(model: str, message: str):
    """Stream a chat completion response token by token."""
    stream = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": message}],
        stream=True,
    )
    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content:
            print(content, end="", flush=True)
    print()


if __name__ == "__main__":
    # Example 1: GPT-4o
    print("=== GPT-4o ===")
    print(chat("gpt-4o", "Write a Python quicksort in 5 lines."))

    # Example 2: Claude Sonnet 4.6
    print("\n=== Claude Sonnet 4.6 ===")
    print(chat(
        "claude-sonnet-4-20250514",
        "Explain quantum entanglement in one sentence.",
        extra_body={"anthropic_version": "vertex-2023-10-01"},
    ))

    # Example 3: DeepSeek R1 (streaming)
    print("\n=== DeepSeek R1 (streaming) ===")
    stream_chat("deepseek-reasoner", "Implement a simple web server in Python.")

    # Example 4: Gemini 2.5 Pro
    print("\n=== Gemini 2.5 Pro ===")
    print(chat("gemini-2.5-pro", "What is the capital of France?"))
