def add_two_numbers(a, b):
    """
    두 숫자를 더하는 함수
    """
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers (int or float)")
        return a + b
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

# 테스트 코드
def test_add_two_numbers():
    assert add_two_numbers(2, 3) == 5
    assert add_two_numbers(-1, 1) == 0
    assert add_two_numbers(0.5, 1.5) == 2.0
    assert add_two_numbers(100, -50) == 50
    assert add_two_numbers("a", 1) is None  # 잘못된 입력 테스트