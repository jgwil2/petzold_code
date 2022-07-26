import unittest

from src.counters import FrequencyDivider


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
