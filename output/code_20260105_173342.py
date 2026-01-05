# 에스프레소 가격 정보를 관리하는 클래스
class EspressoPriceManager:
    def __init__(self):
        self.price = 1800  # 원
        self.currency = "KRW"

    def get_price(self):
        """에스프레소 가격을 반환합니다."""
        return self.price

    def get_price_with_currency(self):
        """가격과 통화를 함께 반환합니다."""
        return f"{self.price} {self.currency}"

    def set_price(self, new_price):
        """에스프레소 가격을 업데이트합니다."""
        if not isinstance(new_price, int) or new_price < 0:
            raise ValueError("가격은 양의 정수여야 합니다.")
        self.price = new_price
        return self.price


# 테스트 코드
import pytest


def test_espresso_price_manager():
    manager = EspressoPriceManager()

    # 기본 가격 확인
    assert manager.get_price() == 1800
    assert manager.get_price_with_currency() == "1800 KRW"

    # 가격 변경 테스트
    new_price = 2000
    assert manager.set_price(new_price) == new_price

    # 유효하지 않은 가격 설정 시 예외 발생 테스트
    with pytest.raises(ValueError):
        manager.set_price(-100)

    with pytest.raises(ValueError):
        manager.set_price("invalid")