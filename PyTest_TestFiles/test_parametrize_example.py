class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

import pytest

@pytest.fixture
def calculator_instance():
    return Calculator()

@pytest.mark.parametrize('input1, input2, operation, expected', [
    (2, 3, 'add', 5),
    (-3, 3, 'add', 0),
    (9, 6, 'subtract', 3),
    (10, -5, 'subtract', 15),
    (3, 9, 'multiply', 27),
    (4, 20, 'multiply', 80),
    (12, 4, 'divide', 3),
    (140, 7, 'divide', 20)
])

def test_calculator(calculator_instance, input1, input2, operation, expected):
    calc = calculator_instance
    
    if operation == 'add':
        result = calc.add(input1, input2)
    elif operation == 'subtract':
        result = calc.subtract(input1, input2)
    elif operation == 'multiply':
        result = calc.multiply(input1, input2)
    elif operation == 'divide':
        result = calc.divide(input1, input2)
    else:
        raise ValueError(f'Invalid operation: {operation}')
    
    assert result == expected