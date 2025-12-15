import logging
import pytest

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def safe_divide(a: float, b: float) -> float:
    """
    두 수 a, b를 입력받아 a를 b로 나눈 값을 반환한다.
    0으로 나누는 경우 ValueError를 발생시킨다.
    """
    try:
        if b == 0:
            raise ValueError("0으로 나눌 수 없습니다.")
        result = a / b
        logger.info(f"{a} / {b} = {result}")
        return result
    except Exception as e:
        logger.error(f"나눗셈 중 오류 발생: {e}")
        raise


# ------------------- 테스트 코드 -------------------

def test_safe_divide_success():
    assert safe_divide(10, 2) == 5.0
    assert safe_divide(-9, 3) == -3.0


def test_safe_divide_zero_division():
    with pytest.raises(ValueError, match="0으로 나눌 수 없습니다."):
        safe_divide(5, 0)


def test_safe_divide_logging(caplog):
    with caplog.at_level(logging.INFO):
        result = safe_divide(8, 4)
        assert "8 / 4" in caplog.text
        assert result == 2.0