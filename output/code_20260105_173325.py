class CoffeeMenu:
    def __init__(self):
        self.menu = {
            "아메리카노": 2000
        }

    def get_price(self, item_name):
        try:
            return self.menu[item_name]
        except KeyError:
            raise ValueError(f"'{item_name}'은(는) 메뉴에 없습니다.")

    def add_item(self, item_name, price):
        if not isinstance(price, int) or price < 0:
            raise ValueError("가격은 양의 정수여야 합니다.")
        self.menu[item_name] = price

    def remove_item(self, item_name):
        if item_name not in self.menu:
            raise ValueError(f"'{item_name}'은(는) 메뉴에 없습니다.")
        del self.menu[item_name]

    def list_menu(self):
        return self.menu.copy()


# 테스트 코드
import pytest


def test_coffee_menu_get_price():
    menu = CoffeeMenu()
    assert menu.get_price("아메리카노") == 2000

    with pytest.raises(ValueError):
        menu.get_price("라떼")


def test_coffee_menu_add_item():
    menu = CoffeeMenu()
    menu.add_item("라떼", 3000)
    assert menu.get_price("라떼") == 3000

    with pytest.raises(ValueError):
        menu.add_item("에스프레소", -1000)

    with pytest.raises(ValueError):
        menu.add_item("에스프레소", "3000")


def test_coffee_menu_remove_item():
    menu = CoffeeMenu()
    menu.remove_item("아메리카노")
    with pytest.raises(ValueError):
        menu.get_price("아메리카노")

    with pytest.raises(ValueError):
        menu.remove_item("라떼")


def test_coffee_menu_list_menu():
    menu = CoffeeMenu()
    menu.add_item("라떼", 3000)
    menu_list = menu.list_menu()
    assert len(menu_list) == 2
    assert menu_list["아메리카노"] == 2000
    assert menu_list["라떼"] == 3000