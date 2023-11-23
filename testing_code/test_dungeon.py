from dungeon import *
from player import *

def test_dungeon():
    player = Player('TestPlayer', 50, WEAPONS[SWORD])
    world = Dungeon(player, ROOMS)
    assert Dungeon.SCREEN_WIDTH == 80
    assert world.location == 'house_63'
    assert world.current_room == ROOMS[world.location]
    assert world.rooms == ROOMS
    assert world.player == player
    