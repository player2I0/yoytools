from yoytools.game import Game
from yoytools.game.world import RandomMap, view_map, Map, Hex
from yoytools.game.world import units

#game = Game([], RandomMap(100, 100))
game = Game([], Map(10, 10, [Hex(0, 0, None, unit=units.Squire()), Hex(1, 0, None, unit=units.UpgradedTower()), Hex(2, 0, None, unit=units.Warrior()), Hex(1, 1, None, unit=units.Peasant()), Hex(3, 0, None, unit=units.Grave())]))

print(len(game.map.hexes))
#print(game.map)
view_map(game.map)
#print(game.map.hexes)