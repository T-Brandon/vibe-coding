import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class QuantityInputHandler:
    """입력란: txt_Quantity 값을 검증하고 처리하는 클래스"""

    def __init__(self):
        self.quantity = 0

    def set_quantity(self, value: str):
        """수량 입력값 검증 및 저장"""
        try:
            cleaned_value = value.strip()
            if not cleaned_value.isdigit():
                raise ValueError("수량은 숫자만 입력 가능합니다.")
            int_value = int(cleaned_value)
            if int_value < 0:
                raise ValueError("수량은 음수일 수 없습니다.")
            self.quantity = int_value
            logger.info(f"수량이 성공적으로 설정되었습니다: {self.quantity}")
        except Exception as e:
            logger.error(f"수량 입력 오류: {e}")
            raise

    def get_quantity(self) -> int:
        """현재 설정된 수량 반환"""
        return self.quantity