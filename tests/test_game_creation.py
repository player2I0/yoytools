from yoytools.game import Game
from yoytools.game.world import RandomMap, view_map, Map, Hex, HexOwner
from yoytools.game.world import units

#game = Game([], RandomMap(100, 100))

hex = Hex(3, 1, unit=units.Peasant())

map = Map(10, 10, [
    Hex(0, 0), Hex(1, 0), Hex(2, 0), Hex(3, 0), Hex(4, 0), Hex(5, 0), Hex(6, 0),
    Hex(0, 1), Hex(1, 1), Hex(2, 1), hex,       Hex(4, 1), Hex(5, 1), Hex(6, 1),
    Hex(0, 2), Hex(1, 2), Hex(2, 2), Hex(3, 2), Hex(4, 2), Hex(5, 2), Hex(6, 2),
    Hex(0, 3), Hex(1, 3), Hex(2, 3), Hex(3, 3), Hex(4, 3), Hex(5, 3), Hex(6, 3)
])
n = hex.get_neighbours()
print(n)
#view_map(Map(10, 10, n.hexes))
view_map(map)