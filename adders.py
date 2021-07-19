from base import LogicComponent
from gates import And, Or, Split, Xor


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


class FullAdder(LogicComponent):
    """
    Adds 3 bits - a, b, and a carry bit from a possible previous op
    on a less-significant column.

    | Input A | Input B | Carry In | Sum Out | Carry Out |
    | ------- | ------- | -------- | ------- | --------- |
    | 0       | 0       | 0        | 0       | 0         |
    | 0       | 0       | 1        | 1       | 0         |
    | 0       | 1       | 0        | 1       | 0         |
    | 0       | 1       | 1        | 0       | 1         |
    | 1       | 0       | 0        | 1       | 0         |
    | 1       | 0       | 1        | 0       | 1         |
    | 1       | 1       | 0        | 0       | 1         |
    | 1       | 1       | 1        | 1       | 1         |
    """

    def __init__(self, name):
        super().__init__(name)
        self.adder_1 = HalfAdder(f"{name}#adder_1")
        self.adder_2 = HalfAdder(f"{name}#adder_2")
        self.or_gate = Or(f"{name}#or_gate")
        self.input_a = self.adder_1.input_a
        self.input_b = self.adder_1.input_b
        self.input_carry = self.adder_2.input_a
        self.adder_1.output_sum.connections.append(self.adder_2.input_b)
        self.adder_1.output_carry.connections.append(self.or_gate.input_b)
        self.adder_2.output_carry.connections.append(self.or_gate.input_a)
        self.output_sum = self.adder_2.output_sum
        self.output_carry = self.or_gate.output
