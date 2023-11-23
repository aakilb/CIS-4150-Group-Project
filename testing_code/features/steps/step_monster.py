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
def step_impl(context, species):
  context.opponent = give_monster(species)

@given('the monster is dead')
def step_impl(context):
  context.monster.hp = 0
  context.monster.update_data()

@when('monster attacks opponent')
def step_impl(context):
  context.monster.attack(context.opponent)

@when('show monster "{size}" stats')
def step_impl(context, size):
  context.show_status = context.monster.show(size)

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
  names = context.monster.name.split(' ')
  assert len(names) == 2
  # Assert the name is correct
  assert names[1] == name
  # Check if special name is one of the valid options
  is_variation = False
  for r in context.table:
    if names[0] == r["variation"]:
      is_variation = True
  assert is_variation

@then('opponent took {dmg_taken:d} DMG')
def step_impl(context, dmg_taken):
  assert context.opponent.max_hp - context.opponent.hp == dmg_taken

@then('the opponent died')
def step_impl(context):
  assert context.opponent.hp <= 0
  assert context.opponent.alive == False
  assert context.opponent.name.startswith('Dead ')

@then('the monster status should be visible')
def step_impl(context):
  # NOTE: the newline characters are different - so remove them
  show_status = context.show_status.splitlines()
  text = context.text.splitlines()
  assert show_status == text, f"{show_status} {text}"

@then('the monster status should not be visible')
def step_impl(context):
  assert context.show_status == None
