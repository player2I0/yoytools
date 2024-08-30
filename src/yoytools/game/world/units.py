class Unit:
    """
    Base class for describing a game unit
    """
    def __init__(self, hex = None, player = None):
        self.hex = hex
        self.player = player


class Capital(Unit):
    """
    The capital of a player (this annoying golden castle)
    """
    def __init__(self, hex = None, player = None):
        super().__init__(hex, player)


class Peasant(Unit):
    """
    A human
    """
    def __init__(self, hex = None, player = None):
        super().__init__(hex, player)


class Warrior(Peasant):
    """
    A human with a spear.
    """
    def __init__(self, hex = None, player = None):
        super().__init__(hex, player)


class Squire(Peasant):
    """
    A human in red armor
    """
    def __init__(self, hex = None, player = None):
        super().__init__(hex, player)


class Knight(Peasant):
    """
    A human in red armor, shield and sword
    """
    def __init__(self, hex = None, player = None):
        super().__init__(hex, player)


class Tower(Unit):
    """
    A tower.
    """
    def __init__(self, hex = None):
        super().__init__(hex, None)


class UpgradedTower(Tower):
    """
    An upgraded tower.
    """
    def __init__(self, hex = None):
        super().__init__(hex)