from behave import *
from monster import Monster
from dicts.monsters import give_monster

@given('give_monster {species}')
def step_impl(context, species):
  context.monster = give_monster(species, False)

@given('give special monster {species}')
def step_impl(context, species):
  context.monster = give_monster(species, True)

@then('the monster {name} should have HP={hp:d} DMG={dmg:d} Action={action}')
def step_impl(context, name, hp, dmg, action):
  assert isinstance(context.monster, Monster)
  print(context.monster.name)
  assert context.monster.name == name
  assert context.mosnter.hp == hp
  assert context.mosnter.max_hp == hp
  assert context.monster.dmg == dmg
  assert context.monster.action == action

@then('the monster {name} should have special name')
def step_impl(context, name):
  assert isinstance(context.monster, Monster)
  print(context.monster.name)
  assert context.monster.name == name
