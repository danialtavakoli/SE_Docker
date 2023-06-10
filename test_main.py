import main

def test_multiply():
    assert main.multiply(2, 3) == 6
    assert main.multiply(0, 10) == 0
    assert main.multiply(-2, 4) == -8

def test_add():
    assert main.add(2, 3) == 5
    assert main.add(0, 0) == 0
    assert main.add(-2, 4) == 2

def test_divide():
    assert main.divide(10, 2) == 5.0
    assert main.divide(0, 10) == 0
    assert main.divide(-4, 2) == -2

def test_subtract():
    assert main.subtract(10, 2) == 8
    assert main.subtract(0, 0) == 0
    assert main.subtract(-4, 2) == -6
