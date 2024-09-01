import yoytools
import yoytools.game.world as world

class Game:
    """A class for describing a game. That's where everything happens."""

    def __init__(self, players: list, map: world.Map = world.RandomMap(10, 10)) -> None:
        """Initialize Game class

        Parameters
        ----------
        players : list
            List of Player class instances, representing game's players
        map : world.Map or world.RandomMap, default world.RandomMao
            Game map.
        """

        self.map = map
        self.players = players


class Player:
    def __init__(self, name = None, color: yoytools.Color = None):
        pass