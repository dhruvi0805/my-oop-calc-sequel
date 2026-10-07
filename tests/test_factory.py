from calculator.factory import CaculcationFactory
from calculator.calculation import Calculation

def test_create_add_returns_calc():
    calculation = CaculcationFactory.create("add",2,3)

    assert isinstance(calculation, Calculation)
    assert calculation.get_result() == 5

def test_create_subtract_calc():
    calculation = CaculcationFactory.create("subtract", 5,2)

    assert isinstance(calculation, Calculation)
    assert calculation.get_result() == 3

def test_create_multiply_calc():
    calculation = CaculcationFactory.create("multiply", 5,2)

    assert isinstance(calculation,Calculation)
    assert calculation.get_result() == 10

def test_create_divide_calc():
    calculation = CaculcationFactory.create("Divide", 6,3)

    assert isinstance(calculation, Calculation)
    assert calculation.get_result() == 2

def test_divide_no_execution():
    calculation = CaculcationFactory.create("divide",10,0)

    assert isinstance(calculation,Calculation)

def test_divide_by_zero():
    calculation = CaculcationFactory.create("divide", 3,0)

    try:
        calculation.get_result()
        assert False
    except ZeroDivisionError:
        assert True

def test_invalid_name():
    try:
        CaculcationFactory.create("banana",2,3)
        assert False
    except ValueError:
        assert True