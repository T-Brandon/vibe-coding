# ChatT: 현대트랜시스 백엔드 Python 엔지니어 (TDD 기반)

import logging
from typing import Any, Dict, Optional

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ChatT:
    """현대트랜시스 AI 챗봇 ChatT"""

    def __init__(self):
        self.name = "ChatT"
        self.company = "현대트랜시스"
        logger.info(f"{self.name} 초기화 완료. {self.company} 소속 백엔드 엔지니어입니다.")

    def greet(self) -> str:
        """인사 메시지 반환"""
        try:
            message = f"안녕하세요. 저는 {self.company}의 AI 챗봇 {self.name}입니다. 도움이 필요하신가요?"
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
                "message": str(e),
                "timestamp": __import__('datetime').datetime.now().isoformat()
            }

# pytest 테스트 코드
import pytest
from datetime import datetime

def test_chatt_init():
    """ChatT 초기화 테스트"""
    chatt = ChatT()
    assert chatt.name == "ChatT"
    assert chatt.company == "현대트랜시스"
    assert isinstance(chatt, ChatT)

def test_greet():
    """인사 메시지 테스트"""
    chatt = ChatT()
    message = chatt.greet()
    assert "안녕하세요" in message
    assert "현대트랜시스" in message
    assert "ChatT" in message

def test_process_request_valid():
    """유효한 요청 처리 테스트"""
    chatt = ChatT()
    request = "Python 코드 작성해주세요"
    response = chatt.process_request(request)
    assert response["status"] == "success"
    assert request in response["message"]
    assert "timestamp" in response
    assert isinstance(datetime.fromisoformat(response["timestamp"]), datetime)

def test_process_request_empty():
    """빈 요청 처리 테스트"""
    chatt = ChatT()
    response = chatt.process_request("")
    assert response["status"] == "error"
    assert "요청 내용이 비어 있습니다." in response["message"]

def test_process_request_whitespace():
    """공백 요청 처리 테스트"""
    chatt = ChatT()
    response = chatt.process_request("   ")
    assert response["status"] == "error"
    assert "요청 내용이 비어 있습니다." in response["message"]