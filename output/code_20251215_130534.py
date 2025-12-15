import logging
from typing import Any

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def safe_divide(a: float, b: float) -> Any:
    """
    안전하게 두 수를 나누는 함수.
    예외 발생 시 None을 반환하고 로그를 남김.
    """
    try:
        result = a / b
        logger.info("Division successful: %s / %s = %s", a, b, result)
        return result
    except ZeroDivisionError:
        logger.error("Division by zero: a=%s, b=%s", a, b)
        return None
    except TypeError as e:
        logger.error("Invalid type for division: %s", e)
        return None


# -------------------- TEST CODE (pytest) -------------------- #
import pytest


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 2, 5.0),
        (7, -7, -1.0),
        (5, 0, None),
        ("10", 2, None),
    ],
)
def test_safe_divide(a, b, expected):
    assert safe_divide(a, b) == expected