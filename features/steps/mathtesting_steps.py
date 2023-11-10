from behave import *
from mathtesting import *

@given('we have 2 numbers to calculate')
def step_impl(context):
    context.mathtest = Mathtesting()

@given('a calculator')
def step_impl(context):
    context.calculator = Mathtesting()

@when('we add them together')
def step_impl(context):
    context.mathtest.add(2, 5)

@then('the result will be 7')
def step_impl(context):
    assert context.mathtest.add(2, 5) == 7

@then('the sum of {a:d} and {b:d} is {sum:d}')
def step_impl(context, a, b, sum):
    assert context.calculator.add(a, b) == sum

@then('the product of {a:d} and {b:d} is {product:d}')
def step_impl(context, a, b, product):
    assert context.calculator.multiply(a, b) == product
