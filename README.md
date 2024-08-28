# yoytools

## Purpose

This is an implementation of [yiotro's antiyoy](https://github.com/yiotro/Antiyoy), which focuses not on providing a *playable game*, but being a merely *implementation* of the game, containing its logic and all the building blocks to it.

## Basic usage

```python
from yoytools.game import Game
from yoytools.game.world import RandomMap, view_map

game = Game([], RandomMap(10, 10))

view_map(game.map)
```

This will create a game and launch the map viewer.

## Implementation status

The project is being worked on and is focused on recreating antiyoy's core.

- [x] Basic Game and Map objects, describing the world.
- [x] Map viewer (using curses)
- [ ] Adding players to the game
- [ ] Units
- [ ] Random map generation
- [ ] A way to play the game (*emulator*)
- [ ] Starting the game