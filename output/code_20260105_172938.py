def get_even_numbers(limit):
    """
    주어진 범위 내의 짝수를 리스트로 반환합니다.
    
    Args:
        limit (int): 범위의 상한 (포함)
    
    Returns:
        list: 짝수 리스트
    
    Raises:
        TypeError: 입력이 정수가 아닐 경우
        ValueError: 입력이 음수일 경우
    """
    import logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    try:
        if not isinstance(limit, int):
            raise TypeError("입력은 정수여야 합니다.")
        if limit < 0:
            raise ValueError("입력은 0 이상의 정수여야 합니다.")
        
        even_numbers = [i for i in range(0, limit + 1) if i % 2 == 0]
        logger.info(f"0부터 {limit}까지 짝수: {even_numbers}")
        return even_numbers
    
    except (TypeError, ValueError) as e:
        logger.error(f"입력 오류: {e}")
        raise