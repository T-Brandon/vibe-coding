def greet_user(name: str) -> str:
    """
    Simple greeting function.
    """
    try:
        if not name:
            raise ValueError("Name cannot be empty.")
        greeting = f"Hello, {name}! I'm Chat‑T."
        return greeting
    except Exception as e:
        import logging
        logging.exception("Error occurred in greet_user.")
        return f"Error: {str(e)}"


# pytest test
def test_greet_user_valid():
    assert "Hello" in greet_user("Alex")


def test_greet_user_empty():
    assert "Error" in greet_user("")