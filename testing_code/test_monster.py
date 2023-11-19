from monster import Monster

#Initializing a monster. Checking to see if values were correctly set.
def test_initialize():
    monster = Monster("Bear", 4, 2, action="hit")
    assert monster.name == 'Bear'
    assert monster.hp == 4
    assert monster.dmg == 2
    assert monster.action == 'hit'
