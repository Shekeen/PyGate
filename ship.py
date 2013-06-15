__author__ = 'barzoque'


class Ship:
    """Programmable ship"""
    def __init__(self, x, y):
        self.coords = (x, y)
        self.scanners = {'s': False, 'w': False, 'n': False, 'e': False}
        self.engines = {'s': False, 'w': False, 'n': False, 'e': False}
        self.circuit = None

    def process(self):
        outputs = self.circuit.process(self.scanners)
        self.engines['s'], self.engines['w'], self.engines['n'], self.engines['e'] = outputs

    def _move_ship(self, speed):
        self.coords = (self.coords[0] + speed[0], self.coords[1] + speed[1])

    def move(self):
        speed = [self.engines['w'] - self.engines['e'], self.engines['n'] - self.engines['s']]
        if speed[0] > 0 and self.scanners['e']:
            speed[0] = 0
        elif speed[0] < 0 and self.scanners['w']:
            speed[0] = 0
        if speed[1] > 0 and self.scanners['s']:
            speed[1] = 0
        elif speed[1] < 0 and self.scanners['n']:
            speed[1] = 0
        self._move_ship(speed)

    def set_circuit(self, circuit):
        self.circuit = circuit
