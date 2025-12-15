import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def add_numbers(a: float, b: float) -> float:
    """
    두 숫자를 더하는 기능.
    예외 처리 및 로깅 포함.
    """
    try:
        result = a + b
        logger.info("두 숫자를 더했습니다: %s + %s = %s", a, b, result)
        return result
    except TypeError as e:
        logger.error("입력값 오류: %s", e)
        raise ValueError("입력값은 숫자여야 합니다.") from e


# -------------------- 테스트 코드 --------------------
import pytest


def test_add_numbers_success():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(2.5, 3.5) == 6.0


def test_add_numbers_invalid_type():
    with pytest.raises(ValueError):
        add_numbers("a", 3)