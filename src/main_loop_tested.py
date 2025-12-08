import os
import subprocess
import json
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
)

# ────────────────────────────────
def ask_chatt(system_prompt, user_prompt):
    response = client.chat.completions.create(
        model=os.getenv("DEFAULT_MODEL", "gpt-4o-mini"),
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.choices[0].message.content

# ────────────────────────────────
def save_file(folder, prefix, content, ext):
    """파일 저장 공통 함수"""
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"{folder}/{prefix}_{timestamp}.{ext}"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path

# ────────────────────────────────
def run_pytest():
    """pytest 실행 후 결과 반환"""
    result = subprocess.run(["pytest", "-q", "--tb=short", "--disable-warnings", "-rN"], 
                            capture_output=True, text=True)
    return result.stdout

# ────────────────────────────────
def vibe_loop():
    base_system = (
        "당신은 현대트랜시스의 AI 개발 엔지니어 Chat‑T입니다.\n"
        "요청을 분석하여 Python 코드와 해당 코드에 대한 pytest 테스트 코드를 함께 작성하세요.\n"
        "출력은 반드시 ```python 코드블록``` 형식으로 작성합니다."
    )

    print("=" * 60)
    print("🚀  Vibe Coding (Test‑Automation Loop)")
    print("Type 'exit' or 'quit' to end.")
    print("=" * 60)

    while True:
        prompt = input("\n프롬프트 입력 >> ")
        if prompt.lower() in ["exit", "quit"]:
            print("🔚 종료합니다.")
            break

        try:
            # Chat‑T에게 코드 + 테스트 코드 요청
            answer = ask_chatt(base_system, prompt)
            print("\n[Chat‑T 응답]\n", answer)

            # 코드만 추출
            code_segment = answer
            if "```" in answer:
                code_segment = answer.split("```")[1]
                if code_segment.startswith("python"):
                    code_segment = code_segment[len("python"):]
                code_segment = code_segment.strip("`\n ")

            # 코드 및 테스트 파일로 분리 저장
            main_path = save_file("output", "main_code", code_segment, "py")
            test_path = save_file("tests", "test_code", code_segment, "py")

            print(f"💾 코드 저장: {main_path}")
            print(f"💾 테스트 저장: {test_path}")

            # pytest 실행
            test_output = run_pytest()
            print("\n[테스트 실행 결과]")
            print(test_output)

            # 리뷰 + 개선 요청
            review_prompt = (
                "다음은 Chat‑T가 작성한 코드의 테스트 실행 결과입니다.\n"
                "테스트 결과를 분석하고 문제가 있다면 개선된 코드를 제시하세요.\n\n"
                f"테스트 출력:\n{test_output}"
            )
            review = ask_chatt(base_system, review_prompt)
            print("\n[리뷰 및 개선 결과]\n", review)

        except Exception as e:
            print(f"⚠️ 오류 발생: {e}")
            continue

# ────────────────────────────────
if __name__ == "__main__":
    vibe_loop()
