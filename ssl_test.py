import requests

try:
    r = requests.get("https://chat.hyundai-transys.com/v1", timeout=10)
    print("✅ HTTPS request succeeded:", r.status_code)
except Exception as e:
    print("❌ HTTPS request failed:", e)