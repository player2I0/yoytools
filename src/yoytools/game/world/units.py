from yoytools.game.world.hex import Hex

class Unit:
    """
    Base class for describing a game unit
    """
    def __init__(self, hex = None):
        self.hex: Hex = hex


class MovableUnit(Unit):
    """
    Base class for describing a movable game unit.
    """
    def __init__(self, hex = None):
        super().__init__(hex)

        self.movable = True
        self.last_moved = -1

    def can_move(self, hex: Hex):
        return True


class ImmovableUnit(Unit):
    """
    Base class for describing an immovable game unit.
    """
    def __init__(self, hex = None):
        super().__init__(hex)

        self.movable = False


class Tree(ImmovableUnit):
    """
    A tree.
    """
    def __init__(self, hex = None):
        super().__init__(hex)


class Grave(ImmovableUnit):
    """
    A grave that turns into a tree on the next turn.
    """
    def __init__(self, hex = None):
        super().__init__(hex)


class Capital(ImmovableUnit):
    """
    The capital of a player (this annoying golden castle)
    """
    def __init__(self, hex = None):
        super().__init__(hex)


class Peasant(MovableUnit):
    """
    A human
    """
    def __init__(self, hex = None):
        super().__init__(hex)

    def can_move(self, hex):
        if hex.owner == self.owner:
            return True


class Warrior(Peasant):
    """
    A human with a spear.
    """
    def __init__(self, hex = None):
        super().__init__(hex)


class Squire(Peasant):
    """
    A human in red armor
    """
    def __init__(self, hex = None):
        super().__init__(hex)


class Knight(Peasant):
    """
    A human in red armor, shield and sword
    """
    def __init__(self, hex = None):
        super().__init__(hex)


class Tower(ImmovableUnit):
    """
    A tower.
    """
    def __init__(self, hex = None):
        super().__init__(hex)


class UpgradedTower(Tower):
    """
    An upgraded tower.
    """
    def __init__(self, hex = None):
        super().__init__(hex)