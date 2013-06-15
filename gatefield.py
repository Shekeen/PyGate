from ship import Ship
import math


class GateField:
    """Game field"""
    def __init__(self, width, height, startpos, endpos, obstacles):
        self.width = width
        self.height = height
        self.field = [[0] * height] * width
        for o in obstacles:
            self.field[o[0]][o[1]] = 1
        self.ship = Ship(startpos)
        self.finish = endpos

    def _check_collision(self, coords):
        return False

    def _sensors_state(self):
        circuit = {'s': False, 'w': False, 'n': False, 'e': False}
        ship_speed = self.ship.get_speed()
        return circuit

    def step(self):
        self.ship.move()
        if self._check_collision(self.ship.coords):
            self.ship.abort_move()

        self.ship.set_circuit(self._sensors_state())
        self.ship.process()
