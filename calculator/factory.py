from calculator.calculation import Calculation
from calculator.operations import Operations

class CaculcationFactory:
    operations = {
        "add": Operations.add,
        "subtract": Operations.subtract,
        "multiply": Operations.multiply,
        "divide": Operations.divide,

    }

    @staticmethod
    def create(name, a, b):
        name = name.strip().lower() 

        try:
            operation = CaculcationFactory.operations[name]
        except KeyError:
            raise ValueError(f"Unknown operation: {name}") from None
        return Calculation(a,b,operation)