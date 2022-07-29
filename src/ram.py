from typing import List
from src.base import InputPin, LogicComponent, OutputPin


class SixtyFourKilobyteRamArray(LogicComponent):
    """
    A 64KBx8 RAM array. Memory is represented internally as a list of
    2^16 ints, such that each byte is represented as a decimal int
    (0-255). The `data_in`, `data_out`, and `address properties are
    lists of binary ints (0-1).

    TODO inputs and outputs will have to connect to Pins or mimic the
    Pin interface in order to auto-update when connected to other
    LogicComponents

    Ch. 16, pp. 203-205
    """

    memory = [0] * (2**16)
    address = [0] * 16
    data_in = [0] * 8
    _data_out = [0] * 8
    _write = 0

    def __init__(self, name: str) -> None:
        super().__init__(name)

        self.write = InputPin(f"{name}#write")

        self.addr_0 = InputPin(f"{name}#addr_0")
        self.addr_1 = InputPin(f"{name}#addr_1")
        self.addr_2 = InputPin(f"{name}#addr_2")
        self.addr_3 = InputPin(f"{name}#addr_3")
        self.addr_4 = InputPin(f"{name}#addr_4")
        self.addr_5 = InputPin(f"{name}#addr_5")
        self.addr_6 = InputPin(f"{name}#addr_6")
        self.addr_7 = InputPin(f"{name}#addr_7")
        self.addr_8 = InputPin(f"{name}#addr_8")
        self.addr_9 = InputPin(f"{name}#addr_9")
        self.addr_10 = InputPin(f"{name}#addr_10")
        self.addr_11 = InputPin(f"{name}#addr_11")
        self.addr_12 = InputPin(f"{name}#addr_12")
        self.addr_13 = InputPin(f"{name}#addr_13")
        self.addr_14 = InputPin(f"{name}#addr_14")
        self.addr_15 = InputPin(f"{name}#addr_15")

        self.di_0 = InputPin(f"{name}#di_0")
        self.di_1 = InputPin(f"{name}#di_1")
        self.di_2 = InputPin(f"{name}#di_2")
        self.di_3 = InputPin(f"{name}#di_3")
        self.di_4 = InputPin(f"{name}#di_4")
        self.di_5 = InputPin(f"{name}#di_5")
        self.di_6 = InputPin(f"{name}#di_6")
        self.di_7 = InputPin(f"{name}#di_7")

        self.do_0 = OutputPin(f"{name}#do_0")
        self.do_1 = OutputPin(f"{name}#do_1")
        self.do_2 = OutputPin(f"{name}#do_2")
        self.do_3 = OutputPin(f"{name}#do_3")
        self.do_4 = OutputPin(f"{name}#do_4")
        self.do_5 = OutputPin(f"{name}#do_5")
        self.do_6 = OutputPin(f"{name}#do_6")
        self.do_7 = OutputPin(f"{name}#do_7")

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
