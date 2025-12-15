# file: code_20251215_110624.py
import logging
from typing import List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AverageCalculator:
    """리스트 내 숫자의 평균을 계산하는 클래스"""

    @staticmethod
    def calculate(numbers: List[float]) -> float:
        try:
            if not numbers:
                raise ValueError("빈 리스트입니다.")
            avg = sum(numbers) / len(numbers)
            logger.info(f"평균 계산 완료: {avg}")
            return avg
        except Exception as e:
            logger.error(f"평균 계산 실패: {e}")
            raise


# pytest 테스트
def test_average_calculator_success():
    numbers = [10, 20, 30]
    assert AverageCalculator.calculate(numbers) == 20.0


def test_average_calculator_empty_list():
    try:
        AverageCalculator.calculate([])
    except ValueError as e:
        assert str(e) == "빈 리스트입니다."
    else:
        assert False, "ValueError가 발생해야 합니다."