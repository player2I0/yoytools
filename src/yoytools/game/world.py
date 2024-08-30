from yoytools import perlin
import random
import curses
import time

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
        '''

        #for line in range(self.height * 2 + 1):
        #    for x 

        return s


class RandomMap(Map):
    def __init__(self, width, height, seed=None) -> None:
        super().__init__(width, height, None)

        self.seed = random.randint(0, 100000)
        
        if seed is not None:
            self.seed = seed

        self.load(self.generate_hexes(width, height, self.seed))

    def generate_hexes(self, width, height, seed):
        threshold = -55

        hexes = []

        noise = perlin.PerlinNoiseFactory(2, tile=(0, 0), unbias=True, octaves=6)

        for x in range(width):
            for y in range(height):
                #print(noise(x/width, y/height))

                y_sub = 0

                if x % 2 != 0:
                    y_sub = (1/height) / 2

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


def view_map(world: Map):
    def viewer(stdscr: curses.window):
        stdscr.clear()
        stdscr.refresh()

        stdscr.nodelay(1)
        #stdscr.leaveok(1)

        viewport = curses.newpad(world.height * 4, world.width * 4 + 10)
        #print(world.height * 2 + 1, world.width * 4)
        #viewport.addstr(5, 5, 'n')
        height, width = stdscr.getmaxyx()
        v_height, v_width = viewport.getmaxyx()

        viewport_offset = [0, 0] #y, x
        
        y_shift = -2

        stdscr.addstr('Map viewer. WASD to navigate, q to exit')

        '''
        for hex_coords in world.hexes:
            #viewport.addstr(5, 5, 'n')
            hex = world.hexes[hex_coords]

            if hex.y % 2 == 0:
                y_shift += 0.5

            if hex.x % 2 == 0:
                #print(hex.y * 4 + 1, hex.x * 4)
                if (hex.y - 1, hex.x) not in world:
                    viewport.addstr(hex.y * 3 + 1, hex.x * 4, ' __ ')
                    viewport.addstr(hex.y * 3 + 2, hex.x * 4, f'/  \\')
                    viewport.addstr(hex.y * 3 + 3, hex.x * 4, '\\__/')
                else:
                    #viewport.addstr(hex.y * 3 + 1, hex.x * 4, ' __ ')
                    if hex.y <= 1:
                        viewport.addstr(hex.y * 3 + 1, hex.x * 4, f'/  \\')
                        viewport.addstr(hex.y * 3 + 2, hex.x * 4, '\\__/')
                    else:
                        viewport.addstr(hex.y * 2 + 2, hex.x * 4, f'/  \\')
                        viewport.addstr(hex.y * 2 + 3, hex.x * 4, '\\__/')
            else:
                if (hex.y - 1, hex.x) not in world:
                    viewport.addstr(hex.y * 3 + 0, hex.x * 4, ' __ ')
                    viewport.addstr(hex.y * 3 + 1, hex.x * 4, f'/  \\')
                    viewport.addstr(hex.y * 3 + 2, hex.x * 4, '\\__/')
                else:
                    if hex.y <= 1:
                        viewport.addstr(hex.y * 3 + 0, hex.x * 4, f'/  \\')
                        viewport.addstr(hex.y * 3 + 1, hex.x * 4, '\\__/')
                    else:
                        viewport.addstr(hex.y * 2 + 1, hex.x * 4, f'/  \\')
                        viewport.addstr(hex.y * 2 + 2, hex.x * 4, '\\__/')
        '''

        for hex_coords in world.hexes:
            #viewport.addstr(5, 5, 'n')
            hex = world.hexes[hex_coords]

            if hex.x % 2 == 0:
                if (hex.x, hex.y - 1) not in world:
                    viewport.addstr(hex.y * 2 + 1, hex.x * 3 + 1, '__')
                    viewport.addstr(hex.y * 2 + 2, hex.x * 3, f'/  \\')
                    viewport.addstr(hex.y * 2 + 3, hex.x * 3, '\\__/')
                else:
                    #viewport.addstr(hex.y * 3 + 0, hex.x * 3 + 1, '__')
                    viewport.addstr(hex.y * 2 + 2, hex.x * 3, f'/  \\')
                    viewport.addstr(hex.y * 2 + 3, hex.x * 3, '\\__/')

                '''
                if (hex.x, hex.y - 1) not in world:
                    if (hex.x - 1, hex.y) not in world:
                        viewport.addstr(hex.y * 3 + 1, hex.x * 3, ' __ ')
                        viewport.addstr(hex.y * 3 + 2, hex.x * 3, f'/  \\')
                        viewport.addstr(hex.y * 3 + 3, hex.x * 3, '\\__/')
                    else:
                        viewport.addstr(hex.y * 3 + 1, hex.x * 3 + 1, '__ ')
                        viewport.addstr(hex.y * 3 + 2, hex.x * 3 + 1, f'  \\')

                        if (hex.x - 1, hex.y + 1) not in world:
                            viewport.addstr(hex.y * 3 + 3, hex.x * 3 + 0, '\\__/')
                        else:
                            viewport.addstr(hex.y * 3 + 3, hex.x * 3 + 1, '__/')
                else:
                    if hex.y <= 1:
                        if (hex.x - 1, hex.y) not in world:
                            viewport.addstr(hex.y * 3 + 1, hex.x * 4, f'/  \\')
                            viewport.addstr(hex.y * 3 + 2, hex.x * 4, '\\__/')
                        else:
                            viewport.addstr(hex.y * 3 + 1, hex.x * 4 + 1, f'  \\')
                            viewport.addstr(hex.y * 3 + 2, hex.x * 4 + 1, '__/')
                    else:
                        if (hex.x - 1, hex.y) not in world:
                            viewport.addstr(hex.y * 2 + 2, hex.x * 4, f'/  \\')
                            viewport.addstr(hex.y * 2 + 3, hex.x * 4, '\\__/')
                        else:
                            viewport.addstr(hex.y * 2 + 2, hex.x * 4 + 1, f'  \\')
                            viewport.addstr(hex.y * 2 + 3, hex.x * 4 + 1, '__/')
                '''
            else:
                if (hex.x, hex.y - 1) not in world:
                    viewport.addstr(hex.y * 2 + 0, hex.x * 3 + 1, '__')
                    viewport.addstr(hex.y * 2 + 1, hex.x * 3, f'/  \\')
                    viewport.addstr(hex.y * 3 + 2, hex.x * 3, '\\__/')
                else:
                    #viewport.addstr(hex.y * 3 + 0, hex.x * 3 + 1, '__')
                    viewport.addstr(hex.y * 2 + 1, hex.x * 3, f'/  \\')
                    viewport.addstr(hex.y * 2 + 2, hex.x * 3, '\\__/')

        viewport.refresh( 0,0, 1,0, height - 1, width - 1)

        while True:
            key = stdscr.getch()
            
            #stdscr.addstr(0, 0, str(key))

            if key == 115 and viewport_offset[0] < v_height - 1:
                viewport_offset[0] += 1
            if key == 119 and viewport_offset[0] > 0:
                viewport_offset[0] -= 1
            if key == 100 and viewport_offset[1] < v_width - 1:
                viewport_offset[1] += 2
            if key == 97 and viewport_offset[1] > 0:
                viewport_offset[1] -= 2
            if key == 113:
                break

            #viewport_offset = [viewport_offset[0], ]

            viewport.refresh( viewport_offset[0],viewport_offset[1], 1,0, height - 1, width - 1)

    curses.wrapper(viewer)