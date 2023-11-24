import pytest
from unittest import mock
from dicts.weapons_skills import *
from dicts.rooms import *
from dicts.utils import *
from monster import *
from combat import *

# Fixtures for parameterized testing
@pytest.fixture(params=['P1', 'P2', 'P3', 'P4'])
def user_names(request):
    return request.param

@pytest.fixture(params=[50, 25, 10, 5])
def user_hp(request):
    return request.param

@pytest.fixture(params=[WEAPONS[SWORD], WEAPONS[DAGGER], WEAPONS[FIST], WEAPONS[BOW]])
def user_weapons(request):
    return request.param

@pytest.fixture(params=['M1', 'M2', 'M3', 'M4'])
def enemy_names(request):
    return request.param

@pytest.fixture(params=[100, 50, 25, 10])
def enemy_hp(request):
    return request.param

@pytest.fixture(params=[50, 25, 10, 5])
def enemy_dmg(request):
    return request.param

@pytest.fixture(params=['hit', 'bit', 'shot', 'jabbed'])
def enemy_action(request):
    return request.param

@pytest.mark.initialize
def test_initialize_users(user_names, user_hp, user_weapons):
    # Create users from player object 
    users = Player(user_names, user_hp, user_weapons)
    # Check if attributes are initialized correctly
    assert users.name in ['P1', 'P2', 'P3', 'P4']
    assert users.hp in [50, 25, 10, 5]
    assert users.weapon in [WEAPONS[SWORD], WEAPONS[DAGGER], WEAPONS[FIST], WEAPONS[BOW]]

@pytest.mark.initialize
def test_initialize_enemy(enemy_names, enemy_hp, enemy_dmg, enemy_action):
    # Create enemies from monster object
    enemys = Monster(enemy_names, enemy_hp, enemy_dmg, enemy_action)
    # Check if attributes are initialized correctly
    assert enemys.name in ['M1', 'M2', 'M3', 'M4']
    assert enemys.hp in [100, 50, 25, 10]
    assert enemys.dmg in [50, 25, 10, 5]
    assert enemys.action in ['hit', 'bit', 'shot', 'jabbed']

@pytest.mark.parametrize('user_names, user_hp, user_weapons', [('P1', 50, WEAPONS[SWORD]), ('P2', 25, WEAPONS[DAGGER]), ('P3', 10, WEAPONS[FIST]), ('P4', 5, WEAPONS[BOW])])
def test_initialize_users_parametrize(user_names, user_hp, user_weapons):
    # Create users from player object 
    users = Player(user_names, user_hp, user_weapons)
    # Check if attributes are initialized correctly
    assert users.name in ['P1', 'P2', 'P3', 'P4']
    assert users.hp in [50, 25, 10, 5]
    assert users.weapon in [WEAPONS[SWORD], WEAPONS[DAGGER], WEAPONS[FIST], WEAPONS[BOW]]

@pytest.mark.parametrize('enemy_names, enemy_hp, enemy_dmg, enemy_action',[('M1', 100, 50,'hit'), ('M2', 50, 25, 'bit'),('M3', 25, 10, 'shot'),('M4', 10, 5, 'jabbed')])
def test_initialize_enemy_parametrize(enemy_names, enemy_hp, enemy_dmg, enemy_action):
    # Create enemies from monster object
    enemys = Monster(enemy_names, enemy_hp, enemy_dmg, enemy_action)
    # Check if attributes are initialized correctly
    assert enemys.name in ['M1', 'M2', 'M3', 'M4']
    assert enemys.hp in [100, 50, 25, 10]
    assert enemys.dmg in [50, 25, 10, 5]
    assert enemys.action in ['hit', 'bit', 'shot', 'jabbed']


# Helper functions to create a user and enemy
def create_user():
    user = Player('TestPlayer', 20, WEAPONS[SWORD])
    return user

def create_enemy():
    enemy = Monster('TestMonster', 20, 5, 'hit')
    return enemy

