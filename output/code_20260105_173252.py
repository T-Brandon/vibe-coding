import logging
from typing import List, Dict

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class OrderManager:
    def __init__(self):
        self.orders: List[Dict[str, any]] = []

    def place_order(self, menu_name: str, quantity: int, price_per_unit: float) -> Dict[str, any]:
        """
        주문을 생성하고 저장합니다.
        """
        try:
            if not isinstance(menu_name, str) or not menu_name.strip():
                raise ValueError("메뉴명은 비어 있을 수 없습니다.")
            if not isinstance(quantity, int) or quantity <= 0:
                raise ValueError("수량은 1 이상의 정수여야 합니다.")
            if not isinstance(price_per_unit, (int, float)) or price_per_unit < 0:
                raise ValueError("가격은 0 이상의 숫자여야 합니다.")

            total_price = quantity * price_per_unit
            order = {
                "menu_name": menu_name.strip(),
                "quantity": quantity,
                "total_price": round(total_price, 2)
            }
            self.orders.append(order)
            logger.info(f"주문 완료: {order}")
            return order

        except Exception as e:
            logger.error(f"주문 처리 중 오류 발생: {e}")
            raise

    def get_all_orders(self) -> List[Dict[str, any]]:
        """
        현재까지의 모든 주문 목록을 반환합니다.
        """
        return self.orders.copy()


# Pytest 테스트
import pytest

def test_place_order_success():
    manager = OrderManager()
    order = manager.place_order("김치찌개", 2, 8500.0)
    assert order["menu_name"] == "김치찌개"
    assert order["quantity"] == 2
    assert order["total_price"] == 17000.0
    assert len(manager.get_all_orders()) == 1

def test_place_order_invalid_menu_name():
    manager = OrderManager()
    with pytest.raises(ValueError, match="메뉴명은 비어 있을 수 없습니다."):
        manager.place_order("", 1, 5000.0)

def test_place_order_invalid_quantity():
    manager = OrderManager()
    with pytest.raises(ValueError, match="수량은 1 이상의 정수여야 합니다."):
        manager.place_order("비빔밥", 0, 9000.0)

def test_place_order_invalid_price():
    manager = OrderManager()
    with pytest.raises(ValueError, match="가격은 0 이상의 숫자여야 합니다."):
        manager.place_order("국밥", 1, -1000.0)

def test_get_all_orders():
    manager = OrderManager()
    manager.place_order("김치찌개", 2, 8500.0)
    manager.place_order("비빔밥", 1, 9000.0)
    orders = manager.get_all_orders()
    assert len(orders) == 2
    assert orders[0]["menu_name"] == "김치찌개"
    assert orders[1]["menu_name"] == "비빔밥"