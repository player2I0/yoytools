from yoytools import perlin
import random
import curses
import time
import types

from yoytools.game.world import units
from yoytools.game.world.hex import Hex, HexOwner

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
                if hex.map is None:
                    hex.map = self
                self[(hex.x, hex.y)] = hex

    def move_unit(self, unit: units.MovableUnit, hex: Hex):
        unit.hex.unit = None
        hex.set_unit(unit)

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

        # hex colors:
        # 0 = red, 1 = yellow, 2 = blue, 3 = green, 4 = magenta, 5 = cyan, -1 = white (empty hex)

        curses.init_pair(9, curses.COLOR_WHITE, curses.COLOR_WHITE)
        #curses.init_pair(10, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(10, curses.COLOR_WHITE, curses.COLOR_RED)
        curses.init_pair(11, curses.COLOR_WHITE, curses.COLOR_YELLOW)
        curses.init_pair(12, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(13, curses.COLOR_WHITE, curses.COLOR_GREEN)
        curses.init_pair(14, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
        curses.init_pair(15, curses.COLOR_WHITE, curses.COLOR_CYAN)

        #unit_emojis = {types.NoneType: ['  ', 0], units.Peasant: ['🧍', 0], units.Squire: ['🧍', 1], units.Warrior: ['🧍', 2], units.Knight: ['🧍', 3], units.Tree: ['🌴', 0], units.Grave: ['💀', 0], units.Tower: ['♜ ', 0], units.UpgradedTower: ['♜ ', 4]}
        unit_emojis = {types.NoneType: ['  ', '  '], units.Peasant: ['🧍', '0_'], units.Squire: ['🧍', '1_'], units.Warrior: ['🧍', '2_'], units.Knight: ['🧍', '3_'], units.Tree: ['🌴', '__'], units.Grave: ['💀', '__'], units.Tower: ['♜ ', '0_'], units.UpgradedTower: ['♜ ', '1_']}

        for hex_coords in world.hexes:
            hex: Hex = world.hexes[hex_coords]

            if hex.x % 2 != 0:
                if (hex.x, hex.y) in world:
                    viewport.addstr(hex.y * 2 + 1, hex.x * 3, unit_emojis[type(hex.unit)][0], curses.color_pair(hex.owner.color + 10))
            else:
                if (hex.x, hex.y) in world:
                    viewport.addstr(hex.y * 2, hex.x * 3, unit_emojis[type(hex.unit)][0], curses.color_pair(hex.owner.color + 10))

        viewport.refresh( 0,0, 1,0, height - 1, width - 1)

        while True:
            height, width = stdscr.getmaxyx()
            v_height, v_width = viewport.getmaxyx()

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