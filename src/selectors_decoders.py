from src.base import LogicComponent
from src.gates import And, Buffer, Or, Not
from src.mixins import EightBitInputOutputMixin


class OneBitSelector(LogicComponent):
    """
    Output one of two different inputs, depending on the select input

    | Select | Input A | Input B | Output |
    |--------|---------|---------|--------|
    | 0      | 0       | X       | 0      |
    | 1      | X       | 0       | 0      |
    | 0      | 1       | X       | 1      |
    | 1      | X       | 1       | 1      |

    Ch. 24, p. 169
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.and_a = And(f"{name}#and_a")
        self.and_b = And(f"{name}#and_b")
        self.or_gate = Or(f"{name}#or_gate")
        self.inverter = Not(f"{name}#inverter")
        self.inverter.output.val = 1
        self.relay = Buffer(f"{name}#relay")
        self.select = self.relay.input
        self.input_a = self.and_a.input_a
        self.relay.output.connections.append(self.inverter.input)
        self.inverter.output.connections.append(self.and_a.input_b)
        self.input_b = self.and_b.input_a
        self.relay.output.connections.append(self.and_b.input_b)
        self.and_a.output.connections.append(self.or_gate.input_a)
        self.and_b.output.connections.append(self.or_gate.input_b)
        self.output = self.or_gate.output
        self.inverter.output.val = 1


class EightBitSelector(LogicComponent, EightBitInputOutputMixin):
    """
    A selector that takes two 8 bit numbers as input and displays one of
    them as output, depending on the select input

    Ch. 24, p. 169
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.selector_0 = OneBitSelector(f"{name}#selector_0")
        self.selector_1 = OneBitSelector(f"{name}#selector_1")
        self.selector_2 = OneBitSelector(f"{name}#selector_2")
        self.selector_3 = OneBitSelector(f"{name}#selector_3")
        self.selector_4 = OneBitSelector(f"{name}#selector_4")
        self.selector_5 = OneBitSelector(f"{name}#selector_5")
        self.selector_6 = OneBitSelector(f"{name}#selector_6")
        self.selector_7 = OneBitSelector(f"{name}#selector_7")
        self.relay = Buffer(f"{name}#relay")
        self.a_0 = self.selector_0.input_a
        self.a_1 = self.selector_1.input_a
        self.a_2 = self.selector_2.input_a
        self.a_3 = self.selector_3.input_a
        self.a_4 = self.selector_4.input_a
        self.a_5 = self.selector_5.input_a
        self.a_6 = self.selector_6.input_a
        self.a_7 = self.selector_7.input_a
        self.b_0 = self.selector_0.input_b
        self.b_1 = self.selector_1.input_b
        self.b_2 = self.selector_2.input_b
        self.b_3 = self.selector_3.input_b
        self.b_4 = self.selector_4.input_b
        self.b_5 = self.selector_5.input_b
        self.b_6 = self.selector_6.input_b
        self.b_7 = self.selector_7.input_b
        self.select = self.relay.input
        self.relay.output.connections.append(self.selector_0.select)
        self.relay.output.connections.append(self.selector_1.select)
        self.relay.output.connections.append(self.selector_2.select)
        self.relay.output.connections.append(self.selector_3.select)
        self.relay.output.connections.append(self.selector_4.select)
        self.relay.output.connections.append(self.selector_5.select)
        self.relay.output.connections.append(self.selector_6.select)
        self.relay.output.connections.append(self.selector_7.select)
        self.output_0 = self.selector_0.output
        self.output_1 = self.selector_1.output
        self.output_2 = self.selector_2.output
        self.output_3 = self.selector_3.output
        self.output_4 = self.selector_4.output
        self.output_5 = self.selector_5.output
        self.output_6 = self.selector_6.output
        self.output_7 = self.selector_7.output
