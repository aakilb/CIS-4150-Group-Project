import pytest
from monster import Monster
from dicts.monsters import give_monster
from dicts.monsters import MONSTER_VARIATION

'''
For demonstration purposes only.

Initializing monsters. 2 tests are explored here to demonstrate Pytest's features.
The first test uses fixtures to initialize the monsters. 4 fixtures are used to set 4
instance variables. Each fixture has a set of 4 values. Each value will be set with each other
value leading to 256 combinations(4^4). The second test uses parametrize to run 4 sets of instance
variables leading to just 4 tests. 


'''
@pytest.fixture(params=["Chicken","Guard","Bear","Punching-Bag"])
def monster_names(request):
    return request.param

@pytest.fixture(params=[1,2,4,10])
def monster_hp(request):
    return request.param

@pytest.fixture(params=[1,2,2,0])
def monster_dmg(request):
    return request.param

@pytest.fixture(params=["pinched","punched","slashed at","N/A"])
def monster_action(request):
    return request.param

#Initializing a monster (using fixtures). Checking to see if values were correctly set.
def test_initialize_fixture(monster_names,monster_hp,monster_dmg,monster_action):
    monster = Monster(monster_names, monster_hp, monster_dmg, action=monster_action)
    assert monster.name in ["Chicken","Guard","Bear","Punching-Bag"]
    assert monster.hp in [1,2,4,10]
    assert monster.dmg in [1,2,2,0]
    assert monster.action in ["pinched","punched","slashed at","N/A"]

#Initializing a monster (using parameterize). Checking to see if values were correctly set.
@pytest.mark.parametrize("monster_name, monster_hp, monster_dmg, monster_action",[("Chicken",1,1,"pinched"),("Guard",2,2,"punched"),("Bear",4,2,"slashed at"),("Punching-Bag",10,0,"N/A")])
def test_initialize_parametrize(monster_name,monster_hp,monster_dmg,monster_action):
    monster = Monster(monster_name, monster_hp, monster_dmg, action=monster_action)
    assert monster.name in ["Chicken","Guard","Bear","Punching-Bag"]
    assert monster.hp in [1,2,4,10]
    assert monster.dmg in [1,2,2,0]
    assert monster.action in ["pinched","punched","slashed at","N/A"]

'''
Controlling Monsters. 
Initializing monsters from a list and performing various actions.
'''

#Initialize Pre-set Monster
@pytest.mark.initialize
@pytest.mark.parametrize("monster_species, expected_monster_name, expected_hp, expected_dmg, expected_action",[("chicken","Chicken",1,1,"pinched"),("guard","Guard",2,2,"punched"),("bear","Bear",4,2,"slashed at"),("pbag","Punching-Bag",10,0,"N/A")])
def test_initialize(monster_species,expected_monster_name,expected_hp,expected_dmg,expected_action):
    monster = give_monster(monster_species, False)
    assert monster.name == expected_monster_name
    assert monster.hp == expected_hp
    assert monster.max_hp == expected_hp
    assert monster.dmg == expected_dmg
    assert monster.alive
    if expected_action == "N/A":
        assert monster.action == ""
    else:
        assert monster.action == expected_action
    assert monster.length == 12 #0

#Initialize Pre-set Monster with Special Name
@pytest.mark.initialize
@pytest.mark.parametrize("monster_species, expected_monster_name",[("chicken","Chicken"),("guard","Guard"),("bear","Bear"),("pbag","Punching-Bag")])
def test_initialize_special(monster_species, expected_monster_name):
    monster = give_monster(monster_species, True)
    assert monster.name.endswith(expected_monster_name)
    variation = MONSTER_VARIATION
    for word in variation:
        assert monster.name.find(word)

'''
Monster performing actions
'''       

#Setup for tests
@pytest.fixture
def monster_attack(request):
    monster = give_monster(request.param[0])
    opponent = give_monster(request.param[1])
    monster.attack(opponent)
    return monster,opponent

#Monster attacks an opponent
@pytest.mark.parametrize("monster_attack",[("chicken","pbag")], indirect=True)
def test_opponent(monster_attack):
    monster,opponent = monster_attack
    assert opponent.max_hp - opponent.hp == monster.dmg

#Monster kills an opponent
@pytest.mark.parametrize("monster_attack", [("guard","chicken")], indirect=True)
def test_opponent_kill(monster_attack):
    monster,opponent = monster_attack
    assert opponent.max_hp - opponent.hp == monster.dmg
    assert opponent.hp <=0
    assert opponent.alive == False
    assert opponent.name.startswith('Dead ')

'''
Display stats about monsters
'''

#Show Max Monster Stats
@pytest.mark.parametrize("monster_species,size", [("guard","max")])
def test_show_max(monster_species,size):
    monster = give_monster(monster_species)
    expected_status = "┌------┐\n|Guard |\n|HP:2  |\n|DMG:2 |\n└------┘"
    status = monster.show(size)
    assert status == expected_status

#Show Max Monster Stats
@pytest.mark.parametrize("monster_species,size", [("guard","min")])
def test_show_min(monster_species,size):
    monster = give_monster(monster_species)
    expected_status = """┌------------------------┐
|Guard |HP: ██ 2 |DMG: 2 |
└------------------------┘"""
    status = monster.show(size)
    assert status == expected_status

#Show Max Dead Monster Stats
@pytest.mark.parametrize("monster_species,size", [("guard","max")])
def test_show_dead_max(monster_species,size):
    monster = give_monster(monster_species)
    monster.hp = 0
    monster.update_data
    expected_status = """┌-----------┐
|Dead Guard |
└-----------┘"""
    status = monster.show(size)
    assert status == expected_status

#Show Min Dead Monster Stats
@pytest.mark.parametrize("monster_species,size", [("guard","min")])
def test_show_dead_min(monster_species,size):
    monster = give_monster(monster_species)
    monster.hp = 0
    monster.update_data
    expected_status = """┌-----------┐
|Dead Guard |
└-----------┘"""
    status = monster.show(size)
    assert status == expected_status








