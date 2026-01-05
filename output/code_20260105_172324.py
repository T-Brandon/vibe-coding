import sys
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def exit_program():
    """
    프로그램을 안전하게 종료합니다.
    """
    try:
        logger.info("프로그램을 종료합니다.")
        sys.exit(0)
    except Exception as e:
        logger.error(f"프로그램 종료 중 오류 발생: {e}")
        sys.exit(1)

# 테스트 코드
def test_exit_program():
    """
    exit_program 함수 테스트
    """
    import pytest
    with pytest.raises(SystemExit) as excinfo:
        exit_program()
    assert excinfo.value.code == 0

if __name__ == "__main__":
    exit_program()