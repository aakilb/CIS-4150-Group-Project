from behave import *
from monster import Monster
from dicts.monsters import give_monster

@given('give_monster {species}')
def step_impl(context, species):
  context.monster = give_monster(species, False)

@given('give special monster {species}')
def step_impl(context, species):
  context.monster = give_monster(species, True)

@given('an opponent {species}')
def step_imp(context, species):
  context.opponent = give_monster(species)

@when('monster attacks opponent')
def step_imp(context):
  context.monster.attack(context.opponent)

@then('the monster {name} should have HP={hp:d} DMG={dmg:d} Action={action}')
def step_impl(context, name, hp, dmg, action):
  assert isinstance(context.monster, Monster)
  assert context.monster.name == name
  assert context.monster.hp == hp
  assert context.monster.max_hp == hp
  assert context.monster.dmg == dmg
  if action == "N/A":
    assert context.monster.action == ""
  else:
    assert context.monster.action == action
  assert context.monster.alive
  assert context.monster.length == 0

@then('the monster {name} should have special name')
def step_impl(context, name):
  assert isinstance(context.monster, Monster)
  assert context.monster.name.endswith(name)
  # TODO: Assert there is something before `name`?
  assert context.monster.name.find(name) > 0

@then('opponent took {dmg_taken:d} DMG')
def step_impl(context, dmg_taken):
  assert context.opponent.max_hp - context.opponent.hp == dmg_taken

@then('the opponent died')
def step_impl(context):
  assert context.opponent.hp <= 0
  assert context.opponent.alive == False
  assert context.opponent.name.startswith('Dead ')
