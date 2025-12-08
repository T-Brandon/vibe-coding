"""
test_api.py
회사 ChatT 모델(API) 연결 테스트 스크립트
"""

import os
import json
import requests
from dotenv import load_dotenv

# .env 파일 로드 (API Key, Base URL 포함)
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("OPENAI_BASE_URL", "https://chat.hyundai-transys.com/api/")

def test_chatt_connection():
    """회사 내부 ChatT API 연결을 테스트합니다."""
    url = f"{BASE_URL}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    print("🔍 ChatT 서버 연결 테스트 중...")
    print(f"→ 요청 URL: {url}")
    print(f"→ 인증 키 앞 6자리: {API_KEY[:6]}************")

    try:
        response = requests.get(url, headers=headers, timeout=10)

        print(f"📡 상태 코드: {response.status_code}")
        if response.status_code == 200:
            # API가 JSON을 반환하는지 검사
            try:
                data = response.json()
                print("✅ 연결 성공! 모델 목록:")
                print(json.dumps(data, indent=2, ensure_ascii=False))
            except json.JSONDecodeError:
                print("⚠️ 서버가 HTML을 반환했습니다. API엔드포인트가 아닐 가능성이 높습니다.")
                print(response.text[:500])  # HTML 일부 출력
        elif response.status_code == 401:
            print("❌ 인증 실패 (API Key가 올바르지 않거나 권한이 없습니다.)")
        elif response.status_code == 404:
            print("❌ 잘못된 경로 (/models 엔드포인트를 찾을 수 없습니다.)")
        else:
            print("⚠️ 예기치 않은 응답:")
            print(response.text[:500])

    except requests.exceptions.RequestException as e:
        print(f"❌ 요청 실패: {e}")

if __name__ == "__main__":
    test_chatt_connection()