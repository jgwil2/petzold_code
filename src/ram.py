from typing import List
from base import LogicComponent


class SixtyFourKilobyteRamArray(LogicComponent):
    """
    A 64KBx8 RAM array. Memory is represented internally as a list of
    2^16 ints, such that each byte is represented as a decimal int
    (0-255). The `data_in`, `data_out`, and `address properties are
    lists of binary ints (0-1).

    Ch. 16, pp. 203-205
    """

    memory = [0] * (2**16)
    address = [0] * 16
    data_in = [0] * 8
    data_out = [0] * 8
    _write = 0

    def __init__(self, name: str) -> None:
        super().__init__(name)

    @property
    def write(self):
        return self._write

    @write.setter
    def write(self, write):
        self._write = write
        if self._write == 1:
            address_int = self._binary_list_to_int(self.address)
            self.memory[address_int] = self._binary_list_to_int(self.data_in)

    @staticmethod
    def _binary_list_to_int(vals: list[int]) -> int:
        bin_str = ""
        for i in vals:
            bin_str += str(i)
        bin_str = "0b" + bin_str
        return int(bin_str, 2)

    @staticmethod
    def _int_to_binary_list(val: int) -> list[int]:
        bin_list: List[int] = []
        val_str = format(val, "08b")
        for i in range(8):
            bin_list[7 - i] = int(val_str[i])
        return bin_list

    def evaluate(self):
        # TODO need to evaluate when address is updated
        address_int = self._binary_list_to_int(self.address)
        self.data_out = self._int_to_binary_list(self.memory[address_int])
