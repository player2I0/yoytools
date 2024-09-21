# 🧍 yoytools

## What is this?

This repo implements [yiotro's antiyoy](https://github.com/yiotro/Antiyoy) in python.

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

- [ ] Game
  - [ ] Adding players to the game
  - [ ] Starting the game
  - [ ] Turns (partially - implemented base functions for handling turns)

- [ ] World
  - [x] Map
  - [ ] Random map generation
  - [x] Hexagons
  - [ ] Units (partially - implemented basic classes, but not functionality)

- [ ] Emulator
  - [x] Basic map viewer
  - [ ] Gameplay