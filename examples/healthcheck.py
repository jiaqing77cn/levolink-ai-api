#!/usr/bin/env python3
"""
Levolink AI — API Health Check
==============================
Check API endpoint connectivity and response time.

Usage: python healthcheck.py
Docs:  https://levolink.apifox.cn/
"""

import time
import urllib.request
import json

BASE_URL = "https://ai.levolink.com/v1"


def check_endpoint(name: str, url: str) -> dict:
    """Check a single API endpoint and return status info."""
    result = {"name": name, "url": url, "status": "unknown", "latency_ms": 0}
    start = time.time()
    try:
        req = urllib.request.Request(url)
        req.add_header("User-Agent", "LevolinkAI-HealthCheck/1.0")
        with urllib.request.urlopen(req, timeout=10) as resp:
            result["status"] = "ok"
            result["http_code"] = resp.getcode()
    except urllib.error.HTTPError as e:
        result["status"] = "http_error"
        result["http_code"] = e.code
    except Exception as e:
        result["status"] = "error"
        result["error"] = str(e)
    finally:
        result["latency_ms"] = round((time.time() - start) * 1000)
    return result


def main():
    endpoints = [
        ("API Base", f"{BASE_URL}/models"),
        ("Chat Completions", f"{BASE_URL}/chat/completions"),
        ("Website", "https://ai.levolink.com"),
        ("API Docs", "https://levolink.apifox.cn"),
    ]

    print("=" * 50)
    print("  Levolink AI — API Health Check")
    print("=" * 50)

    all_ok = True
    for name, url in endpoints:
        r = check_endpoint(name, url)
        icon = "✅" if r["status"] == "ok" or r.get("http_code") == 401 else "❌"
        if r.get("http_code") not in (200, 401):
            all_ok = False
        print(f"  {icon} {name:20s} {r['latency_ms']:>6}ms  {r.get('http_code', '-')}")
        if r["status"] == "error":
            print(f"     Error: {r.get('error', 'unknown')}")

    print("=" * 50)
    print(f"  Overall: {'All endpoints reachable ✅' if all_ok else 'Some endpoints unreachable ❌'}")
    print("=" * 50)


if __name__ == "__main__":
    main()
