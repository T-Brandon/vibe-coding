# src/main_loop_ci.py
import os
import subprocess
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

# ─────────────────────────────────────────────────────────
# 환경 변수 로드
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
)

# ─────────────────────────────────────────────────────────
def run_cmd(cmd, cwd="."):
    """외부 명령 실행 후 결과 반환"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    return result.returncode, result.stdout + result.stderr

def ask_chatt(system_prompt, user_prompt):
    """Chat‑T 모델 호출"""
    resp = client.chat.completions.create(
        model=os.getenv("DEFAULT_MODEL", "gpt-4o-mini"),
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",  "content": user_prompt}
        ],
    )
    return resp.choices[0].message.content

# ─────────────────────────────────────────────────────────
def save_code(content, folder="output"):
    """AI 생성 코드 저장"""
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"{folder}/code_{timestamp}.py"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path

def run_tests():
    """pytest 실행 후 결과 반환"""
    code, out = run_cmd("pytest -q --disable-warnings -rN")
    return code, out

def git_commit(file_path, message):
    """테스트 통과 시 Git 커밋 및 푸시 실행"""
    cmds = [
        f"git add -f {file_path}",                       # 무시된 경로도 강제 추가
        f'git commit -m "{message}"'
    ]
    for cmd in cmds:
        code, out = run_cmd(cmd)
        print(f"📝 {cmd} → 반환코드:{code}")
        if out:
            print(out)
        if code != 0:
            return False
    # 자동 푸시
    code, push_out = run_cmd("git push origin HEAD")  # HEAD: 현재 브랜치 자동 감지
    print(push_out)
    return code == 0

# ─────────────────────────────────────────────────────────
def get_recent_commit_summary():
    """가장 최근 커밋 메시지 요약"""
    code, log = run_cmd("git log -1 --pretty=%B")
    return f"최근 커밋 요약:\n{log.strip()}"

# ─────────────────────────────────────────────────────────
def vibe_ci_loop():
    base_system_prompt = (
    "당신은 현대트랜시스의 숙련된 백엔드 Python 엔지니어이며, "
    "테스트 주도 개발(TDD)을 실천하는 AI 개발 어시스턴트 Chat‑T입니다.\n"
    "요구사항을 분석하여 실행 가능한 Python 코드를 작성하고, 대응되는 pytest 테스트를 반드시 포함하세요.\n"
    "작성하는 모든 코드에는 예외 처리와 로깅을 추가하고, PEP8 스타일을 준수하십시오.\n"
    "출력은 반드시 ```python``` 코드 블록으로만 구성하고 불필요한 설명은 생략하세요."
    )

    # 최근 커밋 요약을 병합해서 시스템 프롬프트 확장
    summary = get_recent_commit_summary()
    system_prompt = base_system_prompt + "\n" + summary

    os.makedirs("logs", exist_ok=True)
    print("=" * 60)
    print("🚀  Chat‑T Vibe Coding – 자동 테스트 + Git 커밋 루프")
    print("Type 'exit' or 'quit' to end.")
    print("=" * 60)

    while True:
        prompt = input("\n프롬프트 입력 >> ")
        if prompt.lower() in ["exit", "quit"]:
            print("👋 세션 종료.")
            break

        try:
            # ① AI 코드 생성
            answer = ask_chatt(system_prompt, prompt)
            print("\n[Chat‑T 코드 생성]\n")
            print(answer)

            # ② 코드블록 정리
            code_body = answer
            if "```" in answer:
                code_body = answer.split("```")[1]
                if code_body.startswith("python"):
                    code_body = code_body[len("python"):]
                code_body = code_body.strip("`\n ")

            # ③ 코드 저장
            saved = save_code(code_body)
            print(f"💾 코드 저장 완료: {saved}")

            # ④ 테스트 실행
            code, output = run_tests()
            log_path = f"logs/test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(log_path, "w", encoding="utf-8") as f:
                f.write(output)
            print("\n[테스트 결과]\n")
            print(output)

            # ⑤ 테스트 통과 여부 판단
            if code == 0:
                print("✅ 테스트 통과! Git 커밋 및 푸시 진행 중…")
                message = f"✅ AutoCommit({os.getenv('DEFAULT_MODEL')}): {os.path.basename(saved)} 테스트 통과"
                success = git_commit(saved, message)
                if success:
                    log_summary = f"{datetime.now()}: {os.path.basename(saved)} ✅ 테스트 통과 및 커밋 완료\n"
                    with open("logs/commit_history.txt", "a", encoding="utf-8") as lf:
                        lf.write(log_summary)
                    print(f"📦 Git 커밋 및 푸시 완료 ({saved})")
                    print("🧾 커밋 이력이 logs/commit_history.txt에 기록되었습니다.")
                else:
                    print("⚠️ Git 커밋 혹은 푸시 실패.")
            else:
                print("❌ 테스트 실패 → Chat‑T에게 수정 요청")
                review_prompt = (
                    "다음 Python 코드와 테스트 출력 내용을 분석하고 오류를 수정하세요.\n"
                    "수정된 코드를 ```python``` 형식으로 제시하세요.\n\n"
                    f"코드:\n{code_body}\n\n테스트 출력:\n{output}"
                )
                feedback = ask_chatt(system_prompt, review_prompt)
                print("\n[Chat‑T 수정안]\n")
                print(feedback)
                print("-" * 60)

        except Exception as e:
            print(f"⚠️ 오류 발생: {e}")
            print("-" * 60)

# ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    vibe_ci_loop()