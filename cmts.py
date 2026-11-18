from itertools import product


def gate(gate_type, a, b):
    if gate_type == 1:
        return a & b
    elif gate_type == 2:
        return a | b
    elif gate_type == 3:
        return 1 - (a & b)
    elif gate_type == 4:
        return 1 - (a | b)


def simulate(x1, x2, x3, g1, g2, g3, fault_location=None, stuck_value=None):
    if fault_location == "X1":
        x1 = stuck_value
    elif fault_location == "X2":
        x2 = stuck_value
    elif fault_location == "X3":
        x3 = stuck_value

    a = gate(g1, x1, x2)
    b = gate(g2, x2, x3)

    if fault_location == "A":
        a = stuck_value
    elif fault_location == "B":
        b = stuck_value

    y = gate(g3, a, b)

    return y


def select_gate(gate_number):
    print(f"\\nSelect Gate {gate_number}:")
    print("1. AND")
    print("2. OR")
    print("3. NAND")
    print("4. NOR")

    while True:
        choice = input("Enter choice: ")

        if choice in ["1", "2", "3", "4"]:
            return int(choice)

        print("Invalid choice.")


def select_fault_location():
    print("\nSelect Fault Location:")
    print("1. X1")
    print("2. X2")
    print("3. X3")
    print("4. A")
    print("5. B")

    locations = {
        "1": "X1",
        "2": "X2",
        "3": "X3",
        "4": "A",
        "5": "B"
    }

    while True:
        choice = input("Enter choice: ")

        if choice in locations:
            return locations[choice]

        print("Invalid choice.")


def select_stuck_value():
    print("\nSelect Stuck-at Fault:")
    print("0. SA0")
    print("1. SA1")

    while True:
        choice = input("Enter choice: ")

        if choice in ["0", "1"]:
            return int(choice)

        print("Invalid choice.")


def main():
    print("Circuit Configuration")

    g1 = select_gate(1)
    g2 = select_gate(2)
    g3 = select_gate(3)

    fault_location = select_fault_location()
    stuck_value = select_stuck_value()

    tests = list(product([0, 1], repeat=3))
    detecting_tests = []

    print("\nTest Results")
    print("-" * 55)
    print("X1 X2 X3 | Healthy Y | Faulty Y | Detection")
    print("-" * 55)

    for x1, x2, x3 in tests:
        healthy_y = simulate(x1, x2, x3, g1, g2, g3)

        faulty_y = simulate(
            x1, x2, x3,
            g1, g2, g3,
            fault_location,
            stuck_value
        )

        detected = healthy_y != faulty_y

        if detected:
            detecting_tests.append((x1, x2, x3))

        print(
            f"{x1}  {x2}  {x3}  |"
            f"     {healthy_y}     |"
            f"    {faulty_y}    |"
            f"    {'YES' if detected else 'NO'}"
        )

    print("-" * 55)

    print(f"\\nSelected Fault: {fault_location}-SA{stuck_value}")

    print("\nDetecting Test Vectors:")

    if detecting_tests:
        for test in detecting_tests:
            print(test)
    else:
        print("No test vector can detect this fault.")


if __name__ == "__main__":
    main()