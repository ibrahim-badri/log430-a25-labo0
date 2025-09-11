"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

# Please note that documentation is for my personal understanding. 
import pytest 
from calculator import Calculator

"""
Python fixture which creates and returns a new Calculator object.
Any test function that might includes calculator as a parameter
will automatically receive this object, hence avoiding creating a Calculator Object
for each test function.
    
Returns :
    calculator (Calculator) : a calculator object.  
"""
@pytest.fixture
def calculator():
    return Calculator()


"""
Verify that get_hello_message returns 'Calculatrice'.

Args:
    calculator (Calculator): Fixture providing a Calculator instance.
"""
def test_app(calculator):
    assert calculator.get_hello_message() == "== Calculatrice v1.0 =="

"""
Test addition with two values using parametrize.

Args:
    calc (Calculator): Fixture providing a Calculator instance.
    a (float): First operand.
    b (float): Second operand.
    expected (float): Expected sum of a and b.
"""
@pytest.mark.parametrize("value_one, value_two, expected_result", [(1, 2, 3),])
def test_addition(calculator, value_one, value_two, expected_result):
    assert calculator.addition(value_one, value_two) == expected_result
    assert calculator.last_result == expected_result
    
"""
Test subtraction with two values using parametrize.

Args:
    calculator (Calculator): Fixture providing a Calculator instance.
    value_one (float): Minuend (the value to subtract from).
    value_two (float): Subtrahend (the value to subtract).
    expected_result (float): Expected difference (value_one - value_two).
"""
@pytest.mark.parametrize("value_one, value_two, expected_result", [(0, 0, 0),])
def test_subtraction(calculator, value_one, value_two, expected_result):
    assert calculator.subtraction(value_one, value_two) == pytest.approx(expected_result)
    assert calculator.last_result == pytest.approx(expected_result)

"""
Test multiplication with two values using parametrize.

Args:
    calculator (Calculator): Fixture providing a Calculator instance.
    value_one (float): First factor.
    value_two (float): Second factor.
    expected_result (float): Expected product (value_one * value_two).
"""
@pytest.mark.parametrize("value_one, value_two, expected_result", [(0, 1, 0),])
def test_multiplication(calculator, value_one, value_two, expected_result):
    assert calculator.multiplication(value_one, value_two) == pytest.approx(expected_result)
    assert calculator.last_result == pytest.approx(expected_result)

"""
Test division with valid non-zero denominator.

Args:
    calculator (Calculator): Fixture providing a Calculator instance.
"""
def test_division_ok(calculator):
    assert calculator.division(100, 2) == 50
    assert calculator.last_result == 50
    
    
"""
Test division by zero according to the current implementation.

Note:
    The code does not raise an exception. It returns the string.

Args:
    calculator (Calculator): Fixture providing a Calculator instance.
"""
def test_division_by_zero_contract(calculator):
    ret = calculator.division(1, 0)
    assert ret == "Erreur : division par zéro"
    assert calculator.last_result == "Error"

"""
Test that division by zero raises ZeroDivisionError.

Note:
    This test is intentionally false: the current implementation
    returns a string instead of raising. As a result, this test fails.

Args:
    calculator (Calculator): Fixture providing a Calculator instance.
"""
def test_division_by_zero_should_raise(calculator):
    with pytest.raises(ZeroDivisionError):
        calculator.division(1, 0)