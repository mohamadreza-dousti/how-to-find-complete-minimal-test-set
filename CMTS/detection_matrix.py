from faults import all_single_faults, fault_label
from fault_simulator import run_fault_simulation
from test_generator import generate_tests

def build_detection_matrix(circuit):
    tests = generate_tests()
    labels = [fault_label(f) for f in all_single_faults()]
    simulation = run_fault_simulation(circuit)
    matrix = {
        test: {label: simulation[test][label]["detected"] for label in labels}
        for test in tests
    }
    return tests, labels, matrix

def classify_faults(labels, matrix):
    detectable, undetectable = [], []
    for label in labels:
        if any(matrix[test][label] for test in matrix):
            detectable.append(label)
        else:
            undetectable.append(label)
    return detectable, undetectable


def get_detecting_tests(labels, matrix):
    detecting_tests = {}
    for label in labels:
        detecting_tests[label] = [
            test for test in matrix
            if matrix[test][label]
        ]
    return detecting_tests
