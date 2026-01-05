class Beverage:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"<Beverage: {self.name}, {self.price}원>"

# 카라멜마키아토 메뉴项
caramel_macchiato = Beverage("카라멜마키아토", 3000)

# 테스트 코드
def test_beverage_creation():
    assert caramel_macchiato.name == "카라멜마키아토"
    assert caramel_macchiato.price == 3000
    assert str(caramel_macchiato) == "<Beverage: 카라멜마키아토, 3000원>"