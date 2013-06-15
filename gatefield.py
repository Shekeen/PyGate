from ship import Ship
from math import trunc


class GateField:
    """Game field with logic"""
    def __init__(self, width, height, startpos, endpos, obstacles):
        self.width = width
        self.height = height
        self.field = Field(width, height, obstacles)
        self.ship = Ship(startpos)
        self.finish = endpos

    def _check_collision(self, coords):
        return False

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
