class ButtonOrder:
    def __init__(self):
        self.is_pressed = False

    def press(self):
        """주문 버튼을 누릅니다."""
        self.is_pressed = True
        return "주문 버튼이 눌렸습니다."

    def release(self):
        """주문 버튼을 뗍니다."""
        self.is_pressed = False
        return "주문 버튼이 해제되었습니다."

    def get_status(self):
        """현재 버튼 상태를 반환합니다."""
        return "누름" if self.is_pressed else "해제됨"