from base import LogicComponent
from gates import And, Split, Xor


class HalfAdder(LogicComponent):
    """
    Adds two bits a and b and provides two outputs: sum and carry.

    | SUM  | 0    | 1    |
    | ---- | ---- | ---- |
    | 0    | 0    | 1    |
    | 1    | 1    | 0    |

    | CARRY  | 0    | 1    |
    | ------ | ---- | ---- |
    | 0      | 0    | 0    |
    | 1      | 0    | 1    |
    """

    def __init__(self, name):
        super().__init__(name)
        self.and_gate = And(f"{name}#and")
        self.xor_gate = Xor(f"{name}#xor")
        self.splitter_a = Split(f"{name}#splitter_a")
        self.splitter_b = Split(f"{name}#splitter_b")
        self.input_a = self.splitter_a.input
        self.input_b = self.splitter_b.input
        self.splitter_a.output_a.connections.append(self.and_gate.input_a)
        self.splitter_a.output_b.connections.append(self.xor_gate.input_a)
        self.splitter_b.output_a.connections.append(self.and_gate.input_b)
        self.splitter_b.output_b.connections.append(self.xor_gate.input_b)
        self.output_carry = self.and_gate.output
        self.output_sum = self.xor_gate.output
