class CoffeeButton:
    def __init__(self):
        self.coffee_type = "Americano"

    def press(self):
        """아메리카노 버튼을 누를 때 호출되는 메서드"""
        try:
            print(f"{self.coffee_type} 주문이 접수되었습니다.")
            return self.coffee_type
        except Exception as e:
            print(f"버튼 누르기 중 오류 발생: {e}")
            return None

# 테스트 코드
def test_btn_Americano():
    button = CoffeeButton()
    result = button.press()
    assert result == "Americano", "아메리카노 주문이 정상적으로 처리되지 않았습니다."