class Unit:
    """
    Base class for describing a game unit
    """
    def __init__(self, hex = None):
        self.hex = hex


class Tree(Unit):
    """
    A tree.
    """
    def __init__(self, hex = None):
        super().__init__(hex)


class Grave(Unit):
    """
    A grave that turns into a tree on the next turn.
    """
    def __init__(self, hex = None):
        super().__init__(hex)


class Capital(Unit):
    """
    The capital of a player (this annoying golden castle)
    """
    def __init__(self, hex = None):
        super().__init__(hex)


class Peasant(Unit):
    """
    A human
    """
    def __init__(self, hex = None):
        super().__init__(hex)


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


class Tower(Unit):
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