from gates import Not, Level, And


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

    sample_and_gate = And("and")
    sample_and_gate.input_a.val = Level.HI
    sample_and_gate.input_b.val = Level.HI
    print(f"and output = {sample_and_gate.output.val}")


if __name__ == "__main__":
    main()
