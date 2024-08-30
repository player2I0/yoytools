class Unit:
    """
    Base class for describing a game unit
    """
    def __init__(self, hex = None, player = None):
        self.hex = hex
        self.player = player


class Capital(Unit):
    def __init__(self, hex = None, player = None):
        super.__init__(hex, player)