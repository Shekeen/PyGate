from ship import Ship
from math import trunc, fabs, floor, ceil


class Field:
    """Actual field"""
    def __init__(self, width, height, obstacles):
        self.width = width
        self.height = height
        self.field = [[0] * height] * width
        for o in obstacles:
            if o[0] < 0 or o[0] >= width or o[1] < 0 or o[1] >= height:
                continue
            self.field[o[0]][o[1]] = 1

    def get_at(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        return self.field[x][y]


class GateField:
    """Game field with logic"""
    def __init__(self, width, height, startpos, endpos, obstacles):
        self.width = width
        self.height = height
        self.field = Field(width, height, obstacles)
        self.ship = Ship(startpos)
        self.finish = endpos

    def _check_collision(self, coords):
        check_horiz = fabs(coords[0] - trunc(coords[0])) > 0.05
        check_vert = fabs(coords[1] - trunc(coords[1])) > 0.05
        if check_horiz:
            if check_vert:
                return self.field.get_at(floor(coords[0]), floor(coords[1])) or \
                       self.field.get_at(floor(coords[0]), ceil(coords[1])) or \
                       self.field.get_at(ceil(coords[0]), floor(coords[1])) or \
                       self.field.get_at(ceil(coords[0]), ceil(coords[1]))
            else:
                return self.field.get_at(floor(coords[0]), trunc(coords[1])) or \
                       self.field.get_at(ceil(coords[0]), trunc(coords[1]))
        else:
            if check_vert:
                return self.field.get_at(trunc(coords[0]), floor(coords[1])) or \
                       self.field.get_at(trunc(coords[0]), ceil(coords[1]))
            else:
                return self.field.get_at(trunc(coords[0]), trunc(coords[1]))

    def _sensors_state(self):
        circuit = {'s': False, 'w': False, 'n': False, 'e': False}
        current_cell = (trunc(self.ship.coords[0]), trunc(self.ship.coords[1]))
        circuit['s'] = self.field.get_at(current_cell[0], current_cell[1] + 1)
        circuit['w'] = self.field.get_at(current_cell[0] - 1, current_cell[1])
        circuit['n'] = self.field.get_at(current_cell[0], current_cell[1] - 1)
        circuit['e'] = self.field.get_at(current_cell[0] + 1, current_cell[1])
        return circuit

    def step(self):
        self.ship.move()
        if self._check_collision(self.ship.coords):
            self.ship.abort_move()

        self.ship.set_circuit(self._sensors_state())
        self.ship.process()
