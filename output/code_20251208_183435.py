# even_filter.py

def filter_even_numbers(numbers: list[int]) -> list[int]:
    """
    주어진 리스트에서 짝수만 필터링하여 반환하는 함수.
    
    Args:
        numbers (list[int]): 정수 리스트
    
    Returns:
        list[int]: 짝수만 포함된 리스트
    """
    return [n for n in numbers if n % 2 == 0]