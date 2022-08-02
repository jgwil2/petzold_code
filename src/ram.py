from typing import List
from src.base import InputPin, LogicComponent, OutputPin


class RamWriteInputPin(InputPin):
    _val: int

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, val: int):
        if self._val != val:
            self._val = val
            self.component.updateWrite(val)


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

        self.write = RamWriteInputPin(self)

        self.addr_0 = InputPin(self)
        self.addr_1 = InputPin(self)
        self.addr_2 = InputPin(self)
        self.addr_3 = InputPin(self)
        self.addr_4 = InputPin(self)
        self.addr_5 = InputPin(self)
        self.addr_6 = InputPin(self)
        self.addr_7 = InputPin(self)
        self.addr_8 = InputPin(self)
        self.addr_9 = InputPin(self)
        self.addr_10 = InputPin(self)
        self.addr_11 = InputPin(self)
        self.addr_12 = InputPin(self)
        self.addr_13 = InputPin(self)
        self.addr_14 = InputPin(self)
        self.addr_15 = InputPin(self)

        self.di_0 = InputPin(self)
        self.di_1 = InputPin(self)
        self.di_2 = InputPin(self)
        self.di_3 = InputPin(self)
        self.di_4 = InputPin(self)
        self.di_5 = InputPin(self)
        self.di_6 = InputPin(self)
        self.di_7 = InputPin(self)

        self.do_0 = OutputPin(self)
        self.do_1 = OutputPin(self)
        self.do_2 = OutputPin(self)
        self.do_3 = OutputPin(self)
        self.do_4 = OutputPin(self)
        self.do_5 = OutputPin(self)
        self.do_6 = OutputPin(self)
        self.do_7 = OutputPin(self)

    @property
    def data_out(self):
        address_int = self._binary_list_to_int(self.address)
        self._data_out = self._int_to_binary_list(self.memory[address_int])
        return self._data_out

    @data_out.setter
    def data_out(self, data_out):
        self._data_out = data_out

    def updateWriteInputSignal(self, val):
        if val == 1:
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
