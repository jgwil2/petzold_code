import unittest

from latches import EightBitLatch, OneBitLatch


class TestLatches(unittest.TestCase):
    def setUp(self):
        pass

    def test_one_bit_latch(self):
        test_latch = OneBitLatch("test_latch")
        test_latch.clock.val = 0
        test_latch.data.val = 0
        self.assertEqual(test_latch.q.val, 0, "Initial output = 0")
        self.assertEqual(test_latch.q_bar.val, 1, "Initial !output = 1")
        # store 1 in the latch
        test_latch.clock.val = 1
        test_latch.data.val = 1
        self.assertEqual(test_latch.q.val, 1, "Latch stores val 1")
        self.assertEqual(test_latch.q_bar.val, 0, "Latch stores val 1")
        # shift clock
        test_latch.clock.val = 0
        self.assertEqual(test_latch.q.val, 1, "Latch stores val 1")
        self.assertEqual(test_latch.q_bar.val, 0, "Latch stores val 1")
        test_latch.data.val = 0
        self.assertEqual(
            test_latch.q.val, 1, "When clock = 0, data does not affect output"
        )
        self.assertEqual(
            test_latch.q_bar.val,
            0,
            "When clock = 0, data does not affect output",
        )
        # store 0 in the latch
        test_latch.clock.val = 1
        self.assertEqual(
            test_latch.q.val, 0, "When clock = 1, data is overwritten"
        )
        self.assertEqual(
            test_latch.q_bar.val, 1, "When clock = 1, data is overwritten"
        )
        # shift clock
        test_latch.clock.val = 0
        test_latch.data.val = 1
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
                getattr(test_latch, f"q_{i}").val, 0, "Initializes to 0"
            )
        test_latch.clock.val = 1
        test_latch.d_0.val = 1
        test_latch.d_1.val = 1
        test_latch.d_4.val = 1
        test_latch.d_7.val = 1
        test_latch.clock.val = 0
        # clear inputs
        for i in range(8):
            getattr(test_latch, f"q_{i}").val = 0
        self.assertEqual(test_latch.d_0.val, 1)
        self.assertEqual(test_latch.d_0.val, 1)
        self.assertEqual(test_latch.d_4.val, 1)
        self.assertEqual(test_latch.d_7.val, 1)
