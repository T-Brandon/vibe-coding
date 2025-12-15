import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_order_label():
    """
    주문 정보를 표시하는 라벨 텍스트를 반환합니다.
    """
    try:
        label_text = "lbl_OrderInfo"
        logger.info("라벨 텍스트 반환 성공: %s", label_text)
        return label_text
    except Exception as e:
        logger.exception("라벨 텍스트 생성 중 오류 발생: %s", e)
        raise


# pytest 테스트
def test_get_order_label():
    result = get_order_label()
    assert isinstance(result, str)
    assert result == "lbl_OrderInfo"