import pytest
from lion.calculator import add, multi
# from calculator import add, multi
def test_add():
    assert add(2, 3) == 5

def test_multi():
    assert multi(4,9) == 36
