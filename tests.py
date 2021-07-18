import unittest

from base import Level
from gates import And, Nand, Nor, Not, Or, Xor


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
        test_and = And("test_and_gate")
        test_and.input_a.val = Level.HI
        test_and.input_b.val = Level.HI
        self.assertEqual(test_and.output.val, Level.HI, "1 x 1 = 1")
        test_and.input_a.val = Level.LO
        self.assertEqual(test_and.output.val, Level.LO, "0 x 1 = 0")
        test_and.input_b.val = Level.LO
        self.assertEqual(test_and.output.val, Level.LO, "0 x 0 = 0")
        test_and.input_a.val = Level.HI
        self.assertEqual(test_and.output.val, Level.LO, "1 x 0 = 0")

    def test_or(self):
        test_or = Or("test_or_gate")
        test_or.input_a.val = Level.HI
        test_or.input_b.val = Level.HI
        self.assertEqual(test_or.output.val, Level.HI, "1 + 1 = 1")
        test_or.input_a.val = Level.LO
        self.assertEqual(test_or.output.val, Level.HI, "0 + 1 = 1")
        test_or.input_b.val = Level.LO
        self.assertEqual(test_or.output.val, Level.LO, "0 + 0 = 0")
        test_or.input_a.val = Level.HI
        self.assertEqual(test_or.output.val, Level.HI, "1 + 0 = 1")

    def test_nand(self):
        test_nand = Nand("test_nand_gate")
        test_nand.input_a.val = Level.HI
        test_nand.input_b.val = Level.HI
        self.assertEqual(test_nand.output.val, Level.LO, "!(1 x 1) = 0")
        test_nand.input_a.val = Level.LO
        self.assertEqual(test_nand.output.val, Level.HI, "!(0 x 1) = 1")
        test_nand.input_b.val = Level.LO
        self.assertEqual(test_nand.output.val, Level.HI, "!(0 x 0) = 1")
        test_nand.input_a.val = Level.HI
        self.assertEqual(test_nand.output.val, Level.HI, "!(1 x 0) = 1")

    def test_nor(self):
        test_nor = Nor("test_nor_gate")
        test_nor.input_a.val = Level.HI
        test_nor.input_b.val = Level.HI
        self.assertEqual(test_nor.output.val, Level.LO, "!(1 + 1) = 0")
        test_nor.input_a.val = Level.LO
        self.assertEqual(test_nor.output.val, Level.LO, "!(0 + 1) = 0")
        test_nor.input_b.val = Level.LO
        self.assertEqual(test_nor.output.val, Level.HI, "!(0 + 0) = 1")
        test_nor.input_a.val = Level.HI
        self.assertEqual(test_nor.output.val, Level.LO, "!(1 + 0) = 0")

    def test_xor(self):
        test_xor = Xor("test_xor_gate")
        test_xor.input_a.val = Level.HI
        test_xor.input_b.val = Level.HI
        self.assertEqual(test_xor.output.val, Level.LO, "(1 + 1) * (!1 + !1) = 0")
        test_xor.input_a.val = Level.LO
        self.assertEqual(test_xor.output.val, Level.HI, "(0 + 1) * (!0 + !1) = 1")
        test_xor.input_b.val = Level.LO
        self.assertEqual(test_xor.output.val, Level.LO, "(0 + 0) * (!0 + !0) = 0")
        test_xor.input_a.val = Level.HI
        self.assertEqual(test_xor.output.val, Level.HI, "(1 + 0) * (!1 + !0) = 1")


if __name__ == "__main__":
    unittest.main()
