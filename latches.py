from base import Level, LogicComponent
from gates import And, Nor, Not, Split


class FlipFlop(LogicComponent):
    """
    An RS flip-flop
    """

    def __init__(self, name):
        super().__init__(name)
        self.nor_a = Nor(f"{name}#nor_a")
        self.nor_b = Nor(f"{name}#nor_b")
        self.r = self.nor_a.input_a
        self.s = self.nor_b.input_b
        self.nor_a.output.connections.append(self.nor_b.input_a)
        self.nor_b.output.connections.append(self.nor_a.input_b)
        self.q = self.nor_a.output
        self.q_bar = self.nor_b.output
        self.q_bar.val = Level.HI


class OneBitLatch(LogicComponent):
    """
    A level-triggered D-type flip-flop
    """

    def __init__(self, name):
        super().__init__(name)
        self.splitter_clock = Split(f"{name}#splitter_clock")
        self.splitter_data = Split(f"{name}#splitter_data")
        self.and_a = And(f"{name}#and_a")
        self.and_b = And(f"{name}#and_b")
        self.inverter = Not(f"{name}#inverter")
        self.nor_a = Nor(f"{name}#nor_a")
        self.nor_b = Nor(f"{name}#nor_b")
        self.clock = self.splitter_clock.input
        self.data = self.splitter_data.input
        self.splitter_clock.output_a.connections.append(self.and_a.input_b)
        self.splitter_clock.output_b.connections.append(self.and_b.input_a)
        self.splitter_data.output_a.connections.append(self.inverter.input)
        self.inverter.output.connections.append(self.and_a.input_a)
        self.splitter_data.output_b.connections.append(self.and_b.input_b)
        self.and_a.output.connections.append(self.nor_a.input_a)
        self.and_b.output.connections.append(self.nor_b.input_b)
        self.nor_a.output.connections.append(self.nor_b.input_a)
        self.nor_b.output.connections.append(self.nor_a.input_b)
        self.q = self.nor_a.output
        self.q_bar = self.nor_b.output
        self.q_bar.val = Level.HI


class EightBitLatch(LogicComponent):
    pass
