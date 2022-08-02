import unittest

from src.ram import SixtyFourKilobyteRamArray


class TestRam(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_sixty_four_kilobye_ram_array_convenience_methods(self):
        ram = SixtyFourKilobyteRamArray("test_ram")
        self.assertEqual(ram._binary_list_to_int([0] * 8), 0)
        self.assertEqual(ram._binary_list_to_int([1] * 8), 255)
        self.assertEqual(ram._binary_list_to_int([0, 0, 1, 0, 0, 1, 1, 0]), 100)
        self.assertEqual(ram._binary_list_to_int([1] * 16), 65535)

        self.assertEqual(ram._int_to_binary_list(0), [0] * 8)
        self.assertEqual(ram._int_to_binary_list(255), [1] * 8)
        self.assertEqual(ram._int_to_binary_list(127), [1, 1, 1, 1, 1, 1, 1, 0])
        self.assertEqual(ram._int_to_binary_list(85), [1, 0, 1, 0, 1, 0, 1, 0])

    def test_sixty_four_kilobye_ram_array(self):
        ram = SixtyFourKilobyteRamArray("test_ram")
        self.assertEqual(ram.data_out, [0] * 8, "RAM output initialized as 0")
        ram.data_in = [1] * 8
        self.assertEqual(
            ram.data_out, [0] * 8, "No data has been written to RAM"
        )
        ram.write.val = 1
        ram.write.val = 0
        self.assertEqual(
            ram.data_out, [1] * 8, "Data has been written to RAM at address 0"
        )
        ram.address[0] = 1
        self.assertEqual(
            ram.data_out, [0] * 8, "RAM still has value 0 at address 1"
        )
        ram.data_in = ram._int_to_binary_list(219)
        ram.write.val = 1
        ram.write.val = 0
        self.assertEqual(
            ram.memory[1], 219, "Value 219 has been written to RAM at address 1"
        )
        ram.address[0] = 0
        self.assertEqual(
            ram.data_out, [1] * 8, "RAM still has value 1 at address 0"
        )
        ram.address = [1] * 16
        self.assertEqual(
            ram.data_out, [0] * 8, "RAM still has value 0 at address 65535"
        )
        ram.data_in = ram._int_to_binary_list(100)
        ram.write.val = 1
        ram.write.val = 0
        self.assertEqual(
            ram.memory[65535],
            100,
            "Value 100 has been written at address 65536",
        )
