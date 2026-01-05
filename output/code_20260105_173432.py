# 버튼 클래스 정의
class Button:
    def __init__(self, name: str, is_pressed: bool = False):
        self.name = name
        self.is_pressed = is_pressed

    def press(self):
        """버튼을 누릅니다."""
        self.is_pressed = True
        return f"{self.name} 버튼이 눌렸습니다."

    def release(self):
        """버튼을 해제합니다."""
        self.is_pressed = False
        return f"{self.name} 버튼이 해제되었습니다."

    def get_status(self):
        """버튼의 현재 상태를 반환합니다."""
        return self.is_pressed


# pytest 테스트
def test_button_press_and_release():
    button = Button("Start")
    assert button.get_status() is False
    assert button.press() == "Start 버튼이 눌렸습니다."
    assert button.get_status() is True
    assert button.release() == "Start 버튼이 해제되었습니다."
    assert button.get_status() is False