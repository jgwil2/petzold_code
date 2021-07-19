from gates import And, Level, Nand, Not


def main():
    sample_inverter_a = Not("a")
    sample_inverter_b = Not("b")
    sample_inverter_a.output.connections.append(sample_inverter_b.input)
    sample_inverter_a.input.val = Level.HI
    print(f"inverter_a output = {sample_inverter_a.output.val}")
    print(f"inverter_b output = {sample_inverter_b.output.val}")
    sample_inverter_a.input.val = Level.LO
    print(f"inverter_a output = {sample_inverter_a.output.val}")
    print(f"inverter_b output = {sample_inverter_b.output.val}")

    sample_nand_gate = Nand("nand")
    sample_inverter_c = Not("c")
    sample_nand_gate.output.connections.append(sample_inverter_c.input)
    sample_nand_gate.input_a.val = Level.HI
    sample_nand_gate.input_b.val = Level.HI
    print(f"nand output = {sample_nand_gate.output.val}")
    print(f"inverter output = {sample_inverter_c.output.val}")
    sample_nand_gate.input_b.val = Level.LO
    print(f"nand output = {sample_nand_gate.output.val}")
    print(f"inverter output = {sample_inverter_c.output.val}")


if __name__ == "__main__":
    main()
