from math import isfinite
from calculator.validation import numeric_value

class Calculation():
    def __init__(self, values, operation):
        self.values = tuple(values)
        self.operation = operation

    def get_result(self):
        result = self.operation(*self.values)

        if not isfinite(result):
            raise ValueError("Result must be finite")
        return result
