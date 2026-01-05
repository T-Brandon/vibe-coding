class CoffeeMenu:
    def __init__(self):
        self.menu = {
            "아메리카노": 3500,
            "카페라떼": 4500,
            "카푸치노": 4500,
            "모카": 5000,
            "바닐라라떼": 5500,
            "초콜릿무스": 6000,
            "에스프레소": 3000,
            "아이스티": 4000,
            "레몬에이드": 4500,
            "딸기스무디": 5500
        }

    def get_menu(self):
        """메뉴와 가격을 반환합니다."""
        return self.menu

    def get_price(self, item_name):
        """지정된 메뉴 항목의 가격을 반환합니다."""
        try:
            return self.menu[item_name]
        except KeyError:
            raise ValueError(f"'{item_name}'은(는) 메뉴에 없습니다.")

    def add_item(self, item_name, price):
        """새로운 메뉴 항목을 추가합니다."""
        if not isinstance(price, int) or price <= 0:
            raise ValueError("가격은 양의 정수여야 합니다.")
        self.menu[item_name] = price

    def remove_item(self, item_name):
        """메뉴에서 항목을 제거합니다."""
        if item_name not in self.menu:
            raise ValueError(f"'{item_name}'은(는) 메뉴에 없습니다.")
        del self.menu[item_name]


# 테스트 코드
import pytest


def test_coffee_menu_initialization():
    menu = CoffeeMenu()
    assert len(menu.get_menu()) == 10
    assert menu.get_price("아메리카노") == 3500


def test_get_price_valid_item():
    menu = CoffeeMenu()
    assert menu.get_price("카페라떼") == 4500


def test_get_price_invalid_item():
    menu = CoffeeMenu()
    with pytest.raises(ValueError, match="메뉴에 없습니다"):
        menu.get_price("존재하지 않는 음료")


def test_add_item():
    menu = CoffeeMenu()
    menu.add_item("아이스아메리카노", 4000)
    assert menu.get_price("아이스아메리카노") == 4000


def test_add_item_invalid_price():
    menu = CoffeeMenu()
    with pytest.raises(ValueError, match="양의 정수여야 합니다"):
        menu.add_item("테스트음료", -1000)


def test_remove_item():
    menu = CoffeeMenu()
    menu.remove_item("에스프레소")
    with pytest.raises(ValueError, match="메뉴에 없습니다"):
        menu.get_price("에스프레소")


def test_remove_item_not_exists():
    menu = CoffeeMenu()
    with pytest.raises(ValueError, match="메뉴에 없습니다"):
        menu.remove_item("존재하지 않는 음료")