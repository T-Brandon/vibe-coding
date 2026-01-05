import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def example_function():
    """
    예시 함수: 간단한 기능을 수행하고 로그를 기록합니다.
    """
    try:
        logger.info("예시 함수가 실행되었습니다.")
        return "함수가 정상적으로 실행되었습니다."
    except Exception as e:
        logger.error(f"예시 함수 실행 중 오류 발생: {e}")
        raise

# 테스트 코드
import pytest

def test_example_function():
    """example_function 테스트"""
    result = example_function()
    assert result == "함수가 정상적으로 실행되었습니다."
    logger.info("테스트가 성공적으로 완료되었습니다.")