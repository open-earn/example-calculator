import abc


class Calculator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def sum(self, a: int, b: int) -> int:
        ...
