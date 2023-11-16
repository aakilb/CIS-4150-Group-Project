from behave import *
from monster import Monster
from dicts.monsters import give_monster

@given('give_monster {species}')
def step_impl(context, species):
  context.monster = give_monster(species, False)

@then('the monster {name} should have HP={hp:d} DMG={dmg:d} Action={action}')
def step_impl(context, name, hp, dmg, action):
  assert isinstance(context.monster, Monster)
  # TODO: check variable values?
