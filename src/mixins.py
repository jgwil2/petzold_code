class EightBitInputOutputMixin(object):
    def set_data_as_int(self, input: int, prefix: str):
        # convert decimal to binary str and
        # iterate least-significant to most-significant
        input_str = format(input, "08b")
        for i in range(8):
            getattr(self, f"{prefix}_{7-i}").setExternalPin(
                1 if input_str[i] == "1" else 0
            )

    def get_data_as_int(self, prefix: str) -> int:
        bin_str = ""
        for i in range(8):
            bin_str += "1" if getattr(self, f"{prefix}_{7-i}").val == 1 else "0"
        # prepend binary prefix
        bin_str = "0b" + bin_str
        return int(bin_str, 2)
