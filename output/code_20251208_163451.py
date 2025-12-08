def filter_even_numbers(numbers: list[int]) -> list[int]:
    """
    주어진 리스트에서 짝수만 추출하여 반환하는 함수

    Args:
        numbers (list[int]): 정수 리스트

    Returns:
        list[int]: 짝수만 포함된 리스트
    """
    if not isinstance(numbers, list):
        raise TypeError("입력값은 리스트여야 합니다.")
    return [num for num in numbers if isinstance(num, int) and num % 2 == 0]