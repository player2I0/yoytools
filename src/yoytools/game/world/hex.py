from yoytools.game.world import units

class Hex:
    """
    ⬡
    """

    def __init__(self, x, y, map = None, data=None, owner = None, unit = None):
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

    def get_neighbours(self):
        collection = HexCollection.from_existing_coordinates([
                                  (self.x, self.y - 1),
                (self.x - 1, self.y),               (self.x + 1, self.y),

            (self.x - 1, self.y + 1),               (self.x + 1, self.y + 1),
                                  (self.x, self.y + 1)
        ], self.map)

        return collection

    def load(self, data):
        pass


class HexOwner:
    def __init__(self, hex = None, color = -1, player = None):
        self.color = color
        self.hex = hex
        self.player = player


class HexCollection:
    def __init__(self):
        self.hexes = []

    def add(self, hex):
        self.hexes.append(hex)

    def __str__(self):
        s = ''

        for hex in self.hexes:
            s += f'({hex.x}, {hex.y}) '

        return s

    @staticmethod
    def from_existing_coordinates(l, map):
        collection = HexCollection()

        for coordinate in l:
            if coordinate in map:
                collection.add(map[coordinate])

        return collection