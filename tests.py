import unittest

from base import Level
from gates import And, Nand, Nor, Not, Or, Xor
from adders import FullAdder, HalfAdder, EightBitAdder


class TestLogicGates(unittest.TestCase):
    def setUp(self):
        pass

    def test_not(self):
        test_inverter = Not("test_inverter")
        test_inverter.input.val = Level.HI
        self.assertEqual(test_inverter.output.val, Level.LO, "!1 = 0")
        test_inverter.input.val = Level.LO
        self.assertEqual(test_inverter.output.val, Level.HI, "!0 = 1")

    def test_and(self):
        test_and_gate = And("test_and_gate")
        test_and_gate.input_a.val = Level.HI
        test_and_gate.input_b.val = Level.HI
        self.assertEqual(test_and_gate.output.val, Level.HI, "1 x 1 = 1")
        test_and_gate.input_a.val = Level.LO
        self.assertEqual(test_and_gate.output.val, Level.LO, "0 x 1 = 0")
        test_and_gate.input_b.val = Level.LO
        self.assertEqual(test_and_gate.output.val, Level.LO, "0 x 0 = 0")
        test_and_gate.input_a.val = Level.HI
        self.assertEqual(test_and_gate.output.val, Level.LO, "1 x 0 = 0")

    def test_or(self):
        test_or_gate = Or("test_or_gate")
        test_or_gate.input_a.val = Level.HI
        test_or_gate.input_b.val = Level.HI
        self.assertEqual(test_or_gate.output.val, Level.HI, "1 + 1 = 1")
        test_or_gate.input_a.val = Level.LO
        self.assertEqual(test_or_gate.output.val, Level.HI, "0 + 1 = 1")
        test_or_gate.input_b.val = Level.LO
        self.assertEqual(test_or_gate.output.val, Level.LO, "0 + 0 = 0")
        test_or_gate.input_a.val = Level.HI
        self.assertEqual(test_or_gate.output.val, Level.HI, "1 + 0 = 1")

    def test_nand(self):
        test_nand_gate = Nand("test_nand_gate")
        test_nand_gate.input_a.val = Level.HI
        test_nand_gate.input_b.val = Level.HI
        self.assertEqual(test_nand_gate.output.val, Level.LO, "!(1 x 1) = 0")
        test_nand_gate.input_a.val = Level.LO
        self.assertEqual(test_nand_gate.output.val, Level.HI, "!(0 x 1) = 1")
        test_nand_gate.input_b.val = Level.LO
        self.assertEqual(test_nand_gate.output.val, Level.HI, "!(0 x 0) = 1")
        test_nand_gate.input_a.val = Level.HI
        self.assertEqual(test_nand_gate.output.val, Level.HI, "!(1 x 0) = 1")

    def test_nor(self):
        test_nor_gate = Nor("test_nor_gate")
        test_nor_gate.input_a.val = Level.HI
        test_nor_gate.input_b.val = Level.HI
        self.assertEqual(test_nor_gate.output.val, Level.LO, "!(1 + 1) = 0")
        test_nor_gate.input_a.val = Level.LO
        self.assertEqual(test_nor_gate.output.val, Level.LO, "!(0 + 1) = 0")
        test_nor_gate.input_b.val = Level.LO
        self.assertEqual(test_nor_gate.output.val, Level.HI, "!(0 + 0) = 1")
        test_nor_gate.input_a.val = Level.HI
        self.assertEqual(test_nor_gate.output.val, Level.LO, "!(1 + 0) = 0")

    def test_xor(self):
        test_xor_gate = Xor("test_xor_gate")
        test_xor_gate.input_a.val = Level.HI
        test_xor_gate.input_b.val = Level.HI
        self.assertEqual(test_xor_gate.output.val, Level.LO, "(1 + 1) * (!1 + !1) = 0")
        test_xor_gate.input_a.val = Level.LO
        self.assertEqual(test_xor_gate.output.val, Level.HI, "(0 + 1) * (!0 + !1) = 1")
        test_xor_gate.input_b.val = Level.LO
        self.assertEqual(test_xor_gate.output.val, Level.LO, "(0 + 0) * (!0 + !0) = 0")
        test_xor_gate.input_a.val = Level.HI
        self.assertEqual(test_xor_gate.output.val, Level.HI, "(1 + 0) * (!1 + !0) = 1")


