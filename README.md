# yoytools

## Basic usage

```python
from yoytools.game import Game
from yoytools.game.world import RandomMap, view_map

game = Game([], RandomMap(10, 10))

view_map(game.map)
```

This will create a game and you will enter the map viewer.