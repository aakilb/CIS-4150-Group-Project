import pytest
from dicts.weapons_skills import *
from dicts.monsters import give_monster

'''
Controlling Players.
'''

#Initialize a Player with a bow,a fist, and an invalid weapon
@pytest.mark.parametrize("name,hp,weaponselect",[("Bori",10, "bow"),("Bori",10,"fist"),("Bori",10,"invalid_weapon")])
def test_initialize_player(name,hp,weaponselect):
    player = Player(name,hp,WEAPONS[weaponselect])
    assert player.name == 'Bori'
    assert player.max_hp == 10
    assert player.hp == player.max_hp
    assert player.alive
    assert player.action == 'hit'
    assert player.weapon == WEAPONS[weaponselect]
    assert player.dmg == WEAPONS[weaponselect][DMG]
    assert player.weapon_verb == WEAPONS[weaponselect][VERB]
    assert player.skill == 0
    assert player.max_skill == 3

#Player attacks a Monster

