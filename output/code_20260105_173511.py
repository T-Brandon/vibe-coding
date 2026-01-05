# btn_Vanilla 기능 구현 (TDD 기반)

import logging
from typing import Optional

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ButtonVanilla:
    """기본 버튼 기능 클래스"""

    def __init__(self, name: str, is_active: bool = False):
        """
        버튼 초기화

        Args:
            name (str): 버튼 이름
            is_active (bool): 활성화 상태 (기본: False)
        """
        self.name = name
        self.is_active = is_active
        logger.info(f"버튼 '{self.name}'이(가) 초기화되었습니다. 활성화 상태: {self.is_active}")

    def activate(self) -> bool:
        """
        버튼 활성화

        Returns:
            bool: 활성화 성공 여부
        """
        try:
            if self.is_active:
                logger.warning(f"버튼 '{self.name}'은(는) 이미 활성화 상태입니다.")
                return False

            self.is_active = True
            logger.info(f"버튼 '{self.name}'이(가) 활성화되었습니다.")
            return True

        except Exception as e:
            logger.error(f"버튼 '{self.name}' 활성화 중 오류 발생: {e}")
            return False

    def deactivate(self) -> bool:
        """
        버튼 비활성화

        Returns:
            bool: 비활성화 성공 여부
        """
        try:
            if not self.is_active:
                logger.warning(f"버튼 '{self.name}'은(는) 이미 비활성화 상태입니다.")
                return False

            self.is_active = False
            logger.info(f"버튼 '{self.name}'이(가) 비활성화되었습니다.")
            return True

        except Exception as e:
            logger.error(f"버튼 '{self.name}' 비활성화 중 오류 발생: {e}")
            return False

    def get_status(self) -> dict:
        """
        버튼 상태 반환

        Returns:
            dict: 버튼 상태 정보
        """
        return {
            "name": self.name,
            "is_active": self.is_active,
            "status": "active" if self.is_active else "inactive"
        }


# 테스트 코드
import pytest


def test_button_vanilla_init():
    """버튼 초기화 테스트"""
    button = ButtonVanilla("TestButton")
    assert button.name == "TestButton"
    assert button.is_active is False


def test_button_vanilla_activate():
    """버튼 활성화 테스트"""
    button = ButtonVanilla("TestButton")
    assert button.activate() is True
    assert button.is_active is True


def test_button_vanilla_deactivate():
    """버튼 비활성화 테스트"""
    button = ButtonVanilla("TestButton")
    button.activate()
    assert button.deactivate() is True
    assert button.is_active is False


def test_button_vanilla_status():
    """버튼 상태 확인 테스트"""
    button = ButtonVanilla("TestButton")
    status = button.get_status()
    assert status["name"] == "TestButton"
    assert status["is_active"] is False
    assert status["status"] == "inactive"


def test_button_vanilla_double_activate():
    """중복 활성화 테스트"""
    button = ButtonVanilla("TestButton")
    button.activate()
    assert button.activate() is False  # 이미 활성화됨


def test_button_vanilla_double_deactivate():
    """중복 비활성화 테스트"""
    button = ButtonVanilla("TestButton")
    assert button.deactivate() is False  # 이미 비활성화됨