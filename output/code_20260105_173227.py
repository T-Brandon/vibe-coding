import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_coffee_menu():
    """
    커피 메뉴 5가지를 반환하는 함수
    """
    coffee_menu = [
        "아메리카노",
        "카페라테",
        "카푸치노",
        "바닐라라테",
        "에스프레소"
    ]
    logger.info("커피 메뉴 5가지가 성공적으로 로드되었습니다.")
    return coffee_menu

# 테스트 코드
def test_get_coffee_menu():
    menu = get_coffee_menu()
    assert len(menu) == 5, "메뉴는 5가지 항목이어야 합니다."
    assert isinstance(menu, list), "반환 타입은 리스트여야 합니다."
    assert all(isinstance(item, str) for item in menu), "모든 메뉴 항목은 문자열이어야 합니다."
    logger.info("get_coffee_menu 테스트가 성공적으로 완료되었습니다.")