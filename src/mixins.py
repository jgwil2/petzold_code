class InputOutputMixin(object):
    # TODO configure size on init when inheriting
    def set_data_as_int(self, input: int, prefix: str, size: int = 8):
        # convert decimal to binary str and
        # iterate least-significant to most-significant
        highest_digit = size - 1
        input_str = format(input, "08b")
        for i in range(size):
            getattr(self, f"{prefix}_{highest_digit-i}").setExternalPin(
                1 if input_str[i] == "1" else 0
            )

    def get_data_as_int(self, prefix: str, size: int = 8) -> int:
        highest_digit = size - 1
        bin_str = ""
        for i in range(size):
            bin_str += (
                "1"
                if getattr(self, f"{prefix}_{highest_digit-i}").val == 1
                else "0"
            )
        # prepend binary prefix
        bin_str = "0b" + bin_str
        return int(bin_str, 2)
