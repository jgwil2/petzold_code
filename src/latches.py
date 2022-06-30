from src.base import LogicComponent
from src.gates import And, Nor, Not, Buffer
from src.mixins import EightBitInputOutputMixin


class FlipFlop(LogicComponent):
    """
    An RS flip-flop

    Ch. 14, pp. 159-162
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.nor_a = Nor(f"{name}#nor_a")
        self.nor_b = Nor(f"{name}#nor_b")
        self.r = self.nor_a.input_a
        self.s = self.nor_b.input_b
        self.nor_a.output.connections.append(self.nor_b.input_a)
        self.nor_b.output.connections.append(self.nor_a.input_b)
        self.q = self.nor_a.output
        self.q_bar = self.nor_b.output
        self.q_bar.val = 1


class OneBitLatch(LogicComponent):
    """
    A level-triggered D-type flip-flop

    Ch. 14, pp. 163-167
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.relay_clock = Buffer(f"{name}#relay_clock")
        self.relay_data = Buffer(f"{name}#relay_data")
        self.and_a = And(f"{name}#and_a")
        self.and_b = And(f"{name}#and_b")
        self.inverter = Not(f"{name}#inverter")
        self.nor_a = Nor(f"{name}#nor_a")
        self.nor_b = Nor(f"{name}#nor_b")
        self.clock = self.relay_clock.input
        self.data = self.relay_data.input
        self.relay_clock.output.connections.append(self.and_a.input_b)
        self.relay_clock.output.connections.append(self.and_b.input_a)
        self.relay_data.output.connections.append(self.inverter.input)
        self.inverter.output.connections.append(self.and_a.input_a)
        self.relay_data.output.connections.append(self.and_b.input_b)
        self.and_a.output.connections.append(self.nor_a.input_a)
        self.and_b.output.connections.append(self.nor_b.input_b)
        self.nor_a.output.connections.append(self.nor_b.input_a)
        self.nor_b.output.connections.append(self.nor_a.input_b)
        self.q = self.nor_a.output
        self.q_bar = self.nor_b.output
        self.q_bar.val = 1


class OneBitEdgeTriggeredLatch(LogicComponent):
    """
    An edge-triggered D-type flip-flop with preset and clear

    | Pre | Clr | D | Clk | Q | Q-bar |
    |-----|-----|---|-----|---|-------|
    | 0   | 1   | X | X   | 0 | 1     |
    | 1   | 0   | X | X   | 1 | 0     |
    | 0   | 0   | 0 | T   | 0 | 1     |
    | 0   | 0   | 1 | T   | 1 | 0     |
    | 0   | 0   | X | 0   | Q | Q-bar |

    Ch. 14, pp. 178-179
    """

    pass


class EightBitLatch(LogicComponent, EightBitInputOutputMixin):
    """
    A latch capable of storing a single 8-bit value
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.latch_0 = OneBitLatch(f"{name}#latch_0")
        self.latch_1 = OneBitLatch(f"{name}#latch_1")
        self.latch_2 = OneBitLatch(f"{name}#latch_2")
        self.latch_3 = OneBitLatch(f"{name}#latch_3")
        self.latch_4 = OneBitLatch(f"{name}#latch_4")
        self.latch_5 = OneBitLatch(f"{name}#latch_5")
        self.latch_6 = OneBitLatch(f"{name}#latch_6")
        self.latch_7 = OneBitLatch(f"{name}#latch_7")
        self.d_0 = self.latch_0.data
        self.d_1 = self.latch_1.data
        self.d_2 = self.latch_2.data
        self.d_3 = self.latch_3.data
        self.d_4 = self.latch_4.data
        self.d_5 = self.latch_5.data
        self.d_6 = self.latch_6.data
        self.d_7 = self.latch_7.data
        self.q_0 = self.latch_0.q
        self.q_1 = self.latch_1.q
        self.q_2 = self.latch_2.q
        self.q_3 = self.latch_3.q
        self.q_4 = self.latch_4.q
        self.q_5 = self.latch_5.q
        self.q_6 = self.latch_6.q
        self.q_7 = self.latch_7.q
        self.relay = Buffer(f"{name}#clock")
        self.clock = self.relay.input
        self.relay.output.connections.append(self.latch_0.clock)
        self.relay.output.connections.append(self.latch_1.clock)
        self.relay.output.connections.append(self.latch_2.clock)
        self.relay.output.connections.append(self.latch_3.clock)
        self.relay.output.connections.append(self.latch_4.clock)
        self.relay.output.connections.append(self.latch_5.clock)
        self.relay.output.connections.append(self.latch_6.clock)
        self.relay.output.connections.append(self.latch_7.clock)
