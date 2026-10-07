from math import isfinite
from calculator.validation import numeric_value

class Calculation():
    def __init__(self, a, b, operation):
        numbers = numeric_value([a,b])
        self.a = numbers[0]
        self.b = numbers[1]
        self.operation = operation

    def get_result(self):
        result = self.operation(self.a, self.b)
        
        if not isfinite(result):
            raise ValueError("Result must be finite")
        return result
