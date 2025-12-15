# order_system.py
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MenuItemNotFoundError(Exception):
    pass

class OrderSystem:
    def __init__(self):
        self.menu = {
            "커피": 3000,
            "라떼": 4000,
            "주스": 3500
        }

    def calculate_total(self, item: str, quantity: int) -> dict:
        try:
            if item not in self.menu:
                logger.error(f"메뉴 '{item}' 를 찾을 수 없습니다.")
                raise MenuItemNotFoundError(f"'{item}'는 메뉴에 없습니다.")
            if quantity <= 0:
                logger.error("수량은 1 이상이어야 합니다.")
                raise ValueError("수량은 1 이상이어야 합니다.")
            
            total = self.menu[item] * quantity
            logger.info(f"주문 완료: {item} x {quantity}, 총금액: {total}원")
            return {"menu": item, "quantity": quantity, "total": total}
        
        except (MenuItemNotFoundError, ValueError) as e:
            logger.exception("주문 처리 중 오류 발생")
            raise e


if __name__ == "__main__":
    system = OrderSystem()
    try:
        selected_menu = input("메뉴를 선택하세요 (커피/라떼/주스): ")
        quantity = int(input("수량을 입력하세요: "))
        result = system.calculate_total(selected_menu, quantity)
        print(f"선택된 메뉴: {result['menu']}, 수량: {result['quantity']}, 총금액: {result['total']}원")
    except Exception as e:
        print(f"오류: {e}")