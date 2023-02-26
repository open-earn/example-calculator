import pytest
from src.calculator import Calculator, CalculatorImpl

@pytest.fixture
def calculator() -> Calculator:
    return CalculatorImpl()