from math import isfinite

class Calculation():
    def __init__(self, values, operation, **options):
        self.values = tuple(values)
        self.operation = operation
        self.options = dict(options)

    def get_result(self):
        result = self.operation(*self.values, **self.options)

        if not isfinite(result):
            raise ValueError("Result must be finite")
        return result
