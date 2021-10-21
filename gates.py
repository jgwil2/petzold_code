from base import Level, InputPin, OutputPin, LogicComponent


class Relay(LogicComponent):
    """
    Sends input signal to two different outputs
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
    """

    def __init__(self, name):
        super().__init__(name)
        self.input = InputPin(self)
        self.output = OutputPin(self)

    def evaluate(self):
        self.output.val = Level.LO if self.input.val == Level.HI else Level.HI


class And(LogicComponent):
    """
    Outputs 1 if inputs a and b equal 1, otherwise outputs 0.

    | AND  | 0    | 1    |
    | ---- | ---- | ---- |
    | 0    | 0    | 0    |
    | 1    | 0    | 1    |
    """

    def __init__(self, name):
        super().__init__(name)
        self.input_a = InputPin(self)
        self.input_b = InputPin(self)
        self.output = OutputPin(self)

    def evaluate(self):
        self.output.val = (
            Level.HI
            if self.input_a.val == Level.HI and self.input_b.val == Level.HI
            else Level.LO
        )


class Or(LogicComponent):

    """
    Outputs 1 if input a equals 1 or input b equals 1, otherwise outputs
    0.

    | OR   | 0    | 1    |
    | ---- | ---- | ---- |
    | 0    | 0    | 1    |
    | 1    | 1    | 1    |
    """

    def __init__(self, name):
        super().__init__(name)
        self.input_a = InputPin(self)
        self.input_b = InputPin(self)
        self.output = OutputPin(self)

    def evaluate(self):
        self.output.val = (
            Level.HI
            if self.input_a.val == Level.HI or self.input_b.val == Level.HI
            else Level.LO
        )


class Nand(LogicComponent):
    """
    Negation of the And gate.

    | NAND | 0    | 1    |
    | ---- | ---- | ---- |
    | 0    | 1    | 1    |
    | 1    | 1    | 0    |
    """

    def __init__(self, name):
        super().__init__(name)
        self.and_gate = And(f"{name}#and")
        self.inverter = Not(f"{name}#not")
        self.and_gate.output.connections.append(self.inverter.input)
        self.input_a = self.and_gate.input_a
        self.input_b = self.and_gate.input_b
        self.output = self.inverter.output


class Nor(LogicComponent):
    """
    Negation of the Or gate.

    | NOR  | 0    | 1    |
    | ---- | ---- | ---- |
    | 0    | 1    | 0    |
    | 1    | 0    | 0    |
    """

    def __init__(self, name):
        super().__init__(name)
        self.or_gate = Or(f"{name}#or")
        self.inverter = Not(f"{name}#not")
        self.or_gate.output.connections.append(self.inverter.input)
        self.input_a = self.or_gate.input_a
        self.input_b = self.or_gate.input_b
        self.output = self.inverter.output


class Xor(LogicComponent):
    """
    Exclusive Or - outputs 1 if input a does not equal input b,
    otherwise outputs 0.

    | XOR  | 0    | 1    |
    | ---- | ---- | ---- |
    | 0    | 0    | 1    |
    | 1    | 1    | 0    |
    """

    def __init__(self, name):
        super().__init__(name)
        self.or_gate = Or(f"{name}#or")
        self.nand_gate = Nand(f"{name}#nand")
        self.and_gate = And(f"{name}#and")
        self.relay_a = Relay(f"{name}#relay_a")
        self.relay_b = Relay(f"{name}#relay_b")
        self.input_a = self.relay_a.input
        self.input_b = self.relay_b.input
        self.relay_a.output.connections.append(self.or_gate.input_a)
        self.relay_a.output.connections.append(self.nand_gate.input_a)
        self.relay_b.output.connections.append(self.or_gate.input_b)
        self.relay_b.output.connections.append(self.nand_gate.input_b)
        self.or_gate.output.connections.append(self.and_gate.input_b)
        self.nand_gate.output.connections.append(self.and_gate.input_a)
        self.nand_gate.output.val = Level.HI
        self.output = self.and_gate.output
