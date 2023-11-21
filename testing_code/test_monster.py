import pytest
from monster import Monster

'''
Initializing monsters. 2 tests are explored here to demonstrate Pytest's features.
The first test uses fixtures to initialize the monsters. 4 fixtures are used to set 4
instance variables. Each fixture has a set of 4 values. Each value will be set with each other
value leading to 256 combinations(4^4). The second test uses parametrize to run 4 sets of instance
variables leading to just 4 tests. 

Note: For demonstration purposes only. The second method would likely be a better way to test initialization, unless
you want to cover many scenarios.
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

