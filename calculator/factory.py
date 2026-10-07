from calculator.calculation import Calculation
from calculator.operations import Operations

class CaculcationFactory:
    operations = {
        "add": Operations.add,
        "subtract": Operations.subtract,
        "multiply": Operations.multiply,
        "divide": Operations.divide,
        "square": Operations.square,
        "sqrt": Operations.sqrt,
        "sum": Operations.sum,
    }
    operand_counts = {
        "add": 2,
        "subtract": 2,
        "multiply": 2,
        "divide": 2,
        "square": 1,
        "sqrt": 1,
        "sum": 1,

    }

    @staticmethod
    def create(name, *values):
        name = name.strip().lower() 

        try:
            operation = CaculcationFactory.operations[name]
        except KeyError:
            raise ValueError(f"Unknown operation: {name}") from None
        
        if name in CaculcationFactory.operand_counts:
            expected = CaculcationFactory.operand_counts[name]

            if len(values) != expected:
                raise ValueError(
                    f"{name} requires {expected} value(s)."
                )
        
        return Calculation((values),operation)