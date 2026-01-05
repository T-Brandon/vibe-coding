class Beverage:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def get_info(self) -> dict:
        return {"name": self.name, "price": self.price}


class Menu:
    def __init__(self):
        self.items = {}

    def add_item(self, beverage: Beverage):
        self.items[beverage.name] = beverage

    def get_item(self, name: str) -> Beverage:
        if name not in self.items:
            raise KeyError(f"{name}은(는) 메뉴에 없습니다.")
        return self.items[name]

    def list_items(self) -> list:
        return [item.get_info() for item in self.items.values()]


# 테스트 코드
import pytest
import logging

logging.basicConfig(level=logging.INFO)


def test_beverage_creation():
    latte = Beverage("바닐라라떼", 2800)
    assert latte.name == "바닐라라떼"
    assert latte.price == 2800
    assert latte.get_info() == {"name": "바닐라라떼", "price": 2800}


def test_menu_add_and_get_item():
    menu = Menu()
    latte = Beverage("바닐라라떼", 2800)
    menu.add_item(latte)

    retrieved = menu.get_item("바닐라라떼")
    assert retrieved.name == "바닐라라떼"
    assert retrieved.price == 2800

    with pytest.raises(KeyError):
        menu.get_item("존재하지않는음료")


def test_menu_list_items():
    menu = Menu()
    latte = Beverage("바닐라라떼", 2800)
    menu.add_item(latte)

    items = menu.list_items()
    assert len(items) == 1
    assert items[0] == {"name": "바닐라라떼", "price": 2800}