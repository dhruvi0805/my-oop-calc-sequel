from math import isfinite

def numeric_value(values):
    numbers = []
    
    for value in values:
        try:
            number = float(value)
        except (TypeError, ValueError):
            raise ValueError("values must be numeric")

        if not isfinite(number):
            raise ValueError("Values must be finite")

        numbers.append(number)

    return tuple(numbers)