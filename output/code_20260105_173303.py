import logging
from typing import Any, Dict, Optional

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ChatT:
    """현대트랜시스 AI 챗봇 ChatT"""

    def __init__(self):
        self.name = "ChatT"
        self.company = "현대트랜시스"
        logger.info(f"{self.name} 초기화 완료. {self.company}의 AI 챗봇입니다.")

    def greet(self) -> str:
        """인사 메시지 반환"""
        try:
            message = f"안녕하세요, 저는 {self.company}의 AI 챗봇 {self.name}입니다. 도움이 필요하신가요?"
            logger.info("인사 메시지 전송 완료")
            return message
        except Exception as e:
            logger.error(f"인사 메시지 생성 중 오류 발생: {e}")
            raise

    def process_request(self, request: str) -> Dict[str, Any]:
        """사용자 요청 처리"""
        try:
            if not request.strip():
                raise ValueError("요청 내용이 비어 있습니다.")

            response = {
                "status": "success",
                "message": f"요청 '{request}'을(를) 처리 중입니다.",
                "timestamp": __import__('datetime').datetime.now().isoformat()
            }
            logger.info(f"요청 처리 완료: {request}")
            return response
        except Exception as e:
            logger.error(f"요청 처리 중 오류 발생: {e}")
            return {
                "status": "error",
                "message": f"요청 처리 중 오류가 발생했습니다: {str(e)}",
                "timestamp": __import__('datetime').datetime.now().isoformat()
            }

# 테스트 코드
import pytest

def test_chat_t_init():
    chat_t = ChatT()
    assert chat_t.name == "ChatT"
    assert chat_t.company == "현대트랜시스"

def test_greet():
    chat_t = ChatT()
    greeting = chat_t.greet()
    assert "안녕하세요" in greeting
    assert "현대트랜시스" in greeting
    assert "ChatT" in greeting

def test_process_request():
    chat_t = ChatT()
    request = "테스트 요청"
    response = chat_t.process_request(request)
    assert response["status"] == "success"
    assert request in response["message"]

def test_process_request_empty():
    chat_t = ChatT()
    response = chat_t.process_request("")
    assert response["status"] == "error"

def test_process_request_whitespace():
    chat_t = ChatT()
    response = chat_t.process_request("   ")
    assert response["status"] == "error"