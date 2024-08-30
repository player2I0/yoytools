from yoytools.game import Game
from yoytools.game.world import RandomMap, view_map, Map, Hex

#game = Game([], RandomMap(100, 100))
game = Game([], Map(10, 10, [Hex(0, 0, None), Hex(1, 0, None), Hex(2, 0, None), Hex(1, 1, None)]))

print(len(game.map.hexes))
#print(game.map)
view_map(game.map)
#print(game.map.hexes)