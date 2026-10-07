from math import sqrt

class Operations:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b

    @staticmethod
    def square(value):
        return value ** 2

    @staticmethod
    def sqrt(value):
        return sqrt(value)

    @staticmethod
    def sum(*values):
        if len(values) == 0:
            raise ValueError("Sum requires at least one value")
        return sum(values)
    
    