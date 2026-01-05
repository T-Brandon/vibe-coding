class MacchiatoButton:
    def __init__(self):
        self.is_pressed = False

    def press(self):
        """맥치아토 버튼을 누릅니다."""
        try:
            self.is_pressed = True
            print("맥치아토 버튼이 눌렸습니다.")
        except Exception as e:
            print(f"버튼 누르기 중 오류 발생: {e}")

    def release(self):
        """맥치아토 버튼을 해제합니다."""
        try:
            self.is_pressed = False
            print("맥치아토 버튼이 해제되었습니다.")
        except Exception as e:
            print(f"버튼 해제 중 오류 발생: {e}")

    def get_status(self):
        """버튼 현재 상태를 반환합니다."""
        return self.is_pressed