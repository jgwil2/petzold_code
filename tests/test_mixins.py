import unittest

from src.adders import EightBitAdder
from src.latches import EightBitLatch


class TestMixins(unittest.TestCase):
    def setUp(self):
        pass

    def test_adder_with_mixin(self):
        test_adder = EightBitAdder("test_adder")
        test_adder.set_data_as_int(1, "input_a")
        test_adder.set_data_as_int(1, "input_b")
        self.assertEqual(test_adder.get_data_as_int("output_s"), 2)
        test_adder.set_data_as_int(74, "input_b")
        self.assertEqual(test_adder.get_data_as_int("output_s"), 75)
        test_adder.set_data_as_int(39, "input_a")
        self.assertEqual(test_adder.get_data_as_int("output_s"), 113)

    def test_latch_with_mixin(self):
        test_latch = EightBitLatch("test_latch")
        test_latch.set_data_as_int(32, "d")
        self.assertEqual(test_latch.get_data_as_int("q"), 0)
        test_latch.clock.val = 1
        self.assertEqual(test_latch.get_data_as_int("q"), 32)
        test_latch.clock.val = 0
        test_latch.set_data_as_int(132, "d")
        self.assertEqual(test_latch.get_data_as_int("q"), 32)
        test_latch.clock.val = 1
        self.assertEqual(test_latch.get_data_as_int("q"), 132)
