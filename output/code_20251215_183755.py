# file: calculator.py
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CalculatorError(Exception):
    """Custom exception for calculator errors."""
    pass

class Calculator:
    def add(self, a: float, b: float) -> float:
        try:
            result = a + b
            logger.info(f"Adding {a} + {b} = {result}")
            return result
        except Exception as e:
            logger.error(f"Addition failed: {e}")
            raise CalculatorError("Addition operation failed") from e

    def subtract(self, a: float, b: float) -> float:
        try:
            result = a - b
            logger.info(f"Subtracting {a} - {b} = {result}")
            return result
        except Exception as e:
            logger.error(f"Subtraction failed: {e}")
            raise CalculatorError("Subtraction operation failed") from e

    def multiply(self, a: float, b: float) -> float:
        try:
            result = a * b
            logger.info(f"Multiplying {a} * {b} = {result}")
            return result
        except Exception as e:
            logger.error(f"Multiplication failed: {e}")
            raise CalculatorError("Multiplication operation failed") from e

    def divide(self, a: float, b: float) -> float:
        try:
            if b == 0:
                raise CalculatorError("Division by zero is not allowed.")
            result = a / b
            logger.info(f"Dividing {a} / {b} = {result}")
            return result
        except CalculatorError:
            logger.error("Attempted division by zero.")
            raise
        except Exception as e:
            logger.error(f"Division failed: {e}")
            raise CalculatorError("Division operation failed") from e