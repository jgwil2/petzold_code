from random import randrange
import unittest

from src.counters import EightBitRippleCounter, FrequencyDivider


class TestAdders(unittest.TestCase):
    def setUp(self):
        pass

    def test_frequency_divider(self):
        test_frequency_divider = FrequencyDivider("test")
        self.assertEqual(
            test_frequency_divider.clock.val, 0, "Clock starts at 0"
        )
        self.assertEqual(test_frequency_divider.q.val, 0, "Q starts at 0")
        test_frequency_divider.clock.setExternalPin(1)
        self.assertEqual(
            test_frequency_divider.q.val,
            1,
            "Q goes to 1 when clock makes positive transition",
        )
        test_frequency_divider.clock.setExternalPin(0)
        self.assertEqual(
            test_frequency_divider.q.val,
            1,
            "Q remains 1 when clock makes negative transition",
        )
        test_frequency_divider.clock.setExternalPin(1)
        self.assertEqual(
            test_frequency_divider.q.val,
            0,
            "Q goes to 0 when clock makes positive transition",
        )

    def test_eight_bit_ripple_counter(self):
        test_counter = EightBitRippleCounter("test")
        self.assertEqual(
            test_counter.get_data_as_int("q"), 0, "Output starts at 0"
        )
        test_counter.clock.setExternalPin(1)
        test_counter.clock.setExternalPin(0)
        self.assertEqual(
            test_counter.get_data_as_int("q"),
            1,
            "Output value is 1 after one clock cycle",
        )
        test_cycles = randrange(255)
        for i in range(test_cycles):
            test_counter.clock.setExternalPin(1)
            test_counter.clock.setExternalPin(0)
        self.assertEqual(
            test_counter.get_data_as_int("q"),
            1 + test_cycles,
            "After a random number of cycles, output value equals number of cycles elapsed",
        )
