from typing import List
from src.base import LogicComponent


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
    _data_out = [0] * 8
    _write = 0

    def __init__(self, name: str) -> None:
        super().__init__(name)

    @property
    def data_out(self):
        address_int = self._binary_list_to_int(self.address)
        self._data_out = self._int_to_binary_list(self.memory[address_int])
        return self._data_out

    @data_out.setter
    def data_out(self, data_out):
        self._data_out = data_out

    @property
    def write(self):
        return self._write

    @write.setter
    def write(self, write):
        self._write = write
        if self._write == 1:
            address_int = self._binary_list_to_int(self.address)
            self.memory[address_int] = self._binary_list_to_int(self.data_in)

    def _binary_list_to_int(self, vals: list[int]) -> int:
        bin_str = ""
        for i in reversed(vals):
            bin_str += str(i)
        bin_str = "0b" + bin_str
        return int(bin_str, 2)

    def _int_to_binary_list(self, val: int) -> list[int]:
        if val > 255:
            raise ValueError("Integer value must be less than 255")
        bin_list: List[int] = []
        val_str = format(val, "08b")
        for i in range(8):
            bin_list.append(int(val_str[7 - i]))
        return bin_list
