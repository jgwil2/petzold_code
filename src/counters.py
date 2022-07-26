from src.base import LogicComponent
from src.latches import OneBitEdgeTriggeredLatch
from src.mixins import EightBitInputOutputMixin


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


class EightBitRippleCounter(LogicComponent, EightBitInputOutputMixin):
    """
    An 8-bit ripple counter

    Ch. 14, pp. 173-178
    """

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.latch_0 = OneBitEdgeTriggeredLatch(f"{name}#latch_0")
        self.latch_1 = OneBitEdgeTriggeredLatch(f"{name}#latch_1")
        self.latch_2 = OneBitEdgeTriggeredLatch(f"{name}#latch_2")
        self.latch_3 = OneBitEdgeTriggeredLatch(f"{name}#latch_3")
        self.latch_4 = OneBitEdgeTriggeredLatch(f"{name}#latch_4")
        self.latch_5 = OneBitEdgeTriggeredLatch(f"{name}#latch_5")
        self.latch_6 = OneBitEdgeTriggeredLatch(f"{name}#latch_6")
        self.latch_7 = OneBitEdgeTriggeredLatch(f"{name}#latch_7")
        self.clock = self.latch_0.clock

        self.q_0 = self.latch_0.q
        self.latch_0.q_bar.connections.append(self.latch_0.data)
        self.latch_0.q_bar.connections.append(self.latch_1.clock)

        self.q_1 = self.latch_1.q
        self.latch_1.q_bar.connections.append(self.latch_1.data)
        self.latch_1.q_bar.connections.append(self.latch_2.clock)

        self.q_2 = self.latch_2.q
        self.latch_2.q_bar.connections.append(self.latch_2.data)
        self.latch_2.q_bar.connections.append(self.latch_3.clock)

        self.q_3 = self.latch_3.q
        self.latch_3.q_bar.connections.append(self.latch_3.data)
        self.latch_3.q_bar.connections.append(self.latch_4.clock)

        self.q_4 = self.latch_4.q
        self.latch_4.q_bar.connections.append(self.latch_4.data)
        self.latch_4.q_bar.connections.append(self.latch_5.clock)

        self.q_5 = self.latch_5.q
        self.latch_5.q_bar.connections.append(self.latch_5.data)
        self.latch_5.q_bar.connections.append(self.latch_6.clock)

        self.q_6 = self.latch_6.q
        self.latch_6.q_bar.connections.append(self.latch_6.data)
        self.latch_6.q_bar.connections.append(self.latch_7.clock)

        self.q_7 = self.latch_7.q
        self.latch_7.q_bar.connections.append(self.latch_7.data)
