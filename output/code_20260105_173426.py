# UI 요소 설계 기준 (PowerPoint / Excel 목업 기준)에 따라 구현된 Python 클래스

import logging
from typing import Dict, Any, Optional

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UIElement:
    """
    UI 요소 기본 클래스
    PowerPoint / Excel 목업 기준에 따라 속성과 동작을 정의합니다.
    """

    def __init__(
        self,
        name: str,
        position: Dict[str, int],
        size: Dict[str, int],
        color: str = "#FFFFFF",
        is_visible: bool = True,
        tooltip: Optional[str] = None
    ):
        """
        UI 요소 초기화

        :param name: 요소 이름
        :param position: 위치 (x, y)
        :param size: 크기 (width, height)
        :param color: 배경 색상 (기본: 흰색)
        :param is_visible: 가시성 여부
        :param tooltip: 툴팁 텍스트 (선택 사항)
        """
        self.name = name
        self.position = position
        self.size = size
        self.color = color
        self.is_visible = is_visible
        self.tooltip = tooltip
        logger.info(f"UI 요소 '{self.name}'이(가) 초기화되었습니다.")

    def set_position(self, x: int, y: int) -> None:
        """
        UI 요소의 위치를 설정합니다.

        :param x: X 좌표
        :param y: Y 좌표
        """
        try:
            self.position = {"x": x, "y": y}
            logger.info(f"'{self.name}' 위치가 ({x}, {y})로 업데이트되었습니다.")
        except Exception as e:
            logger.error(f"위치 설정 중 오류 발생: {e}")
            raise

    def set_size(self, width: int, height: int) -> None:
        """
        UI 요소의 크기를 설정합니다.

        :param width: 너비
        :param height: 높이
        """
        try:
            self.size = {"width": width, "height": height}
            logger.info(f"'{self.name}' 크기가 ({width}x{height})로 업데이트되었습니다.")
        except Exception as e:
            logger.error(f"크기 설정 중 오류 발생: {e}")
            raise

    def set_color(self, color: str) -> None:
        """
        UI 요소의 색상을 설정합니다.

        :param color: 색상 코드 (예: #FF0000)
        """
        try:
            self.color = color
            logger.info(f"'{self.name}' 색상이 {color}로 변경되었습니다.")
        except Exception as e:
            logger.error(f"색상 설정 중 오류 발생: {e}")
            raise

    def toggle_visibility(self) -> None:
        """
        UI 요소의 가시성을 토글합니다.
        """
        try:
            self.is_visible = not self.is_visible
            status = "표시됨" if self.is_visible else "숨김"
            logger.info(f"'{self.name}'이(가) {status} 상태로 변경되었습니다.")
        except Exception as e:
            logger.error(f"가시성 토글 중 오류 발생: {e}")
            raise

    def get_properties(self) -> Dict[str, Any]:
        """
        UI 요소의 현재 속성을 반환합니다.

        :return: 속성 딕셔너리
        """
        return {
            "name": self.name,
            "position": self.position,
            "size": self.size,
            "color": self.color,
            "is_visible": self.is_visible,
            "tooltip": self.tooltip
        }


# 테스트 코드 (pytest 기반)
import pytest

def test_ui_element_creation():
    """UI 요소 생성 테스트"""
    element = UIElement(
        name="Button1",
        position={"x": 10, "y": 20},
        size={"width": 100, "height": 50},
        color="#FF0000",
        is_visible=True,
        tooltip="Click me!"
    )
    assert element.name == "Button1"
    assert element.position == {"x": 10, "y": 20}
    assert element.size == {"width": 100, "height": 50}
    assert element.color == "#FF0000"
    assert element.is_visible is True
    assert element.tooltip == "Click me!"

def test_set_position():
    """위치 설정 테스트"""
    element = UIElement("TestElement", {"x": 0, "y": 0}, {"width": 50, "height": 50})
    element.set_position(100, 200)
    assert element.position == {"x": 100, "y": 200}

def test_set_size():
    """크기 설정 테스트"""
    element = UIElement("TestElement", {"x": 0, "y": 0}, {"width": 50, "height": 50})
    element.set_size(300, 150)
    assert element.size == {"width": 300, "height": 150}

def test_set_color():
    """색상 설정 테스트"""
    element = UIElement("TestElement", {"x": 0, "y": 0}, {"width": 50, "height": 50})
    element.set_color("#00FF00")
    assert element.color == "#00FF00"

def test_toggle_visibility():
    """가시성 토글 테스트"""
    element = UIElement("TestElement", {"x": 0, "y": 0}, {"width": 50, "height": 50}, is_visible=True)
    element.toggle_visibility()
    assert element.is_visible is False
    element.toggle_visibility()
    assert element.is_visible is True

def test_get_properties():
    """속성 조회 테스트"""
    element = UIElement(
        name="Button1",
        position={"x": 10, "y": 20},
        size={"width": 100, "height": 50},
        color="#FF0000",
        is_visible=True,
        tooltip="Click me!"
    )
    props = element.get_properties()
    assert props["name"] == "Button1"
    assert props["position"] == {"x": 10, "y": 20}
    assert props["size"] == {"width": 100, "height": 50}
    assert props["color"] == "#FF0000"
    assert props["is_visible"] is True
    assert props["tooltip"] == "Click me!"