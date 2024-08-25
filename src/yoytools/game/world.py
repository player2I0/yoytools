from yoytools import perlin
import random

class Map:
    def __init__(self, width, height, data = None) -> None:
        self.hexes = {}

        self.width = width
        self.height = height

        if data is not None:
            self.load(data)

    def load(self, data):
        if type(data) is dict:
            for hex_cords in data:
                cords = tuple(map(int, hex_cords.split('.')))

                self[cords] = Hex(*cords, self, data[hex_cords])
        elif type(data) is list:
            for hex in data:
                self[(hex.x, hex.y)] = hex

    def __setitem__(self, key, value):
        self.hexes[key] = value

    def __getitem__(self, key):
        return self.hexes[key]
    
    def __contains__(self, item):
        if item in self.hexes:
            return True
        return False
    
    def __str__(self):
        s = ''

        '''
        for y in range(self.height):
            for char_ind in range(3):
                for x in range(self.width):
                    if (x, y) in self:
                        if char_ind == 0:
                            s += '  _ '
                        elif char_ind == 1:
                            s += ' / \\'
                        elif char_ind == 2:
                            s += ' \\_/'
                    else:
                        s += '   '
                s += '\n'
        '''

        for x in range(self.width):
            #print('iter')
            if x % 2 != 0 and (x, 0) in self:
                s += ' __ '
                #print('um')
            else:
                s += '    '
                #print('what')
        
        s += '\n'

        for x in range(self.width):
            #print('iter')
            if x % 2 != 0 and (x, 0) in self:
                s += f'/{str(x)}{str(0)}\\'
                #print('um')
            elif (x, 0) in self:
                s += ' __ '
                #print('what')
            else:
                s += '    '
        
        s += '\n'

        for y in range(self.height):
            for char in range(2):
                for x in range(self.width):
                    if (x, y) in self:
                        if x % 2 == 0:
                            if char == 0:
                                s += f'/{str(x)}{str(y)}\\'
                            elif char == 1:
                                s += '\\__/'
                        else:
                            if char == 0:
                                s += '\\__/'
                            elif char == 1:
                                if (x, y + 1) in self:
                                    s += f'/{str(x)}{str(y + 1)}\\'
                                else:
                                    s += '    '
                    else:
                        s += '    '
                s += '\n'

        return s


class RandomMap(Map):
    def __init__(self, width, height, seed=None) -> None:
        super().__init__(width, height, None)

        self.seed = random.randint(0, 100000)
        
        if seed is not None:
            self.seed = seed

        self.load(self.generate_hexes(width, height, self.seed))

    def generate_hexes(self, width, height, seed):
        threshold = 0.1

        hexes = []

        noise = perlin.PerlinNoiseFactory(2, tile=(0, 0))

        for x in range(width):
            for y in range(height):
                #print(noise(x/width, y/height))

                y_sub = 0

                #if x % 2 != 0:
                #    y_sub = (1/height) / 2

                if noise(x/width, y/height - y_sub) >= threshold:
                    hexes.append(Hex(x, y, self))

        return hexes
        

class Hex:
    """
    ⬡
    """

    def __init__(self, x, y, map, data=None, owner = None, unit = None):
        self.x = x
        self.y = y
        self.map = map

        self.owner = owner
        self.unit = unit

        if data is not None:
            self.load(data)

    def load(self, data):
        pass