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


class RandomMap(Map):
    def __init__(self, width, height, seed=None) -> None:
        super().__init__(width, height, None)

        self.seed = random.randint(0, 100000)
        
        if seed is not None:
            self.seed = seed

        self.load(self.generate_hexes(width, height, self.seed))

    def generate_hexes(self, width, height, seed):
        threshold = 0.48

        hexes = []

        noise = perlin.PerlinNoiseFactory(2, tile=(25600, 256), unbias=True, octaves=6)

        for x in range(width):
            for y in range(height):
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

        viewport = curses.newpad(world.height * 4, world.width * 4 + 10)
        height, width = stdscr.getmaxyx()
        v_height, v_width = viewport.getmaxyx()

        viewport_offset = [0, 0] #y, x
        
        y_shift = -2

        stdscr.addstr('Map viewer. WASD to navigate, q to exit')

        for hex_coords in world.hexes:
            hex = world.hexes[hex_coords]

            if hex.x % 2 == 0:
                if (hex.x, hex.y - 1) not in world:
                    viewport.addstr(hex.y * 2 + 1, hex.x * 3 + 1, '__')
                    viewport.addstr(hex.y * 2 + 2, hex.x * 3, f'/  \\')
                    viewport.addstr(hex.y * 2 + 3, hex.x * 3, '\\__/')
                else:
                    viewport.addstr(hex.y * 2 + 2, hex.x * 3, f'/  \\')
                    viewport.addstr(hex.y * 2 + 3, hex.x * 3, '\\__/')
            else:
                if (hex.x, hex.y - 1) not in world:
                    viewport.addstr(hex.y * 2 + 0, hex.x * 3 + 1, '__')
                    viewport.addstr(hex.y * 2 + 1, hex.x * 3, f'/  \\')
                    viewport.addstr(hex.y * 3 + 2, hex.x * 3, '\\__/')
                else:
                    viewport.addstr(hex.y * 2 + 1, hex.x * 3, f'/  \\')
                    viewport.addstr(hex.y * 2 + 2, hex.x * 3, '\\__/')

        viewport.refresh( 0,0, 1,0, height - 1, width - 1)

        while True:
            key = stdscr.getch()
            
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

            viewport.refresh( viewport_offset[0],viewport_offset[1], 1,0, height - 1, width - 1)

    curses.wrapper(viewer)