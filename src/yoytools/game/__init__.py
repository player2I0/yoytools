import yoytools
import yoytools.game.world as world
from yoytools.game.world import units

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

        self.map = map #game map
        self.players: list = [] #game players
        self.started = False #is game started
        self.turning_player = None #player currently 'turning' (moving his units; e. g. 'playing')
        self.turns = -1

        for player in players:
            self.players.append(player)
            player.game = self

    def start(self):
        self.started = True

    def turn(self):
        if self.players.index(self.turning_player) >= len(self.players) - 1:
            self.turning_player = self.players[0]
        else:
            self.turning_player = self.players[self.players.index(self.turning_player) + 1]


class Player:
    """A class describing player, containing *isolated* code which is immune to undesirable modifying the game."""

    def __init__(self, name = 'player', color: int = 0):
        self.name = name
        self.color = color
        self.game: Game = None

    def can_turn(self):
        return (self.game.started and self.game.turning_player is self)
    
    def end_turn(self):
        if self.can_turn():
            self.game.turn()

    def move_unit(self, unit: units.MovableUnit, hex: world.Hex):
        if self.can_turn():
            if unit.movable and unit.can_move(hex) and unit.last_moved != self.game.turns:
                self.game.map.move_unit(unit, hex)
                unit.last_moved = self.game.turns