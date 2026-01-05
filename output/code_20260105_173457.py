class CoffeeMachine:
    def __init__(self):
        self.current_beverage = None
        self.is_brewing = False
        self.log = []

    def btn_Espresso(self):
        """에스프레소 버튼을 누를 때 호출되는 메서드"""
        try:
            if self.is_brewing:
                raise RuntimeError("현재 음료 제조 중입니다. 기다려주세요.")
            self.current_beverage = "Espresso"
            self.is_brewing = True
            self.log.append(f"[{self.current_beverage}] 제조 시작")
            return f"{self.current_beverage} 제조 중입니다."
        except Exception as e:
            self.log.append(f"에러: {str(e)}")
            raise

    def finish_brewing(self):
        """제조 완료 시 호출"""
        if self.is_brewing:
            self.is_brewing = False
            self.log.append(f"[{self.current_beverage}] 제조 완료")
            result = f"{self.current_beverage} 완성되었습니다!"
            self.current_beverage = None
            return result
        return "현재 제조 중인 음료가 없습니다."

    def get_log(self):
        """로그 조회"""
        return self.log.copy()