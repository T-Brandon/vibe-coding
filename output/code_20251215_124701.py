# even_filter.py
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def filter_even_numbers(numbers):
    """
    리스트에서 짝수만 필터링하여 반환하는 함수
    :param numbers: 정수 리스트
    :return: 짝수 리스트
    """
    try:
        if not isinstance(numbers, list):
            raise TypeError("입력값은 리스트여야 합니다.")

        even_list = [n for n in numbers if isinstance(n, int) and n % 2 == 0]
        logger.info("짝수 리스트 필터링 완료: %s", even_list)
        return even_list

    except Exception as e:
        logger.error("짝수 필터링 중 오류 발생: %s", e)
        raise


# 테스트 코드 (pytest)
# test_even_filter.py
import pytest
from even_filter import filter_even_numbers


def test_filter_even_numbers_basic():
    assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_filter_even_numbers_empty():
    assert filter_even_numbers([]) == []


def test_filter_even_numbers_no_even():
    assert filter_even_numbers([1, 3, 5, 7]) == []


def test_filter_even_numbers_mixed_types():
    assert filter_even_numbers([2, "a", 4.5, 6, None]) == [2, 6]


def test_filter_even_numbers_invalid_input():
    with pytest.raises(TypeError):
        filter_even_numbers("1234")