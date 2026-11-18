GATE_TYPES = ("AND", "OR", "NAND", "NOR")

def evaluate_gate(gate_type: str, input_a: int, input_b: int) -> int:
    if input_a not in (0, 1) or input_b not in (0, 1):
        raise ValueError("Gate inputs must be 0 or 1.")

    gate_type = gate_type.upper()

    if gate_type == "AND":
        return input_a & input_b
    if gate_type == "OR":
        return input_a | input_b
    if gate_type == "NAND":
        return 1 - (input_a & input_b)
    if gate_type == "NOR":
        return 1 - (input_a | input_b)

    raise ValueError(
        f"Unsupported gate type: {gate_type}. "
        f"Choose one of {', '.join(GATE_TYPES)}."
    )
