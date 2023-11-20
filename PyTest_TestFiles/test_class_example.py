class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multipy(self, x, y):
        return x * y
    
    def divide(self, x, y):
        return x / y
    
def test_addition():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-3, 3) == 0

def test_subtration():
    calc = Calculator()
    assert calc.subtract(9, 6) == 3
    assert calc.subtract (10, -5) == 15

def test_multiplication():
    calc = Calculator()
    assert calc.multipy(3, 9) == 27
    assert calc.multipy(4, 20) == 80

def test_division():
    calc = Calculator()
    assert calc.divide(12, 4) == 3
    assert calc.divide(140, 7) == 20