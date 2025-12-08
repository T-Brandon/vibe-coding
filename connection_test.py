from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
)

try:
    resp = client.models.list()
    print("✅ API 연결 성공:", resp.data[0].id)
except Exception as e:
    print(f"❌ API 연결 실패: {e}")
    print(f"💡 오류 타입: {type(e)}")
    print(f"💡 오류 내용: {str(e)}")