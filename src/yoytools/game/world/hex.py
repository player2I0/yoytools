class Hex:
    """
    ⬡
    """

    def __init__(self, x, y, map, data=None, owner = None, unit = None):
        self.x = x
        self.y = y
        self.map = map

        self.owner: Hex = owner

        if owner is None:
            self.owner = HexOwner(hex=self)
        else:
            owner.hex = self

        self.unit = unit

        if unit is not None:
            self.set_unit(unit)

        if data is not None:
            self.load(data)
    
    def set_unit(self, unit: units.Unit):
        self.unit = unit
        unit.hex = self

    def load(self, data):
        pass


class HexOwner:
    def __init__(self, hex = None, color = -1, player = None):
        self.color = color
        self.hex = hex
        self.player = player