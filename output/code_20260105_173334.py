class CoffeeMenu:
    def __init__(self):
        self.menu = {
            "라떼": 2500
        }

    def get_price(self, item_name):
        """메뉴 항목의 가격을 반환합니다."""
        try:
            return self.menu[item_name]
        except KeyError:
            raise ValueError(f"'{item_name}'은(는) 메뉴에 없습니다.")

    def add_item(self, item_name, price):
        """메뉴에 새 항목을 추가합니다."""
        if not isinstance(price, int) or price < 0:
            raise ValueError("가격은 0 이상의 정수여야 합니다.")
        self.menu[item_name] = price

    def remove_item(self, item_name):
        """메뉴에서 항목을 제거합니다."""
        try:
            del self.menu[item_name]
        except KeyError:
            raise ValueError(f"'{item_name}'은(는) 메뉴에 없습니다.")

    def list_menu(self):
        """메뉴 목록을 반환합니다."""
        return self.menu.copy()


# 테스트 코드
import pytest


def test_coffee_menu_get_price():
    menu = CoffeeMenu()
    assert menu.get_price("라떼") == 2500
    with pytest.raises(ValueError):
        menu.get_price("아메리카노")


def test_coffee_menu_add_item():
    menu = CoffeeMenu()
    menu.add_item("아메리카노", 2000)
    assert menu.get_price("아메리카노") == 2000
    with pytest.raises(ValueError):
        menu.add_item("에스프레소", -1000)


def test_coffee_menu_remove_item():
    menu = CoffeeMenu()
    menu.remove_item("라떼")
    with pytest.raises(ValueError):
        menu.get_price("라떼")


def test_coffee_menu_list_menu():
    menu = CoffeeMenu()
    menu.add_item("아메리카노", 2000)
    menu_list = menu.list_menu()
    assert "라떼" in menu_list
    assert "아메리카노" in menu_list
    assert menu_list["라떼"] == 2500
    assert menu_list["아메리카노"] == 2000