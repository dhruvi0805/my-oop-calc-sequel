from math import sqrt, pow

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

    @staticmethod
    def power(value,*,exponent =2):
        return pow(value, exponent)

    @staticmethod
    def scale(value, *, factor=1):
        if factor == 0:
            raise ValueError("factor cannot be zero")
        return value / factor
    
    