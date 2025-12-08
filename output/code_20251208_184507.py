def get_even_numbers(numbers: list[int]) -> list[int]:
    """
    입력받은 리스트에서 짝수만 필터링하여 반환합니다.

    :param numbers: 정수 리스트
    :return: 짝수만 포함된 리스트
    """
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("리스트에는 정수만 포함되어야 합니다.")

    return [num for num in numbers if num % 2 == 0]


# --------- Pytest 테스트 코드 ---------
import pytest

def test_get_even_numbers_basic():
    assert get_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

def test_get_even_numbers_all_even():
    assert get_even_numbers([2, 4, 6, 8]) == [2, 4, 6, 8]

def test_get_even_numbers_no_even():
    assert get_even_numbers([1, 3, 5, 7]) == []

def test_get_even_numbers_empty():
    assert get_even_numbers([]) == []

def test_get_even_numbers_with_non_integer():
    with pytest.raises(ValueError):
        get_even_numbers([1, 2, "3", 4])