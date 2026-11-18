FAULT_LOCATIONS = ("X1", "X2", "X3", "A", "B")
STUCK_VALUES = (0, 1)


def make_fault(location: str, stuck_at: int) -> dict:
    location = location.upper()

    if location not in FAULT_LOCATIONS:
        raise ValueError(
            f"Unknown fault location: {location}. "
            f"Choose one of {', '.join(FAULT_LOCATIONS)}."
        )

    if stuck_at not in STUCK_VALUES:
        raise ValueError("Stuck-at value must be 0 or 1.")

    return {"location": location, "stuck_at": stuck_at}


def all_single_faults() -> list[dict]:
    """Return the 10 single stuck-at faults for this circuit."""
    return [
        make_fault(location, stuck_at)
        for location in FAULT_LOCATIONS
        for stuck_at in STUCK_VALUES
    ]


def fault_label(fault: dict) -> str:
    return f"{fault['location']}-SA{fault['stuck_at']}"
