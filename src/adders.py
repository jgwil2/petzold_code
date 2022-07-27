from src.base import LogicComponent
from src.gates import And, Or, Buffer, Xor
from src.mixins import InputOutputMixin


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

    Ch. 12, pp. 131-137
    """

    def __init__(self, name):
        super().__init__(name)
        self.and_gate = And(f"{name}#and")
        self.xor_gate = Xor(f"{name}#xor")
        self.relay_a = Buffer(f"{name}#relay_a")
        self.relay_b = Buffer(f"{name}#relay_b")
        self.input_a = self.relay_a.input
        self.input_b = self.relay_b.input
        self.relay_a.output.connections.append(self.and_gate.input_a)
        self.relay_a.output.connections.append(self.xor_gate.input_a)
        self.relay_b.output.connections.append(self.and_gate.input_b)
        self.relay_b.output.connections.append(self.xor_gate.input_b)
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

    Ch. 12, pp. 137-138
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


class EightBitAdder(LogicComponent, InputOutputMixin):
    """
    Adds two 8-bit numbers.

    Ch. 12, pp. 139-142
    """

    def __init__(self, name):
        super().__init__(name)
        self.adder_0 = FullAdder(f"{name}#adder_0")
        self.adder_1 = FullAdder(f"{name}#adder_1")
        self.adder_2 = FullAdder(f"{name}#adder_2")
        self.adder_3 = FullAdder(f"{name}#adder_3")
        self.adder_4 = FullAdder(f"{name}#adder_4")
        self.adder_5 = FullAdder(f"{name}#adder_5")
        self.adder_6 = FullAdder(f"{name}#adder_6")
        self.adder_7 = FullAdder(f"{name}#adder_7")
        # carry in is wired to carry in of least significant adder
        self.input_carry = self.adder_0.input_carry
        # each carry out is wired to the carry in of the next
        # most significant adder
        self.adder_0.output_carry.connections.append(self.adder_1.input_carry)
        self.adder_1.output_carry.connections.append(self.adder_2.input_carry)
        self.adder_2.output_carry.connections.append(self.adder_3.input_carry)
        self.adder_3.output_carry.connections.append(self.adder_4.input_carry)
        self.adder_4.output_carry.connections.append(self.adder_5.input_carry)
        self.adder_5.output_carry.connections.append(self.adder_6.input_carry)
        self.adder_6.output_carry.connections.append(self.adder_7.input_carry)
        # carry out of most significant adder is carry out of full adder
        self.output_carry = self.adder_7.output_carry
        # inputs: two 8 bit numbers A and B
        # each bit is labelled a_0-a_7 or b_0-b_7
        self.input_a_0 = self.adder_0.input_a
        self.input_a_1 = self.adder_1.input_a
        self.input_a_2 = self.adder_2.input_a
        self.input_a_3 = self.adder_3.input_a
        self.input_a_4 = self.adder_4.input_a
        self.input_a_5 = self.adder_5.input_a
        self.input_a_6 = self.adder_6.input_a
        self.input_a_7 = self.adder_7.input_a
        self.input_b_0 = self.adder_0.input_b
        self.input_b_1 = self.adder_1.input_b
        self.input_b_2 = self.adder_2.input_b
        self.input_b_3 = self.adder_3.input_b
        self.input_b_4 = self.adder_4.input_b
        self.input_b_5 = self.adder_5.input_b
        self.input_b_6 = self.adder_6.input_b
        self.input_b_7 = self.adder_7.input_b
        # output S is the sum of A and B
        # each bit is labelled s_0-s_7
        self.output_s_0 = self.adder_0.output_sum
        self.output_s_1 = self.adder_1.output_sum
        self.output_s_2 = self.adder_2.output_sum
        self.output_s_3 = self.adder_3.output_sum
        self.output_s_4 = self.adder_4.output_sum
        self.output_s_5 = self.adder_5.output_sum
        self.output_s_6 = self.adder_6.output_sum
        self.output_s_7 = self.adder_7.output_sum
