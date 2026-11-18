from gates import evaluate_gate, GATE_TYPES
from faults import make_fault


class Circuit:
    def __init__(self, gate1: str, gate2: str, gate3: str):
        self.gates = {
            "G1": self._validate_gate(gate1),
            "G2": self._validate_gate(gate2),
            "G3": self._validate_gate(gate3),
        }

    @staticmethod
    def _validate_gate(gate_type: str) -> str:
        gate_type = gate_type.upper()
        if gate_type not in GATE_TYPES:
            raise ValueError(
                f"Invalid gate type: {gate_type}. "
                f"Choose one of {', '.join(GATE_TYPES)}."
            )
        return gate_type

    def simulate(self, x1: int, x2: int, x3: int,
                 fault: dict | None = None) -> dict:
        inputs = {"X1": x1, "X2": x2, "X3": x3}
        if any(value not in (0, 1) for value in inputs.values()):
            raise ValueError("All primary inputs must be 0 or 1.")

        if fault is not None:
            fault = make_fault(fault["location"], fault["stuck_at"])
            location = fault["location"]
            stuck_at = fault["stuck_at"]
            if location in inputs:
                inputs[location] = stuck_at

        a = evaluate_gate(self.gates["G1"], inputs["X1"], inputs["X2"])
        b = evaluate_gate(self.gates["G2"], inputs["X2"], inputs["X3"])

        if fault is not None:
            if fault["location"] == "A":
                a = fault["stuck_at"]
            elif fault["location"] == "B":
                b = fault["stuck_at"]

        y = evaluate_gate(self.gates["G3"], a, b)

        return {
            "X1": inputs["X1"],
            "X2": inputs["X2"],
            "X3": inputs["X3"],
            "A": a,
            "B": b,
            "Y": y,
        }
