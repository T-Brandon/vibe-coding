# coffee_order.py
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CoffeeOrderSystem:
    def __init__(self):
        self.menu = {
            "btn_Americano": "Americano",
            "btn_Latte": "Latte",
            "btn_Espresso": "Espresso",
            "btn_Vanilla": "Vanilla Latte",
            "btn_Macchiato": "Macchiato",
        }
        self.order_list = []

    def select_coffee(self, button_name: str) -> str:
        try:
            coffee = self.menu.get(button_name)
            if not coffee:
                raise ValueError(f"존재하지 않는 버튼: {button_name}")
            self.order_list.append(coffee)
            logger.info(f"{coffee} 선택됨.")
            return coffee
        except Exception as e:
            logger.error(f"커피 선택 중 오류 발생: {e}")
            raise

    def order(self) -> str:
        try:
            if not self.order_list:
                raise ValueError("주문할 항목이 없습니다.")
            summary = ", ".join(self.order_list)
            logger.info(f"주문 완료: {summary}")
            self.order_list.clear()
            return f"주문 완료: {summary}"
        except Exception as e:
            logger.error(f"주문 처리 중 오류 발생: {e}")
            raise