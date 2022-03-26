import unittest

from adders import FullAdder, HalfAdder, EightBitAdder


class TestAdders(unittest.TestCase):
    def setUp(self):
        pass

    def test_half_adder(self):
        half_adder = HalfAdder("test_half_adder")
        half_adder.input_a.val = 1
        half_adder.input_b.val = 1
        self.assertEqual(half_adder.output_sum.val, 0, "1 + 1: sum bit is 0")
        self.assertEqual(half_adder.output_carry.val, 1, "1 + 1: carry bit is 1")
        half_adder.input_a.val = 0
        self.assertEqual(half_adder.output_sum.val, 1, "0 + 1: sum bit is 1")
        self.assertEqual(half_adder.output_carry.val, 0, "0 + 1: carry bit is 0")
        half_adder.input_b.val = 0
        self.assertEqual(half_adder.output_sum.val, 0, "0 + 0: sum bit is 0")
        self.assertEqual(half_adder.output_carry.val, 0, "0 + 0: carry bit is 0")

    def test_full_adder(self):
        full_adder = FullAdder("test_full_adder")
        full_adder.input_a.val = 1
        full_adder.input_b.val = 1
        full_adder.input_carry.val = 1
        self.assertEqual(full_adder.output_sum.val, 1, "adder(1, 1, 1) = (1, 1)")
        self.assertEqual(full_adder.output_carry.val, 1, "adder(1, 1, 1) = (1, 1)")
        full_adder.input_carry.val = 0
        self.assertEqual(full_adder.output_sum.val, 0, "adder(1, 1, 0) = (0, 1")
        self.assertEqual(full_adder.output_carry.val, 1, "adder(1, 1, 0) = (0, 1)")
        full_adder.input_b.val = 0
        self.assertEqual(full_adder.output_sum.val, 1, "adder(1, 0, 0) = (1, 0")
        self.assertEqual(full_adder.output_carry.val, 0, "adder(1, 0, 0) = (1, 0)")
        full_adder.input_a.val = 0
        self.assertEqual(full_adder.output_sum.val, 0, "adder(0, 0, 0) = (0, 0")
        self.assertEqual(full_adder.output_carry.val, 0, "adder(0, 0, 0) = (0, 0)")

    def test_eight_bit_adder(self):
        eight_bit_adder = EightBitAdder("test_eight_bit_adder")
        eight_bit_adder.input_a_0.val = 1
        eight_bit_adder.input_b_0.val = 1
        self.assertEqual(eight_bit_adder.output_s_0.val, 0, "1 + 1 = 2")
        self.assertEqual(eight_bit_adder.output_s_1.val, 1, "1 + 1 = 2")
        self.assertEqual(eight_bit_adder.output_s_2.val, 0, "1 + 1 = 2")
        eight_bit_adder.input_a_1.val = 1
        eight_bit_adder.input_a_2.val = 1
        eight_bit_adder.input_a_3.val = 1
        eight_bit_adder.input_a_4.val = 1
        eight_bit_adder.input_a_5.val = 1
        eight_bit_adder.input_b_1.val = 1
        eight_bit_adder.input_b_5.val = 1
        self.assertEqual(eight_bit_adder.output_s_0.val, 0, "63 + 35 = 98")
        self.assertEqual(eight_bit_adder.output_s_1.val, 1, "63 + 35 = 98")
        self.assertEqual(eight_bit_adder.output_s_2.val, 0, "63 + 35 = 98")
        self.assertEqual(eight_bit_adder.output_s_3.val, 0, "63 + 35 = 98")
        self.assertEqual(eight_bit_adder.output_s_4.val, 0, "63 + 35 = 98")
        self.assertEqual(eight_bit_adder.output_s_5.val, 1, "63 + 35 = 98")
        self.assertEqual(eight_bit_adder.output_s_6.val, 1, "63 + 35 = 98")
        self.assertEqual(eight_bit_adder.output_s_7.val, 0, "63 + 35 = 98")
