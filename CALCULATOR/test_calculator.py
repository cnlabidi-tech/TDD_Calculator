import pytest
from CALCULATOR.calculator import add

def test_empty_string_return_0():
    assert add("") == 0