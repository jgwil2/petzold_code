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
    pass
