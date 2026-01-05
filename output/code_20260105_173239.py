import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class OrderManager:
    def __init__(self):
        self.menu = {
            1: {"name": "김치찌개", "price": 8000},
            2: {"name": "비빔밥", "price": 9000},
            3: {"name": "불고기", "price": 15000}
        }
        self.current_order = {}

    def select_menu(self, menu_id: int, quantity: int) -> bool:
        """
        메뉴 선택 및 수량 입력
        :param menu_id: 메뉴 ID (1, 2, 3 중 하나)
        :param quantity: 주문 수량 (양수)
        :return: 성공 여부
        """
        try:
            if not isinstance(menu_id, int) or menu_id not in self.menu:
                raise ValueError(f"Invalid menu ID: {menu_id}")
            if not isinstance(quantity, int) or quantity <= 0:
                raise ValueError(f"Invalid quantity: {quantity}")

            menu_item = self.menu[menu_id]
            self.current_order = {
                "menu_id": menu_id,
                "name": menu_item["name"],
                "price": menu_item["price"],
                "quantity": quantity,
                "total_price": menu_item["price"] * quantity
            }
            logger.info(f"Menu selected: {menu_item['name']}, Quantity: {quantity}, Total: {self.current_order['total_price']} KRW")
            return True

        except Exception as e:
            logger.error(f"Order selection failed: {e}")
            return False

    def get_current_order(self):
        """현재 주문 정보 반환"""
        return self.current_order.copy() if self.current_order else None

# Pytest 테스트 코드
import pytest

def test_select_menu_valid():
    order_manager = OrderManager()
    result = order_manager.select_menu(1, 2)
    assert result is True
    order = order_manager.get_current_order()
    assert order["name"] == "김치찌개"
    assert order["quantity"] == 2
    assert order["total_price"] == 16000

def test_select_menu_invalid_id():
    order_manager = OrderManager()
    result = order_manager.select_menu(99, 1)
    assert result is False

def test_select_menu_invalid_quantity():
    order_manager = OrderManager()
    result = order_manager.select_menu(1, 0)
    assert result is False

def test_select_menu_negative_quantity():
    order_manager = OrderManager()
    result = order_manager.select_menu(1, -1)
    assert result is False

def test_select_menu_string_id():
    order_manager = OrderManager()
    result = order_manager.select_menu("1", 1)
    assert result is False

def test_get_current_order_empty():
    order_manager = OrderManager()
    order = order_manager.get_current_order()
    assert order is None