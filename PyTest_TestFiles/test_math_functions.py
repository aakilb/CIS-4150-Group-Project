def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multipy(x, y):
    return x * y

def divide(x, y):
    return x / y

def test_addition():
    assert add(2, 3) == 5
    assert add(-3, 3) == 0

def test_subtration():
    assert subtract(9, 6) == 3
    assert subtract (10, -5) == 15

def test_multiplication():
    assert multipy(3, 9) == 27
    assert multipy(4, 20) == 80

def test_division():
    assert divide(12, 4) == 3
    assert divide(140, 7) == 20