from src.base import InputPin, OutputPin, LogicComponent


class Buffer(LogicComponent):
    """
    Sends input signal unaltered to an output

    Ch. 11, p. 128
    """

    def __init__(self, name):
        super().__init__(name)
        self.input = InputPin(self)
        self.output = OutputPin(self)

    def evaluate(self):
        self.output.val = self.input.val


class Not(LogicComponent):
    """
    Inverts input signal - output = !input

    Ch. 11, pp. 118-119
    """

    def __init__(self, name):
        super().__init__(name)
        self.input = InputPin(self)
        self.output = OutputPin(self)

    def evaluate(self):
        self.output.val = 0 if self.input.val == 1 else 1


class And(LogicComponent):
    """
    Outputs 1 if inputs a and b equal 1, otherwise outputs 0.

    | AND  | 0    | 1    |
    | ---- | ---- | ---- |
    | 0    | 0    | 0    |
    | 1    | 0    | 1    |

    Ch. 11, pp. 111-115
    """

    def __init__(self, name):
        super().__init__(name)
        self.input_a = InputPin(self)
        self.input_b = InputPin(self)
        self.output = OutputPin(self)

    def evaluate(self):
        self.output.val = (
            1 if self.input_a.val == 1 and self.input_b.val == 1 else 0
        )


class Or(LogicComponent):

    """
    Outputs 1 if input a equals 1 or input b equals 1, otherwise outputs
    0.

    | OR   | 0    | 1    |
    | ---- | ---- | ---- |
    | 0    | 0    | 1    |
    | 1    | 1    | 1    |

    Ch. 11, pp. 116-118
    """

    def __init__(self, name):
        super().__init__(name)
        self.input_a = InputPin(self)
        self.input_b = InputPin(self)
        self.output = OutputPin(self)

    def evaluate(self):
        self.output.val = (
            1 if self.input_a.val == 1 or self.input_b.val == 1 else 0
        )


class Nand(LogicComponent):
    """
    Negation of the And gate.

    | NAND | 0    | 1    |
    | ---- | ---- | ---- |
    | 0    | 1    | 1    |
    | 1    | 1    | 0    |

    Ch. 11, pp. 125-127
    """

    def __init__(self, name):
        super().__init__(name)
        self.and_gate = And(f"{name}#and")
        self.inverter = Not(f"{name}#not")
        self.and_gate.output.connections.append(self.inverter.input)
        self.input_a = self.and_gate.input_a
        self.input_b = self.and_gate.input_b
        self.output = self.inverter.output
        self.output.val = 1


class Nor(LogicComponent):
    """
    Negation of the Or gate.

    | NOR  | 0    | 1    |
    | ---- | ---- | ---- |
    | 0    | 1    | 0    |
    | 1    | 0    | 0    |

    Ch. 11, pp. 122-125
    """

    def __init__(self, name):
        super().__init__(name)
        self.or_gate = Or(f"{name}#or")
        self.inverter = Not(f"{name}#not")
        self.or_gate.output.connections.append(self.inverter.input)
        self.input_a = self.or_gate.input_a
        self.input_b = self.or_gate.input_b
        self.output = self.inverter.output
        self.output.val = 1


class Xor(LogicComponent):
    """
    Exclusive Or - outputs 1 if input a does not equal input b,
    otherwise outputs 0.

    | XOR  | 0    | 1    |
    | ---- | ---- | ---- |
    | 0    | 0    | 1    |
    | 1    | 1    | 0    |

    Ch. 12, pp. 135-136
    """

    def __init__(self, name):
        super().__init__(name)
        self.or_gate = Or(f"{name}#or")
        self.nand_gate = Nand(f"{name}#nand")
        self.and_gate = And(f"{name}#and")
        self.relay_a = Buffer(f"{name}#relay_a")
        self.relay_b = Buffer(f"{name}#relay_b")
        self.input_a = self.relay_a.input
        self.input_b = self.relay_b.input
        self.relay_a.output.connections.append(self.or_gate.input_a)
        self.relay_a.output.connections.append(self.nand_gate.input_a)
        self.relay_b.output.connections.append(self.or_gate.input_b)
        self.relay_b.output.connections.append(self.nand_gate.input_b)
        self.or_gate.output.connections.append(self.and_gate.input_b)
        self.nand_gate.output.connections.append(self.and_gate.input_a)
        self.nand_gate.output.val = 1
        self.output = self.and_gate.output
