from calculator.calculation import Calculation
from calculator.operations import Operations

class CalculationFactory:
    operations = {
        "add": Operations.add,
        "subtract": Operations.subtract,
        "multiply": Operations.multiply,
        "divide": Operations.divide,
        "square": Operations.square,
        "sqrt": Operations.sqrt,
        "sum": Operations.sum,
        "power": Operations.power,
        "scale": Operations.scale,
    }
    operand_counts = {
        "add": 2,
        "subtract": 2,
        "multiply": 2,
        "divide": 2,
        "square": 1,
        "sqrt": 1,
        "power": 1,
        "scale": 1,

    }

    @staticmethod
    def create(name, *values, **options):
        name = name.strip().lower() 

        try:
            operation = CalculationFactory.operations[name]
        except KeyError:
            raise ValueError(f"Unknown operation: {name}") from None
        
        if name in CalculationFactory.operand_counts:
            expected = CalculationFactory.operand_counts[name]

            if len(values) != expected:
                raise ValueError(
                    f"{name} requires {expected} value(s)."
                )
        if name == "sum" and len(values) <1: 
            raise ValueError("sum requires at least one value")

        allowed_options = {
            "power": {"exponent"},
            "scale": {"factor"},
        }

        if name in allowed_options:
            allowed = allowed_options[name]

            for option in options:
                if option not in allowed:
                    raise ValueError(f"Unknown option: {option}")

                if "exponent" in options:
                    options["exponent"] = float(options["exponent"])

                if "factor" in options:
                    options["factor"] = float(options["factor"])
        
        return Calculation((values),operation,**options)