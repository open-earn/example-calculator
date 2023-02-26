from src.calculator import Calculator
from random import randint

def test_sum(calculator: Calculator):
    a = randint(0, 10)
    b = randint(0, 10)
    
    result = calculator.sum(a,b)
    assert result == a+b