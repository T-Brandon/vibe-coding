def get_even_numbers(numbers: list[int]) -> list[int]:
    """
    주어진 리스트에서 짝수만 추출하여 반환하는 함수.
    
    Parameters:
        numbers (list[int]): 정수 리스트
    
    Returns:
        list[int]: 짝수만 포함된 리스트
    """
    return [n for n in numbers if n % 2 == 0]


if __name__ == "__main__":
    # 예시 실행
    sample = [1, 2, 3, 4, 5, 6]
    print(get_even_numbers(sample))  # [2, 4, 6]