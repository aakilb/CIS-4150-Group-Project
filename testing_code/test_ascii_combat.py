from dicts.weapons_skills import *
from dicts.rooms import *
from dicts.utils import *
from dicts.monsters import give_monster
import combat, dungeon, sys
import pytest

@pytest.mark.initialize
def test_player():
    player = Player('TestPlayer', 20, WEAPONS[SWORD])
    assert player.name == 'TestPlayer'
    assert player.hp == 20
    assert player.weapon == WEAPONS[SWORD]