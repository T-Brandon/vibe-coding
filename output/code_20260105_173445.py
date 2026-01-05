# btn_Latte 기능 구현 (예: Latte 버튼 클릭 시 동작)

import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class LatteButton:
    """Latte 버튼 클래스"""

    def __init__(self):
        self.is_pressed = False

    def press(self):
        """Latte 버튼을 누름"""
        try:
            self.is_pressed = True
            logger.info("Latte 버튼이 눌렸습니다.")
            return True
        except Exception as e:
            logger.error(f"Latte 버튼 누르기 중 오류 발생: {e}")
            return False

    def release(self):
        """Latte 버튼을 뗌"""
        try:
            self.is_pressed = False
            logger.info("Latte 버튼이 떨어졌습니다.")
            return True
        except Exception as e:
            logger.error(f"Latte 버튼 떼기 중 오류 발생: {e}")
            return False

    def get_status(self):
        """현재 버튼 상태 반환"""
        return self.is_pressed


# pytest 테스트 코드
import pytest

def test_latte_button_press():
    btn = LatteButton()
    assert btn.press() is True
    assert btn.get_status() is True

def test_latte_button_release():
    btn = LatteButton()
    btn.press()
    assert btn.release() is True
    assert btn.get_status() is False

def test_latte_button_initial_status():
    btn = LatteButton()
    assert btn.get_status() is False