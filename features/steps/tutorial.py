from behave import *
from mathtesting import *

@given('we have 2 numbers to calculate')
def step_impl(context):
    context.mathtest = Mathtesting()

@when('we add them together')
def step_impl(context):
    context.mathtest.add(2, 5)

@then('the result will be 7')
def step_impl(context):
    assert context.mathtest.add(2, 5) == 7

@given('A calculator')
def step_impl(context)
    context.calculator = Mathtesting()

@then('The sum of {a:d} and {b:d} is {sum:d}')
def step_impl(context, a, b, sum)
    assert context.calculator.add(a, b) == sum
