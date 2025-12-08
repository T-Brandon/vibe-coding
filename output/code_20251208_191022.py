# reverse_string.py
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def reverse_string(input_str: str) -> str:
    """
    주어진 문자열을 뒤집어 반환합니다.
    :param input_str: 뒤집을 문자열
    :return: 뒤집힌 문자열
    """
    try:
        if not isinstance(input_str, str):
            raise TypeError("입력값은 문자열이어야 합니다.")
        reversed_str = input_str[::-1]
        logger.info("문자열 뒤집기 성공")
        return reversed_str
    except Exception as e:
        logger.exception(f"문자열 뒤집기 실패: {e}")
        raise