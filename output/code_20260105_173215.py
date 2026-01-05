# ChatT: 현대트랜시스 백엔드 Python 엔지니어
# TDD 기반 코드 작성 및 테스트 포함

import logging
import pytest

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ExampleService:
    """예제 서비스 클래스"""

    def __init__(self):
        self.data = []

    def add_item(self, item):
        """데이터 리스트에 항목 추가"""
        try:
            if not isinstance(item, (str, int, float)):
                raise TypeError("item must be str, int, or float")
            self.data.append(item)
            logger.info(f"Added item: {item}")
            return True
        except Exception as e:
            logger.error(f"Error adding item: {e}")
            return False

    def get_items(self):
        """저장된 모든 항목 반환"""
        try:
            logger.info(f"Retrieved {len(self.data)} items")
            return self.data.copy()
        except Exception as e:
            logger.error(f"Error retrieving items: {e}")
            return []

# Pytest 테스트
def test_add_item_success():
    service = ExampleService()
    result = service.add_item("test")
    assert result is True
    assert "test" in service.get_items()

def test_add_item_invalid_type():
    service = ExampleService()
    result = service.add_item(None)
    assert result is False

def test_get_items():
    service = ExampleService()
    service.add_item("item1")
    service.add_item("item2")
    items = service.get_items()
    assert len(items) == 2
    assert "item1" in items
    assert "item2" in items

if __name__ == "__main__":
    pytest.main([__file__])