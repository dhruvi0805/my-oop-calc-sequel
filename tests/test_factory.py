from calculator.factory import CalculationFactory
from calculator.calculation import Calculation

def test_create_add_returns_calc():
    calculation = CalculationFactory.create("add",2,3)

    assert isinstance(calculation, Calculation)
    assert calculation.get_result() == 5

def test_create_subtract_calc():
    calculation = CalculationFactory.create("subtract", 5,2)

    assert isinstance(calculation, Calculation)
    assert calculation.get_result() == 3

def test_create_multiply_calc():
    calculation = CalculationFactory.create("multiply", 5,2)

    assert isinstance(calculation,Calculation)
    assert calculation.get_result() == 10

def test_create_divide_calc():
    calculation = CalculationFactory.create("Divide", 6,3)

    assert isinstance(calculation, Calculation)
    assert calculation.get_result() == 2

def test_divide_no_execution():
    calculation = CalculationFactory.create("divide",10,0)

    assert isinstance(calculation,Calculation)

def test_divide_by_zero():
    calculation = CalculationFactory.create("divide", 3,0)

    try:
        calculation.get_result()
        assert False
    except ZeroDivisionError:
        assert True

def test_invalid_name():
    try:
        CalculationFactory.create("banana",2,3)
        assert False
    except ValueError:
        assert True

def test_create_sqrt():
    calculation =  CalculationFactory.create("sqrt", 4)

    assert isinstance(calculation, Calculation)
    assert calculation.get_result() == 2

def test_neg_sqrt():
    calculation = CalculationFactory.create("sqrt", -4)

    assert isinstance(calculation, Calculation)

    try:
        calculation.get_result()
        assert False
    except ValueError:
        assert True

def test_wrong_operand_count():
    try:
        CalculationFactory.create("sqrt", 4,9)
        assert False
    except ValueError:
        assert True

def test_invalid_option():
    try:
        CalculationFactory.create("power", 3, banana=4)
        assert False

    except ValueError:
        assert True

def test_scale_with_factor():
    calculation = CalculationFactory.create("scale",10,factor =2)
    assert calculation.get_result() == 5.0

def test_scale_factor_invalid():
    try:
        CalculationFactory.create("scale", 20, apple =2)
        assert False
    except ValueError:
        assert True

def test_scale_zero_factor():
    calculation = CalculationFactory.create("scale", 10, factor = 0)

    try:
        calculation.get_result()
        assert False

    except ValueError:
        assert True

