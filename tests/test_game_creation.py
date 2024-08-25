from yoytools.game import Game
from yoytools.game.world import RandomMap

game = Game([], RandomMap(8, 5))

print(len(game.map.hexes))
print(game.map)