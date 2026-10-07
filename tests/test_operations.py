from calculator.operations import Operations
from calculator.calculation import Calculation

def test_add():
    assert Operations.add(2,4) == 6

def test_subtract():
    assert Operations.subtract(4, 1) == 3

def test_multiply():
    assert Operations.multiply(4, 5) == 20

def test_divide():
    assert Operations.divide(10,2) == 5

def test_power_with_option():
    calculation = Calculation([3], Operations.power, exponent=4)

