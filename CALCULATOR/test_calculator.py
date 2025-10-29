import pytest
from CALCULATOR.calculator import add

@pytest.mark.parametrize("n, expected", [
    ("", 0),
    ("1", 1),
])
def test_add(n, expected):
    assert add(n) == expected