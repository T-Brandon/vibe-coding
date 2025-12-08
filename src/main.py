import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. 환경 변수 로드
load_dotenv()

# 2. OpenAI 클라이언트 초기화
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
)

# 3. API 연결 상태 확인 함수
def check_api_connection():
    try:
        resp = client.models.list()
        print("✅ API 연결 확인 완료. ChatT 모델 사용 가능.")
        return True
    except Exception as e:
        print(f"❌ API 연결 실패: {e}")
        print("💡 확인 사항:")
        print("   1. .env 파일에 API Key, Base URL, Model 이름이 올바른지 확인")
        print("   2. 회사 내부 서버(https://chat.hyundai-transys.com)에 접근 가능한지 확인")
        print("   3. 회사 담당자에게 모델명(Chat-T)이 존재하는지 확인")
        return False

# 4. 프롬프트 루프 함수
def vibe_coding_loop():
    print("=" * 50)
    print("🚀 Vibe Coding Developer Console (ChatT - Safe Mode)")
    print("Type 'exit' or 'quit' to end the session.")
    print("=" * 50)

    # API 연결 상태 확인
    if not check_api_connection():
        print("⚠️ API 연결이 실패하여 프롬프트 입력이 비활성화됩니다.")
        return

    while True:
        user_prompt = input("\n프롬프트 입력 >> ")
        if user_prompt.lower() in ["exit", "quit"]:
            print("🔚 종료합니다. 개발 세션을 마칩니다.")
            break

        # 시스템 프롬프트 로드
        system_prompt_path = "src/prompts/base_prompt.txt"
        if os.path.exists(system_prompt_path):
            with open(system_prompt_path, "r", encoding="utf-8") as f:
                system_prompt = f.read()
        else:
            system_prompt = "당신은 Python 전문 개발 엔지니어입니다."

        try:
            # AI 모델에 요청 보내기
            response = client.chat.completions.create(
                model=os.getenv("DEFAULT_MODEL", "gpt-4o-mini"),
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
            )

            # 응답이 객체인지 확인
            if hasattr(response, 'choices') and len(response.choices) > 0:
                print("\n[결과 출력]")
                print(response.choices[0].message.content)
                print("-" * 50)
            else:
                print("⚠️ 응답이 예상과 다릅니다. 관리자에게 문의하세요.")
                print("-" * 50)

        except Exception as e:
            print(f"⚠️ 오류 발생: {e}")
            print("-" * 50)

# 5. 진입점
if __name__ == "__main__":
    vibe_coding_loop()

# 응답 결과 파일 저장
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_path = f"output/code_{timestamp}.py"
os.makedirs("output", exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    f.write(response.choices[0].message.content)
print(f"💾 Code saved to: {output_path}")