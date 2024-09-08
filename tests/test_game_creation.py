from yoytools.game import Game
from yoytools.game.world import RandomMap, view_map, Map, Hex, HexOwner
from yoytools.game.world import units

#game = Game([], RandomMap(100, 100))
game = Game([], Map(10, 10, [Hex(0, 0, None, unit=units.Squire(), owner=HexOwner(color=1)), Hex(1, 0, None, unit=units.UpgradedTower(), owner=HexOwner(color=1)), Hex(2, 0, None, unit=units.Warrior(), owner=HexOwner(color=1)), Hex(1, 1, None, unit=units.Peasant(), owner=HexOwner(color=1)), Hex(3, 0, None, unit=units.Grave())]))

print(len(game.map.hexes))
#print(game.map)
view_map(game.map)
#print(game.map.hexes)