from base import LogicComponent
from gates import Nand, Not, Or, Split


class OneBitLatch(LogicComponent):
    """
    A level-triggered D-type flip-flop
    """

    def __init__(self, name):
        super().__init__(name)
        self.splitter_a = Split(f"{name}#splitter_a")
        self.splitter_b = Split(f"{name}#splitter_b")
        self.or_a = Or(f"{name}#or_a")
        self.or_b = Or(f"{name}#or_b")
        self.inverter = Not(f"{name}#inverter")
        self.nand_a = Nand(f"{name}#nand_a")
        self.nand_b = Nand(f"{name}#nand_b")
        self.clock = self.splitter_a.input
        self.data = self.splitter_b.input
        self.splitter_a.output_a.connections.append(self.or_a.input_b)
        self.splitter_a.output_b.connections.append(self.or_b.input_a)
        self.splitter_b.output_a.connections.append(self.inverter.input)
        self.inverter.output.connections.append(self.or_a.input_a)
        self.splitter_b.output_b.connections.append(self.or_b.input_b)
        self.or_a.output.connections.append(self.nand_a.input_a)
        self.or_b.output.connections.append(self.nand_b.input_b)
        self.nand_a.output.connections.append(self.nand_b.input_a)
        self.nand_b.output.connections.append(self.nand_a.input_b)
        self.q = self.nand_a.output
        self.q_bar = self.nand_b.output


class EightBitLatch(LogicComponent):
    pass
