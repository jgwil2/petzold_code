from random import randrange
import unittest

from src.counters import EightBitRippleCounter
from src.clock import Clock


class TestClock(unittest.TestCase):
    def setUp(self):
        pass

    def test_clock(self):
        clock = Clock("test_clock", 100000)
        ripple_counter = EightBitRippleCounter("test_counter")
        clock.output.connections.append(ripple_counter.clock)
        test_cycles = randrange(1, 256)
        for i in range(test_cycles):
            clock.tick()
        self.assertEqual(
            ripple_counter.get_data_as_int("q"),
            test_cycles,
            "After random number of cycles, ripple counter value reflects number of clock ticks",
        )
