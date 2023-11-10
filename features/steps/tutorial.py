from behave import *
from mathtesting import *

@given('we have 2 numbers to calculate')
def step_impl(context):
    context.mathtest = Mathtesting()

@when('we add them together')
def step_impl(context):
    context.mathtest.add()

@then('the result will be 7')
def step_impl(context):
    assert context.mathtest.add() == 7