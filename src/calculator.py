from .interface import Calculator

class CalculatorImpl(Calculator):
    def sum(self, a: int, b: int) -> int:
        ...
