import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def greet_user(name: str) -> str:
    """
    사용자 이름을 받아 인사 메시지를 반환합니다.
    
    Args:
        name (str): 사용자 이름
    
    Returns:
        str: 인사 메시지
    
    Raises:
        TypeError: 이름이 문자열이 아닌 경우
    """
    try:
        if not isinstance(name, str):
            raise TypeError("이름은 문자열이어야 합니다.")
        message = f"안녕하세요, {name}님! 현대트랜시스에 오신 것을 환영합니다."
        logger.info(f"사용자 인사 완료: {name}")
        return message
    except Exception as e:
        logger.error(f"인사 메시지 생성 중 오류 발생: {e}")
        raise

# pytest 테스트 코드
def test_greet_user():
    """greet_user 함수 테스트"""
    assert greet_user("김철수") == "안녕하세요, 김철수님! 현대트랜시스에 오신 것을 환영합니다."
    assert greet_user("이영희") == "안녕하세요, 이영희님! 현대트랜시스에 오신 것을 환영합니다."

def test_greet_user_type_error():
    """greet_user 함수의 타입 에러 테스트"""
    try:
        greet_user(123)
    except TypeError as e:
        assert str(e) == "이름은 문자열이어야 합니다."
    else:
        assert False, "TypeError가 발생해야 합니다."

if __name__ == "__main__":
    # 테스트 실행
    import pytest
    pytest.main([__file__])