from mathutils import add

def test_add():
    assert add(2, 3) == 5

import pytest
from mathutils import factorial

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)

"""
Task 1: In test_mathutils.py, write 3 tests for is_prime. Check is_prime(2) is True, is_prime(9) is False, and is_prime(1) is False.

Task 2: Write 2 tests for factorial. Check that factorial(5) equals 120, and that factorial(-1) raises a ValueError. Add the negative-number check to your function first.

Task 3: Run pytest and send me the output.
"""
import pytest
from mathutils import is_prime, factorial

def test_is_prime_true():
    assert is_prime(2)
    
def test_is_prime_false():
    assert not is_prime(9) 

def test_is_prime_one():
    assert not is_prime(1)

def test_factorial_value():
    assert factorial(5)==120
    
def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)

