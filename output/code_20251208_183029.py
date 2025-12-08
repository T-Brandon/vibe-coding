# even_filter.py

def get_even_numbers(numbers: list[int]) -> list[int]:
    """
    주어진 리스트에서 짝수만 추출하여 반환하는 함수
    :param numbers: 정수 리스트
    :return: 짝수만 포함된 리스트
    """
    if not isinstance(numbers, list):
        raise TypeError("입력값은 리스트여야 합니다.")
    return [n for n in numbers if isinstance(n, int) and n % 2 == 0]


# 아래는 pytest용 테스트 코드입니다.
# test_even_filter.py
import pytest
from even_filter import get_even_numbers

def test_get_even_numbers_basic():
    assert get_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

def test_get_even_numbers_empty():
    assert get_even_numbers([]) == []

def test_get_even_numbers_no_even():
    assert get_even_numbers([1, 3, 5, 7]) == []

def test_get_even_numbers_with_negatives():
    assert get_even_numbers([-2, -1, 0, 1, 2]) == [-2, 0, 2]

def test_get_even_numbers_type_error():
    with pytest.raises(TypeError):
        get_even_numbers("1234")

def test_get_even_numbers_non_integers():
    # 정수가 아닌 요소는 무시되어야 함
    assert get_even_numbers([2, 3.5, '4', 6]) == [2, 6]