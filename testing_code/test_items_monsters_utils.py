from dicts.items import ITEMS, get_tag_items, COIN_VALUE
from dicts.monsters import MONSTER_SPECIES, COMBAT_LEVELS
from dicts.utils import use_an, typewriter
import pytest

@pytest.mark.initialize
def test_get_tag_items():
    item_names = ['apple', 'cake', 'bread', 'coin']
    food_items = get_tag_items(item_names, 'food')
    assert food_items == ['apple', 'cake', 'bread']

def test_coin_value():
    assert COIN_VALUE['coin'] == 1
    assert COIN_VALUE['gold coin'] == 7
    assert COIN_VALUE['coins sack'] == 10
    assert COIN_VALUE['gold coins sack'] == 70

def test_items_dict():
    assert 'apple' in ITEMS
    assert 'cake' in ITEMS
    assert 'bread' in ITEMS
    assert 'coin' in ITEMS

def test_monster_species():
    assert 'chicken' in MONSTER_SPECIES
    assert 'archer' in MONSTER_SPECIES
    assert 'spider' in MONSTER_SPECIES
    assert 'wolf' in MONSTER_SPECIES
    assert MONSTER_SPECIES['chicken'][3] == 'pinched'
    assert MONSTER_SPECIES['archer'][3] == 'shot'
    assert MONSTER_SPECIES['spbag'][1] == 999

def test_combat_levels():
    assert len(COMBAT_LEVELS) > 0
    assert isinstance(COMBAT_LEVELS[0], list)
    assert all(isinstance(monster, str) for level in COMBAT_LEVELS for monster in level)

def test_use_an():
    assert use_an('apple') == 'an'
    assert use_an('cake') == 'a'
    assert use_an('orange') == 'an'
    assert use_an('banana') == 'a'

def test_typewriter(capsys):
    text = 'This is a typewriter test.'
    typewriter(text, speed=1)
    captured = capsys.readouterr()
    assert captured.out == text