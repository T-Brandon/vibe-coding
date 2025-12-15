# calculator.py
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Calculator:
    """간단한 사칙연산 계산기 클래스"""

    def add(self, a: float, b: float) -> float:
        try:
            result = a + b
            logger.info(f"Add: {a} + {b} = {result}")
            return result
        except Exception as e:
            logger.exception("Error in add method")
            raise

    def subtract(self, a: float, b: float) -> float:
        try:
            result = a - b
            logger.info(f"Subtract: {a} - {b} = {result}")
            return result
        except Exception as e:
            logger.exception("Error in subtract method")
            raise

    def multiply(self, a: float, b: float) -> float:
        try:
            result = a * b
            logger.info(f"Multiply: {a} * {b} = {result}")
            return result
        except Exception as e:
            logger.exception("Error in multiply method")
            raise

    def divide(self, a: float, b: float) -> float:
        try:
            if b == 0:
                raise ValueError("Division by zero is not allowed.")
            result = a / b
            logger.info(f"Divide: {a} / {b} = {result}")
            return result
        except Exception as e:
            logger.exception("Error in divide method")
            raise