from src.base import LogicComponent
from src.gates import And, Nor, Not, Buffer, Or
from src.mixins import EightBitInputOutputMixin


class ThreeInputNor(LogicComponent):
    """
    Three-input NOR gate used in edge-triggered latch

    Given inputs A, B, C, if A == 0 and B == 0 and C == 0 then
        output == 1
        else output == 0
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.or_gate = Or(f"{name}#or")
        self.nor_gate = Nor(f"{name}#nor")
        self.input_a = self.or_gate.input_a
        self.input_b = self.or_gate.input_b
        self.or_gate.output.val = 1
        self.input_c = self.nor_gate.input_a
        self.or_gate.output.connections.append(self.nor_gate.input_b)
        self.output = self.nor_gate.output


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

    Note: T signifies transition from 0 to 1

    Ch. 14, pp. 178-179
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.nor_a = ThreeInputNor(f"{name}#nor_a")
        self.nor_b = ThreeInputNor(f"{name}#nor_b")
        self.nor_c = ThreeInputNor(f"{name}#nor_c")
        self.nor_d = ThreeInputNor(f"{name}#nor_d")
        self.nor_e = ThreeInputNor(f"{name}#nor_e")
        self.nor_f = ThreeInputNor(f"{name}#nor_f")
        self.inverter = Not(f"{name}#inverter")
        self.clear_relay = Buffer(f"{name}#clear_relay")
        self.preset_relay = Buffer(f"{name}#preset_relay")
        self.clock_relay = Buffer(f"{name}#clock_relay")
        self.clear = self.clear_relay.input
        self.preset = self.preset_relay.input
        self.clock = self.inverter.input
        self.inverter.output.connections.append(self.clock_relay.input)
        self.clear_relay.output.connections.append(self.nor_a.input_a)
        self.clear_relay.output.connections.append(self.nor_e.input_a)
        self.preset_relay.output.connections.append(self.nor_b.input_b)
        self.preset_relay.output.connections.append(self.nor_d.input_b)
        self.preset_relay.output.connections.append(self.nor_f.input_b)
        self.clock_relay.output.connections.append(self.nor_b.input_c)
        self.clock_relay.output.connections.append(self.nor_c.input_b)
        self.data = self.nor_d.input_c
        self.nor_a.output.connections.append(self.nor_b.input_a)
        self.nor_b.output.connections.append(self.nor_a.input_c)
        self.nor_b.output.connections.append(self.nor_c.input_a)
        self.nor_b.output.connections.append(self.nor_e.input_b)
        self.nor_c.output.connections.append(self.nor_d.input_a)
        self.nor_c.output.connections.append(self.nor_f.input_c)
        self.nor_d.output.connections.append(self.nor_a.input_b)
        self.nor_d.output.connections.append(self.nor_c.input_c)
        self.nor_e.output.connections.append(self.nor_f.input_a)
        self.nor_f.output.connections.append(self.nor_e.input_c)
        self.q = self.nor_e.output
        self.q_bar = self.nor_f.output
        self.inverter.output.val = 1
        self.nor_d.output.val = 1
        self.nor_f.output.val = 1


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
