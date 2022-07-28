from src.base import LogicComponent
from src.latches import OneBitEdgeTriggeredLatch
from src.mixins import InputOutputMixin


class FrequencyDivider(LogicComponent):
    """
    A frequency divider whose output oscillates between 0 and 1 at half
    the rate of its clock input

    Ch. 14, pp. 173-175
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.latch = OneBitEdgeTriggeredLatch(f"{name}#latch")
        self.clock = self.latch.clock
        self.latch.q_bar.connections.append(self.latch.data)
        self.latch.data.setExternalPin(1)
        self.q = self.latch.q
        self.q_bar = self.latch.q_bar


class EightBitRippleCounter(LogicComponent, InputOutputMixin):
    """
    An 8-bit ripple counter

    Ch. 14, pp. 173-178
    """

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.divider_0 = FrequencyDivider(f"{name}#divider_0")
        self.divider_1 = FrequencyDivider(f"{name}#divider_1")
        self.divider_2 = FrequencyDivider(f"{name}#divider_2")
        self.divider_3 = FrequencyDivider(f"{name}#divider_3")
        self.divider_4 = FrequencyDivider(f"{name}#divider_4")
        self.divider_5 = FrequencyDivider(f"{name}#divider_5")
        self.divider_6 = FrequencyDivider(f"{name}#divider_6")
        self.divider_7 = FrequencyDivider(f"{name}#divider_7")
        self.clock = self.divider_0.clock

        self.q_0 = self.divider_0.q
        self.divider_0.q_bar.connections.append(self.divider_1.clock)

        self.q_1 = self.divider_1.q
        self.divider_1.q_bar.connections.append(self.divider_2.clock)

        self.q_2 = self.divider_2.q
        self.divider_2.q_bar.connections.append(self.divider_3.clock)

        self.q_3 = self.divider_3.q
        self.divider_3.q_bar.connections.append(self.divider_4.clock)

        self.q_4 = self.divider_4.q
        self.divider_4.q_bar.connections.append(self.divider_5.clock)

        self.q_5 = self.divider_5.q
        self.divider_5.q_bar.connections.append(self.divider_6.clock)

        self.q_6 = self.divider_6.q
        self.divider_6.q_bar.connections.append(self.divider_7.clock)

        self.q_7 = self.divider_7.q


class SixteenBitRippleCounter(LogicComponent, InputOutputMixin):
    """
    A 16-bit ripple counter

    Ch. 17, p. 208 (not explicitly implemented)
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.counter_1 = EightBitRippleCounter(f"{name}#counter_1")
        self.counter_2 = EightBitRippleCounter(f"{name}#counter_2")
        self.clock = self.counter_1.clock
        self.counter_1.divider_7.q_bar.connections.append(self.counter_2.clock)
        self.q_0 = self.counter_1.q_0
        self.q_1 = self.counter_1.q_1
        self.q_2 = self.counter_1.q_2
        self.q_3 = self.counter_1.q_3
        self.q_4 = self.counter_1.q_4
        self.q_5 = self.counter_1.q_5
        self.q_6 = self.counter_1.q_6
        self.q_7 = self.counter_1.q_7
        self.q_8 = self.counter_2.q_0
        self.q_9 = self.counter_2.q_1
        self.q_10 = self.counter_2.q_2
        self.q_11 = self.counter_2.q_3
        self.q_12 = self.counter_2.q_4
        self.q_13 = self.counter_2.q_5
        self.q_14 = self.counter_2.q_6
        self.q_15 = self.counter_2.q_7
