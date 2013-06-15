class Ship:
    """Programmable ship"""
    def __init__(self, pos):
        self.prev_coords = None
        self.coords = pos
        self.scanners = {'s': False, 'w': False, 'n': False, 'e': False}
        self.engines = {'s': False, 'w': False, 'n': False, 'e': False}
        self.circuit = None

    def process(self):
        outputs = self.circuit.process(self.scanners)
        self.engines['s'], self.engines['w'], self.engines['n'], self.engines['e'] = outputs

    def _get_speed(self):
        return 0.1 * (self.engines['w'] - self.engines['e']), 0.1 * (self.engines['n'] - self.engines['s'])

    def move(self):
        speed = self._get_speed()
        self.prev_coords = self.coords
        self.coords = (self.coords[0] + speed[0], self.coords[1] + speed[1])

    def abort_move(self):
        self.coords = self.prev_coords

    def set_circuit(self, circuit):
        self.circuit = circuit
