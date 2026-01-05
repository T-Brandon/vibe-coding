import logging

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def hello_world():
    """
    간단한 Hello World 함수
    """
    try:
        logger.info("Hello World 함수가 호출되었습니다.")
        return "Hello, World!"
    except Exception as e:
        logger.error(f"Hello World 함수 실행 중 오류 발생: {e}")
        raise

# 테스트 코드
def test_hello_world():
    """
    hello_world 함수 테스트
    """
    result = hello_world()
    assert result == "Hello, World!", "함수 결과가 예상과 다릅니다."
    logger.info("테스트 통과: hello_world 함수")