import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class CoffeeMenu:
    def __init__(self):
        self.menu = {
            "아메리카노": 2000,
            "라떼": 2500,
            "에스프레소": 1800,
            "바닐라라떼": 2800,
            "카라멜마키아토": 3000
        }

    def get_price(self, coffee_name: str) -> int:
        """커피 이름으로 가격을 반환"""
        try:
            price = self.menu[coffee_name]
            logging.info(f"{coffee_name}의 가격은 {price}원입니다.")
            return price
        except KeyError:
            logging.error(f"'{coffee_name}'는 메뉴에 없습니다.")
            raise ValueError(f"'{coffee_name}'는 메뉴에 없습니다.")


# ------------------ Pytest 테스트 ------------------

import pytest

@pytest.fixture
def coffee_menu():
    return CoffeeMenu()

def test_get_price_valid(coffee_menu):
    assert coffee_menu.get_price("아메리카노") == 2000
    assert coffee_menu.get_price("라떼") == 2500

def test_get_price_invalid(coffee_menu):
    with pytest.raises(ValueError):
        coffee_menu.get_price("핫초코")