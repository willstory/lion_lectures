import pytest
from calculator import add, strange_func

def test_add():
    # assert 조건, 조건이 false면 나오는 구문
    assert add(5,10)==15
    assert add(11,-10)==1
    
def test_strange_func():
    assert strange_func(10, 8) == 1000
    assert strange_func(1, 8) == 1.6

@pytest.fixture
def setup_data():
    with open("data.txt","r") as f:
        content = f.read()
    return content

def test_use_fixture(setup_data):
    assert setup_data == "DB_Connect_Complete"

@pytest.mark.parametrize("a,b,result", [
    (1, 2, 3),
    (3, 3, 6),
    (10, 5, 15),
])
def test_add(a, b, result):
    assert add(a, b) == result

def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero!")
    return x / y

def test_divide_zero():
    with pytest.raises(ValueError, match="Division by zero!"):
        divide(10, 0)



# test_max.py
from max import find_max

def test_find_max():
    assert find_max([11, 2, 3, 4, 5]) == 11
    assert find_max([0, -1, -5, -3, -4]) == 0
