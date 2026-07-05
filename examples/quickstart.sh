#!/bin/bash
# Levolink AI — curl Quickstart
# Access 500+ AI models via one OpenAI-compatible API.
# Docs: https://levolink.apifox.cn/

API_KEY="${LEVOLINK_API_KEY:-your-api-key}"
BASE_URL="https://ai.levolink.com/v1"

echo "=== GPT-4o ==="
curl -s "$BASE_URL/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $API_KEY" \
  -d '{
    "model": "gpt-4o",
    "messages": [{"role": "user", "content": "Say hello in 5 languages."}]
  }' | jq '.choices[0].message.content'

echo ""
echo "=== Claude Sonnet 4.6 ==="
curl -s "$BASE_URL/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $API_KEY" \
  -d '{
    "model": "claude-sonnet-4-20250514",
    "messages": [{"role": "user", "content": "What is 2+2?"}],
    "anthropic_version": "vertex-2023-10-01"
  }' | jq '.choices[0].message.content'

echo ""
echo "=== DeepSeek R1 (streaming) ==="
curl -s "$BASE_URL/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $API_KEY" \
  -d '{
    "model": "deepseek-reasoner",
    "messages": [{"role": "user", "content": "Write a Python one-liner."}],
    "stream": true
  }'
