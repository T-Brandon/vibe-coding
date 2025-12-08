def get_even_numbers(numbers: list[int]) -> list[int]:
    """리스트에서 짝수만 추출하여 반환합니다."""
    if not isinstance(numbers, list):
        raise TypeError("입력값은 리스트여야 합니다.")
    return [n for n in numbers if isinstance(n, int) and n % 2 == 0]