class TestAdders(unittest.TestCase):
    def setUp(self):
        pass

    def test_half_adder(self):
        half_adder = HalfAdder("test_half_adder")
        half_adder.input_a.val = Level.HI
        half_adder.input_b.val = Level.HI
        self.assertEqual(half_adder.output_sum.val, Level.LO, "1 + 1: sum bit is 0")
        self.assertEqual(half_adder.output_carry.val, Level.HI, "1 + 1: carry bit is 1")
        half_adder.input_a.val = Level.LO
        self.assertEqual(half_adder.output_sum.val, Level.HI, "0 + 1: sum bit is 1")
        self.assertEqual(half_adder.output_carry.val, Level.LO, "0 + 1: carry bit is 0")
        half_adder.input_b.val = Level.LO
        self.assertEqual(half_adder.output_sum.val, Level.LO, "0 + 0: sum bit is 0")
        self.assertEqual(half_adder.output_carry.val, Level.LO, "0 + 0: carry bit is 0")

    def test_full_adder(self):
        full_adder = FullAdder("test_full_adder")
        full_adder.input_a.val = Level.HI
        full_adder.input_b.val = Level.HI
        full_adder.input_carry.val = Level.HI
        self.assertEqual(full_adder.output_sum.val, Level.HI, "adder(1, 1, 1) = (1, 1)")
        self.assertEqual(
            full_adder.output_carry.val, Level.HI, "adder(1, 1, 1) = (1, 1)"
        )
        full_adder.input_carry.val = Level.LO
        self.assertEqual(full_adder.output_sum.val, Level.LO, "adder(1, 1, 0) = (0, 1")
        self.assertEqual(
            full_adder.output_carry.val, Level.HI, "adder(1, 1, 0) = (0, 1)"
        )
        full_adder.input_b.val = Level.LO
        self.assertEqual(full_adder.output_sum.val, Level.HI, "adder(1, 0, 0) = (1, 0")
        self.assertEqual(
            full_adder.output_carry.val, Level.LO, "adder(1, 0, 0) = (1, 0)"
        )
        full_adder.input_a.val = Level.LO
        self.assertEqual(full_adder.output_sum.val, Level.LO, "adder(0, 0, 0) = (0, 0")
        self.assertEqual(
            full_adder.output_carry.val, Level.LO, "adder(0, 0, 0) = (0, 0)"
        )

    def test_eight_bit_adder(self):
        eight_bit_adder = EightBitAdder("test_eight_bit_adder")
        eight_bit_adder.input_a_0.val = Level.HI
        eight_bit_adder.input_b_0.val = Level.HI
        self.assertEqual(eight_bit_adder.output_s_0.val, Level.LO, "1 + 1 = 2")
        self.assertEqual(eight_bit_adder.output_s_1.val, Level.HI, "1 + 1 = 2")
        self.assertEqual(eight_bit_adder.output_s_2.val, Level.LO, "1 + 1 = 2")
        eight_bit_adder.input_a_1.val = Level.HI
        eight_bit_adder.input_a_2.val = Level.HI
        eight_bit_adder.input_a_3.val = Level.HI
        eight_bit_adder.input_a_4.val = Level.HI
        eight_bit_adder.input_a_5.val = Level.HI
        eight_bit_adder.input_b_1.val = Level.HI
        eight_bit_adder.input_b_5.val = Level.HI
        self.assertEqual(eight_bit_adder.output_s_0.val, Level.LO, "63 + 35 = 98")
        self.assertEqual(eight_bit_adder.output_s_1.val, Level.HI, "63 + 35 = 98")
        self.assertEqual(eight_bit_adder.output_s_2.val, Level.LO, "63 + 35 = 98")
        self.assertEqual(eight_bit_adder.output_s_3.val, Level.LO, "63 + 35 = 98")
        self.assertEqual(eight_bit_adder.output_s_4.val, Level.LO, "63 + 35 = 98")
        self.assertEqual(eight_bit_adder.output_s_5.val, Level.HI, "63 + 35 = 98")
        self.assertEqual(eight_bit_adder.output_s_6.val, Level.HI, "63 + 35 = 98")
        self.assertEqual(eight_bit_adder.output_s_7.val, Level.LO, "63 + 35 = 98")


if __name__ == "__main__":
    unittest.main()
