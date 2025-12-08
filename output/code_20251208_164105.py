def filter_even_numbers(numbers):
    """
    입력받은 리스트에서 짝수만 필터링하여 반환합니다.

    :param numbers: 정수 리스트
    :return: 짝수만 포함된 리스트
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
        
    return [n for n in numbers if isinstance(n, int) and n % 2 == 0]