from behave import *
from mathtesting import *

@given('we have 2 numbers to calculate: {a:d} and {b:d}')
def step_impl(context, a, b):
    # given 2 numbers
    context.num1 = a
    context.num2 = b

@given('a calculator')
def step_impl(context):
    # create the instance of Mathtesting
    context.mathtest = Mathtesting()

@when('we add them together')
def add_two_numbers(context):
    # perform the add method
    context.result = context.mathtest.add(context.num1, context.num2)

@when('we multiply them together')
def multiply_two_numbers(context):
    # perform the multiply method
    context.result = context.mathtest.multiply(context.num1, context.num2)

@then('the result will be {results:d}')
def step_impl(context, results):
    # assert the results match the expected value
    assert context.result == results, f"{context.result} != {results}"
