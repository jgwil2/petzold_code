from base import Level, InputPin, OutputPin, LogicComponent


class Split(LogicComponent):
    """
    Sends input signal to two different outputs
    """

    def __init__(self, name):
        self.input = InputPin(self)
        self.output_a = OutputPin(self)
        self.output_b = OutputPin(self)
        super().__init__(name)

    def evaluate(self):
        self.output_a.val = self.output_b.val = self.input.val


class Not(LogicComponent):
    """
    Inverts input signal - output = !input
    """

    def __init__(self, name):
        self.input = InputPin(self)
        self.output = OutputPin(self)
        super().__init__(name)

    def evaluate(self):
        self.output.val = Level.LO if self.input.val == Level.HI else Level.HI


class And(LogicComponent):
    """
    | AND  | 0    | 1    |
    | ---- | ---- | ---- |
    | 0    | 0    | 0    |
    | 1    | 0    | 1    |
    """

    def __init__(self, name):
        self.input_a = InputPin(self)
        self.input_b = InputPin(self)
        self.output = OutputPin(self)
        super().__init__(name)

    def evaluate(self):
        self.output.val = (
            Level.HI
            if self.input_a.val == Level.HI and self.input_b.val == Level.HI
            else Level.LO
        )


class Or(LogicComponent):

    """
    | OR   | 0    | 1    |
    | ---- | ---- | ---- |
    | 0    | 0    | 1    |
    | 1    | 1    | 1    |
    """

    def __init__(self, name):
        self.input_a = InputPin(self)
        self.input_b = InputPin(self)
        self.output = OutputPin(self)
        super().__init__(name)

    def evaluate(self):
        self.output.val = (
            Level.HI
            if self.input_a.val == Level.HI or self.input_b.val == Level.HI
            else Level.LO
        )


class Nand(LogicComponent):
    """
    | NAND | 0    | 1    |
    | ---- | ---- | ---- |
    | 0    | 1    | 1    |
    | 1    | 1    | 0    |
    """

    def __init__(self, name):
        self.and_gate = And(f"{name}#and")
        self.inverter = Not(f"{name}#not")
        self.and_gate.output.connections.append(self.inverter.input)
        self.input_a = self.and_gate.input_a
        self.input_b = self.and_gate.input_b
        self.output = self.inverter.output


class Nor(LogicComponent):
    """
    | NOR  | 0    | 1    |
    | ---- | ---- | ---- |
    | 0    | 1    | 0    |
    | 1    | 0    | 0    |
    """

    def __init__(self, name):
        self.or_gate = Or(f"{name}#or")
        self.inverter = Not(f"{name}#not")
        self.or_gate.output.connections.append(self.inverter.input)
        self.input_a = self.or_gate.input_a
        self.input_b = self.or_gate.input_b
        self.output = self.inverter.output


class Xor(LogicComponent):
    """
    | XOR  | 0    | 1    |
    | ---- | ---- | ---- |
    | 0    | 0    | 1    |
    | 1    | 1    | 0    |
    """

    def __init__(self, name):
        self.or_gate = Or(f"{name}#or")
        self.nand_gate = Nand(f"{name}#nand")
        self.and_gate = And(f"{name}#and")
        self.splitter_a = Split(f"{name}#splitter_a")
        self.splitter_b = Split(f"{name}#splitter_b")
        self.input_a = self.splitter_a.input
        self.input_b = self.splitter_b.input
        self.splitter_a.output_a.connections.append(self.or_gate.input_a)
        self.splitter_a.output_a.connections.append(self.nand_gate.input_a)
        self.splitter_b.output_b.connections.append(self.or_gate.input_b)
        self.splitter_b.output_b.connections.append(self.nand_gate.input_b)
        self.or_gate.output.connections.append(self.and_gate.input_b)
        self.nand_gate.output.connections.append(self.and_gate.input_a)
        self.output = self.and_gate.output