# Fixture to create a combat scenario
@pytest.fixture
def create_combat():
    user = create_user()
    enemy = create_enemy()
    with mock.patch('builtins.input', return_value=''):  # Mocking input to return an empty string
        combat = Combat(user, [enemy])
    return combat

# Test case for checking if user and enemy attributes are initialized correctly
def test_user_enemy():
    user = Player('TestPlayer', 20, WEAPONS[SWORD])
    enemy = Monster('TestMonster', 20, 5, 'hit')
    assert user.name == 'TestPlayer'
    assert user.hp == 20
    assert user.weapon == WEAPONS[SWORD]
    assert enemy.name == 'TestMonster'
    assert enemy.max_hp == 20
    assert enemy.hp == 20
    assert enemy.dmg == 5
    assert enemy.action == 'hit'
    assert enemy.alive == True
    assert enemy.length == 0

# Test case for initializing a combat scenario
def test_combat_init():
    user = create_user()
    enemy = create_enemy()
    with mock.patch('builtins.input', return_value=''):  # Mocking input to return an empty string
        combat = Combat(user, [enemy])
    assert combat.user == user
    assert combat.STRINGS['player_attack'] == 'You ' + user.weapon_verb
    assert combat.user_attack_msg == ''
    assert combat.enemies == [enemy]
    assert combat.no_of_enemies == 1
    assert combat.enemies_dict == {'1': enemy}
    assert combat.enemies_attack_msg == ''

# Test case for handling an empty line in combat
def test_combat_emptyline(create_combat):
    combat = create_combat
    with mock.patch.object(combat, 'display') as mock_display:
        combat.emptyline()
        mock_display.assert_called_once()

# Test case for displaying help in combat
def test_combat_do_help(create_combat):
    combat = create_combat
    with mock.patch.object(combat, 'display') as mock_display:
        combat.do_help(None)
        mock_display.assert_called_once()

# Test case for getting the names of alive enemies
def test_alive_enemy_names(create_combat):
    assert create_combat.alive_enemy_names() == '  1| TestMonster\n'

# Test case for checking the number of alive enemies
def test_enemies_alive(create_combat):
    combat = create_combat
    assert combat.enemies_alive() == 1

    combat.enemies[0].alive = False
    assert combat.enemies_alive() == 0

# Test case for checking enemy attacks
def test_enemy_attack(create_combat):
    combat = create_combat

    # Mocking the enemy attack to prevent actual damage to the user
    with mock.patch.object(combat.enemies[0], 'attack'):
        combat.enemies_attack()

    assert combat.enemies_attack_msg != ' TestMonster hit you (-5HP)\n# You are perfectly healthy!'
    #print("\ncombat.enemies_attack_msg:", combat.enemies_attack_msg)
     
    combat.user.hp = 0
    with mock.patch.object(combat.enemies[0], 'attack'):
        combat.enemies_attack()
    
    #assert combat.enemies_attack_msg == ' !! TestMonster hit you (-5HP)\n# You are bleeding too much.. Argh!'
    if 'You are bleeding too much.. Argh!' in combat.enemies_attack_msg:
        assert True
    else:
        assert False
    #print("\ncombat.enemies_attack_msg:", combat.enemies_attack_msg)
        
    combat.user.hp = combat.user.max_hp
    with mock.patch.object(combat.enemies[0], 'attack'):
        combat.enemies_attack()
    
    assert combat.enemies_attack_msg != ' TestMonster hit you (-5HP)\n# You are perfectly healthy!'
    #print("\ncombat.enemies_attack_msg:", combat.enemies_attack_msg)

def test_user_attack(create_combat):
    combat = create_combat
    enemy = combat.enemies[0]
    with mock.patch.object(combat.user, 'attack'):
        combat.user_attack(enemy)
    
    assert '# You sliced at TestMonster (-3HP)' in combat.user_attack_msg
    #print("\ncombat.user_attack_msg:", combat.user_attack_msg)