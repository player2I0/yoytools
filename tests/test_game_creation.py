from yoytools.game import Game
from yoytools.game.world import RandomMap, view_map

game = Game([], RandomMap(100, 10))

print(len(game.map.hexes))
#print(game.map)
view_map(game.map)
#print(game.map.hexes)