from behave import *
# from player import Player
from dicts.weapons_skills import *

@given('a new Player with a {weapon}')
def step_impl(context, weapon):
  try:
    context.player = Player('Bori', 10, WEAPONS[weapon])
  except Exception as e:
    context.exc = e

@then('the player should be initialized with a {weapon}')
def step_impl(context, weapon):
  assert context.player.name == 'Bori'
  assert context.player.max_hp == 10
  assert context.player.hp == context.player.max_hp
  assert context.player.alive
  assert context.player.action == 'hit'
  assert context.player.weapon == WEAPONS[weapon]
  assert context.player.dmg == WEAPONS[weapon][DMG]
  assert context.player.weapon_verb == WEAPONS[weapon][VERB]
  assert context.player.skill == 0
  assert context.player.max_skill == 3

@then('throw a "{error}" for invalid weapon')
def step_impl(context, error):
  assert isinstance(context.exc, eval(error))
