import os
import subprocess
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
)

# ────────────────────────────────────────────────────────
def get_prompt():
    prompt = input("\n프롬프트 입력 >> ")
    if prompt.lower() in ["quit", "exit"]:
        return None
    return prompt

def save_code(content):
    os.makedirs("output", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"output/code_{timestamp}.py"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path

def run_code(path):
    os.makedirs("logs", exist_ok=True)
    log_path = f"logs/{os.path.basename(path).replace('.py', '.log')}"
    with open(log_path, "w", encoding="utf-8") as f:
        process = subprocess.Popen(["python3", path], stdout=f, stderr=f)
        process.wait()
    with open(log_path, "r", encoding="utf-8") as f:
        output = f.read()
    return output

# ────────────────────────────────────────────────────────
def ask_chatt(system_prompt, user_prompt, model=None):
    """Chat‑T 모델 호출"""
    response = client.chat.completions.create(
        model=model or os.getenv("DEFAULT_MODEL", "gpt-5"),
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.choices[0].message.content

# ────────────────────────────────────────────────────────
def vibe_loop():
    system_prompt = (
        "당신은 현대트랜시스의 AI 개발 엔지니어 Chat‑T입니다.\n"
        "요구사항을 분석해 실행 가능한 Python 코드를 작성하세요.\n"
        "출력은 반드시 코드블록(예: ```python```)으로 감싸주세요."
    )

    print("=" * 60)
    print("🚀  Vibe Coding (Advanced Loop with Chat‑T)  🚀")
    print("Type 'exit' to quit.")
    print("=" * 60)

    while True:
        prompt = get_prompt()
        if prompt is None:
            print("🔚 종료합니다.")
            break

        try:
            code_reply = ask_chatt(system_prompt, prompt)
            print("\n[Chat‑T 출력]")
            print(code_reply)

            # 코드만 추출 (```python~``` 블록 제거)
            code_body = code_reply
            if "```" in code_reply:
                code_body = code_reply.split("```")[1]
                if code_body.startswith("python"):
                    code_body = code_body[len("python"):]
                code_body = code_body.strip("` \n")

            saved_path = save_code(code_body)
            print(f"💾 코드가 '{saved_path}' 파일로 저장되었습니다.")

            # 코드 실행 및 결과 확인
            result = run_code(saved_path)
            print("\n[실행 결과]")
            print(result)

            # 실행결과 리뷰 전달
            review_prompt = (
                f"다음 Python 코드와 실행결과를 평가하고, 개선점을 제시하세요.\n\n"
                f"코드 내용:\n{code_body}\n\n실행결과:\n{result}\n"
                "만약 오류가 있다면 수정된 코드를 ```python``` 형식으로 작성해주세요."
            )
            review = ask_chatt(system_prompt, review_prompt)
            print("\n[Chat‑T 리뷰]")
            print(review)
            print("-" * 60)

        except Exception as e:
            print(f"⚠️ 오류 발생: {e}")
            print("-" * 60)

# ────────────────────────────────────────────────────────
if __name__ == "__main__":
    vibe_loop()
