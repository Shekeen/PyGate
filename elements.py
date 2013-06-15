__author__ = 'barzoque'


class Element:
    """Base class for all circuit elements"""
    def __init__(self):
        self.numInputs = None
        self.numOutputs = None

    def process(self, inputs):
        if len(inputs) != self.numInputs:
            raise ElementInputException


class AndElement(Element):
    """AND element"""
    def __init__(self):
        super().__init__()
        self.numInputs = 2
        self.numOutputs = 1

    def process(self, inputs):
        super().process(inputs)
        return inputs[0] and inputs[1]


class OrElement(Element):
    """OR element"""
    def __init__(self):
        super().__init__()
        self.numInputs = 2
        self.numOutputs = 1

    def process(self, inputs):
        super().process(inputs)
        return inputs[0] or inputs[1]


class NotElement(Element):
    """NOT element"""
    def __init__(self):
        super().__init__()
        self.numInputs = 1
        self.numOutputs = 1

    def process(self, inputs):
        super().process(inputs)
        return not inputs[0]


class XorElement(Element):
    """XOR element"""
    def __init__(self):
        super().__init__()
        self.numInputs = 2
        self.numOutputs = 1

    def process(self, inputs):
        super().process(inputs)
        return inputs[0] ^ inputs[1]


class SplitElement(Element):
    """Splitter element"""
    def __init__(self):
        super().__init__()
        self.numInputs = 1
        self.numOutputs = 2

    def process(self, inputs):
        super().process(inputs)
        return [inputs[0], inputs[0]]


class SwitchElement(Element):
    """Switch element"""
    def __init__(self):
        super().__init__()
        self.numInputs = 2
        self.numOutputs = 2
        self.current = 0

    def process(self, inputs):
        super().process(inputs)
        if inputs[0]:
            if inputs[1]:
                return [True, False] if self.current == 0 else [False, True]
            else:
                self.current = 0
                return [True, False]
        else:
            if inputs[1]:
                self.current = 1
                return [False, True]
            else:
                return [True, False] if self.current == 1 else [False, True]


class ElementInputException:
    """Exception for elements"""
    pass

