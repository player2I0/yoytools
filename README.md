# yoytools

## Purpose

This is an implementation of [yiotro's antiyoy](https://github.com/yiotro/Antiyoy), which focuses not on providing a *playable game*, but being a merely *implementation* of the game, containing its logic and all the building blocks for creating a GUI for the game.

## Basic usage

```python
from yoytools.game import Game
from yoytools.game.world import RandomMap, view_map

game = Game([], RandomMap(10, 10))

view_map(game.map)
```

This will create a game and launch the map viewer.