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

# ───────────────────────────────
def run_cmd(cmd, cwd="."):
    """외부 명령 실행 후 결과 반환"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    return result.returncode, result.stdout + result.stderr

def ask_chatt(system_prompt, user_prompt):
    """Chat‑T 호출"""
    resp = client.chat.completions.create(
        model=os.getenv("DEFAULT_MODEL", "gpt-4o-mini"),
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return resp.choices[0].message.content

# ───────────────────────────────
def save_code(content, folder="output"):
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"{folder}/code_{timestamp}.py"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path

# ───────────────────────────────
def run_tests():
    code, out = run_cmd("pytest -q --disable-warnings -rN")
    return code, out

def git_commit(file_path, message):
    cmds = [
        f"git add {file_path}",
        f'git commit -m "{message}"'
    ]
    for cmd in cmds:
        code, out = run_cmd(cmd)
        print(f"📝 {cmd} → 반환코드:{code}")
        print(out)
        if code != 0:
            return False
    return True

# ───────────────────────────────
def vibe_ci_loop():
    system_prompt = (
        "당신은 현대트랜시스의 AI 개발 엔지니어 Chat‑T입니다.\n"
        "요구사항에 따라 Python 코드와 pytest 테스트를 함께 제작하세요."
    )

    os.makedirs("logs", exist_ok=True)

    print("=" * 60)
    print("🚀  Chat‑T Vibe Coding – 자동 테스트 + Git 커밋 루프")
    print("Type 'exit' or 'quit' to end.")
    print("=" * 60)

    while True:
        prompt = input("\n프롬프트 입력 >> ")
        if prompt.lower() in ["exit", "quit"]:
            print("👋 세션 종료.")
            break

        try:
            # ① 코드 요청
            answer = ask_chatt(system_prompt, prompt)
            print("\n[Chat‑T 코드생성]\n", answer)

            # 코드 본문 추출
            code_body = answer
            if "```" in answer:
                code_body = answer.split("```")[1]
                if code_body.startswith("python"):
                    code_body = code_body[len("python"):]
                code_body = code_body.strip("` \n")

            # ② 파일 저장
            saved = save_code(code_body)
            print(f"💾 저장됨: {saved}")

            # ③ 테스트 실행
            code, output = run_tests()
            log_path = f"logs/test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(log_path, "w", encoding="utf-8") as f:
                f.write(output)
            print("\n[테스트 출력]\n", output)

            # ④ 결과 판단
            if code == 0:
                print("✅ 테스트 통과! Git 커밋 진행 중…")
                success = git_commit(saved, f"✅ AutoCommit: {os.path.basename(saved)} 테스트 통과")
                if success:
                    print(f"📦 Git 커밋 완료 ({saved})")
                else:
                    print("⚠️ Git 커밋 실패.")
            else:
                print("❌ 테스트 실패, Chat‑T에 수정 요청.")
                review_prompt = (
                    "다음 코드와 테스트 출력내용을 분석하고 오류를 수정해주세요.\n\n"
                    f"코드:\n{code_body}\n\n테스트 출력:\n{output}"
                    "수정된 코드를 ```python``` 형식으로 제시하세요."
                )
                feedback = ask_chatt(system_prompt, review_prompt)
                print("\n[Chat‑T 수정안]\n", feedback)

        except Exception as e:
            print(f"⚠️ 오류: {e}")
            continue

# ───────────────────────────────
if __name__ == "__main__":
    vibe_ci_loop()
