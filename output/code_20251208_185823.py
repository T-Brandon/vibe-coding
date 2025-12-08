import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def filter_even_numbers(numbers):
    """
    주어진 리스트에서 짝수만 필터링하여 반환합니다.
    :param numbers: int형 리스트
    :return: 짝수만 포함된 리스트
    """
    try:
        if not isinstance(numbers, list):
            raise TypeError("입력은 리스트여야 합니다.")
        even_numbers = [n for n in numbers if isinstance(n, int) and n % 2 == 0]
        logger.info("짝수 필터링 결과: %s", even_numbers)
        return even_numbers
    except Exception as e:
        logger.exception("짝수 필터링 중 오류 발생: %s", e)
        raise


# =========================== pytest 테스트 코드 ===========================

import pytest

def test_filter_even_numbers_with_valid_input():
    assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

def test_filter_even_numbers_with_empty_list():
    assert filter_even_numbers([]) == []

def test_filter_even_numbers_with_all_odd():
    assert filter_even_numbers([1, 3, 5]) == []

def test_filter_even_numbers_with_mixed_types():
    assert filter_even_numbers([1, 2, 'a', 4.0, 6]) == [2, 6]

def test_filter_even_numbers_with_invalid_input():
    with pytest.raises(TypeError):
        filter_even_numbers("1234")