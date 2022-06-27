import unittest

from ram import SixtyFourKilobyteRamArray


class TestSelectorsDecoders(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_sixty_four_kilobye_ram_array(self):
        self.ram = SixtyFourKilobyteRamArray("test_ram")
