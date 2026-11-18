from gates import GATE_TYPES
from circuit import Circuit
from detection_matrix import (
    build_detection_matrix,
    classify_faults,
    get_detecting_tests,
)

def ask_gate(name):
    while True:
        value = input(f"CHOOSE GATE {name} {GATE_TYPES}: ").strip().upper()
        if value in GATE_TYPES:
            return value
        print("UNDIFIENED GATE")

def main():
    g1, g2, g3 = ask_gate("G1"), ask_gate("G2"), ask_gate("G3")
    circuit = Circuit(g1, g2, g3)

    tests, labels, matrix = build_detection_matrix(circuit)
    detectable, undetectable = classify_faults(labels, matrix)
    detecting_tests = get_detecting_tests(labels, matrix)

    print(f"\\nCIRCUIT: G1={g1}, G2={g2}, G3={g3}")
    print(f"\\nFAULT DETECTION MATRIX:")
    print("TEST  " + "  ".join(f"{label:8}" for label in labels))
    for test in tests:
        bits = "".join(map(str, test))
        row = "  ".join(f"{matrix[test][label]:8}" for label in labels)
        print(f"{bits}   {row}")

    print("\nDETECTABLE FAULTS:")
    print(", ".join(detectable) if detectable else "NO ONE")
    print("\nUNDETECTABLE FAULTS:")
    print(", ".join(undetectable) if undetectable else "NONE")

    print("\nTESTS THAT DETECT EACH FAULT:")
    for label in labels:
        tests_for_fault = detecting_tests[label]
        if tests_for_fault:
            formatted_tests = ["".join(map(str, test)) for test in tests_for_fault]
            print(f"{label}: {', '.join(formatted_tests)}")
        else:
            print(f"{label}: NO DETECTING TEST")

if __name__ == "__main__":
    main()
