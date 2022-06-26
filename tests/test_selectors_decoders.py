import unittest

from src.selectors_decoders import EightBitSelector, OneBitSelector


class TestSelectorsDecoders(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_one_bit_selector(self):
        one_bit_selector = OneBitSelector("test_one_bit_selector")
        one_bit_selector.select.val = 0
        one_bit_selector.input_a.val = 0
        one_bit_selector.input_b.val = 0
        self.assertEqual(
            one_bit_selector.output.val,
            0,
            "select input is 0 so output value of A",
        )
        one_bit_selector.input_a.val = 1
        self.assertEqual(
            one_bit_selector.output.val,
            1,
            "select input is 0 so output value of A",
        )
        one_bit_selector.select.val = 1
        self.assertEqual(
            one_bit_selector.output.val,
            0,
            "select input is 1 so output value of B",
        )
        one_bit_selector.input_b.val = 1
        self.assertEqual(
            one_bit_selector.output.val,
            1,
            "select input is 1 so output value of B",
        )

    def test_eight_bit_selector(self):
        eight_bit_selector = EightBitSelector("test_eight_bit_selector")
        eight_bit_selector.set_data_as_int(32, "a")
        eight_bit_selector.set_data_as_int(101, "b")
        eight_bit_selector.select.val = 0
        self.assertEqual(
            eight_bit_selector.get_data_as_int("output"),
            32,
            "select input is 0 so output is value of A input",
        )
        eight_bit_selector.select.val = 1
        self.assertEqual(
            eight_bit_selector.get_data_as_int("output"),
            101,
            "select input is 1 so output is value of B input",
        )
