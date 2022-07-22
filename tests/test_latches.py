import unittest

from src.latches import (
    EightBitLatch,
    OneBitEdgeTriggeredLatch,
    OneBitLatch,
    ThreeInputNor,
)


class TestLatches(unittest.TestCase):
    def setUp(self):
        pass

    def test_three_input_nor(self):
        test_nor_gate = ThreeInputNor("test_three_input_nor")
        self.assertEqual(
            test_nor_gate.input_a.val, 0, "Levels are correctly set on init"
        )
        self.assertEqual(
            test_nor_gate.input_b.val, 0, "Levels are correctly set on init"
        )
        self.assertEqual(
            test_nor_gate.input_c.val, 0, "Levels are correctly set on init"
        )
        self.assertEqual(
            test_nor_gate.output.val, 1, "Levels are correctly set on init"
        )
        test_nor_gate.input_a.setExternalPin(1)
        self.assertEqual(test_nor_gate.output.val, 0, "Nor(1, 0, 0) = 0")
        test_nor_gate.input_a.setExternalPin(0)
        self.assertEqual(test_nor_gate.output.val, 1, "Nor(0, 0, 0) = 1")
        test_nor_gate.input_b.setExternalPin(1)
        self.assertEqual(test_nor_gate.output.val, 0, "Nor(0, 1, 0) = 0")
        test_nor_gate.input_b.setExternalPin(0)
        test_nor_gate.input_c.setExternalPin(1)
        self.assertEqual(test_nor_gate.output.val, 0, "Nor(0, 0, 1) = 0")

    def test_one_bit_latch(self):
        test_latch = OneBitLatch("test_latch")
        self.assertEqual(test_latch.q.val, 0, "Initial output = 0")
        self.assertEqual(test_latch.q_bar.val, 1, "Initial !output = 1")
        # store 1 in the latch
        test_latch.data.setExternalPin(1)
        test_latch.clock.setExternalPin(1)
        self.assertEqual(test_latch.q.val, 1, "Latch stores val 1")
        self.assertEqual(test_latch.q_bar.val, 0, "Latch stores val 1")
        # shift clock
        test_latch.clock.setExternalPin(0)
        self.assertEqual(test_latch.q.val, 1, "Latch stores val 1")
        self.assertEqual(test_latch.q_bar.val, 0, "Latch stores val 1")
        test_latch.data.setExternalPin(0)
        self.assertEqual(
            test_latch.q.val, 1, "When clock = 0, data does not affect output"
        )
        self.assertEqual(
            test_latch.q_bar.val,
            0,
            "When clock = 0, data does not affect output",
        )
        # store 0 in the latch
        test_latch.clock.setExternalPin(1)
        self.assertEqual(
            test_latch.q.val, 0, "When clock = 1, data is overwritten"
        )
        self.assertEqual(
            test_latch.q_bar.val, 1, "When clock = 1, data is overwritten"
        )
        # shift clock
        test_latch.clock.setExternalPin(0)
        test_latch.data.setExternalPin(1)
        self.assertEqual(
            test_latch.q.val, 0, "When clock = 0, data does not affect output"
        )
        self.assertEqual(
            test_latch.q_bar.val,
            1,
            "When clock = 0, data does not affect output",
        )
        test_latch.clock.setExternalPin(1)
        test_latch.clock.setExternalPin(0)
        test_latch.data.setExternalPin(0)
        self.assertEqual(test_latch.q.val, 1)
        test_latch.clock.setExternalPin(1)
        self.assertEqual(test_latch.q.val, 0)

    def test_one_bit_edge_triggered_latch_transition(self):
        test_latch = OneBitEdgeTriggeredLatch("test_edge_triggered_latch")
        self.assertEqual(test_latch.q.val, 0, "Initial output = 0")
        self.assertEqual(test_latch.q_bar.val, 1, "Initial !output = 1")
        test_latch.data.setExternalPin(1)
        self.assertEqual(
            test_latch.q.val,
            0,
            "Data input does not affect output when clock = 0",
        )
        # store 1 in the latch
        test_latch.clock.setExternalPin(1)
        self.assertEqual(test_latch.q.val, 1, "Latch stores val 1")
        self.assertEqual(test_latch.q_bar.val, 0, "Latch stores val 1")
        test_latch.clock.setExternalPin(0)
        self.assertEqual(test_latch.q.val, 1, "Latch stores val 1")
        self.assertEqual(test_latch.q_bar.val, 0, "Latch stores val 1")
        test_latch.data.setExternalPin(0)
        self.assertEqual(
            test_latch.q.val, 1, "When clock = 0, data does not affect output"
        )
        self.assertEqual(
            test_latch.q_bar.val,
            0,
            "When clock = 0, data does not affect output",
        )
        # store 0 in the latch
        test_latch.clock.setExternalPin(1)
        self.assertEqual(
            test_latch.q.val,
            0,
            "When clock transitions to 1, data is overwritten",
        )
        self.assertEqual(
            test_latch.q_bar.val,
            1,
            "When clock transitions to 1, data is overwritten",
        )
        test_latch.data.setExternalPin(1)
        self.assertEqual(
            test_latch.clock.val,
            1,
            "When clock = 1, data does not affect output",
        )
        self.assertEqual(
            test_latch.q.val, 0, "When clock = 1, data does not affect output"
        )
        # shift clock
        test_latch.clock.setExternalPin(0)
        self.assertEqual(
            test_latch.clock.val,
            0,
            "When clock = 0, data does not affect output",
        )
        self.assertEqual(
            test_latch.q.val, 0, "When clock = 0, data does not affect output"
        )
        self.assertEqual(
            test_latch.q_bar.val,
            1,
            "When clock = 0, data does not affect output",
        )

    def test_eight_bit_latch(self):
        test_latch = EightBitLatch("test_latch")
        for i in range(8):
            self.assertEqual(
                getattr(test_latch, f"q_{i}").val, 0, f"Initializes q_{i} to 0"
            )
        test_latch.d_0.setExternalPin(1)
        test_latch.d_1.setExternalPin(1)
        test_latch.d_4.setExternalPin(1)
        test_latch.d_7.setExternalPin(1)
        test_latch.clock.setExternalPin(1)
        test_latch.clock.setExternalPin(0)
        # clear inputs
        for i in range(8):
            getattr(test_latch, f"d_{i}").setExternalPin(0)
        self.assertEqual(test_latch.q_0.val, 1)
        self.assertEqual(test_latch.q_1.val, 1)
        self.assertEqual(test_latch.q_2.val, 0)
        self.assertEqual(test_latch.q_3.val, 0)
        self.assertEqual(test_latch.q_4.val, 1)
        self.assertEqual(test_latch.q_5.val, 0)
        self.assertEqual(test_latch.q_6.val, 0)
        self.assertEqual(test_latch.q_7.val, 1)
        test_latch.clock.setExternalPin(1)
        for i in range(8):
            self.assertEqual(
                getattr(test_latch, f"q_{i}").val, 0, f"Store 0 in q_{i}"
            )
