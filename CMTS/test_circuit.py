import unittest

from gates import evaluate_gate
from circuit import Circuit
from faults import all_single_faults
from detection_matrix import build_detection_matrix, get_detecting_tests


class GateTests(unittest.TestCase):
    def test_gate_truth_values(self):
        self.assertEqual(evaluate_gate("AND", 1, 1), 1)
        self.assertEqual(evaluate_gate("OR", 0, 1), 1)
        self.assertEqual(evaluate_gate("NAND", 1, 1), 0)
        self.assertEqual(evaluate_gate("NOR", 0, 0), 1)


class CircuitTests(unittest.TestCase):
    def test_topology_and_shared_x2(self):
        # G1=AND, G2=OR, G3=AND
        circuit = Circuit("AND", "OR", "AND")
        result = circuit.simulate(1, 1, 0)
        self.assertEqual(result["A"], 1)  # 1 AND 1
        self.assertEqual(result["B"], 1)  # 1 OR 0
        self.assertEqual(result["Y"], 1)  # 1 AND 1

    def test_x2_fault_changes_shared_net(self):
        circuit = Circuit("AND", "OR", "AND")
        result = circuit.simulate(1, 1, 0, {"location": "X2", "stuck_at": 0})
        self.assertEqual(result["X2"], 0)
        self.assertEqual(result["A"], 0)  # 1 AND 0
        self.assertEqual(result["B"], 0)  # 0 OR 0

    def test_output_net_faults_are_applied_before_g3(self):
        circuit = Circuit("AND", "OR", "AND")
        result = circuit.simulate(1, 1, 0, {"location": "A", "stuck_at": 0})
        self.assertEqual(result["A"], 0)
        self.assertEqual(result["Y"], 0)

    def test_all_ten_faults_exist(self):
        self.assertEqual(len(all_single_faults()), 10)


class DetectionTests(unittest.TestCase):
    def test_detecting_tests_are_returned_for_each_fault(self):
        circuit = Circuit("AND", "OR", "AND")
        tests, labels, matrix = build_detection_matrix(circuit)
        detecting_tests = get_detecting_tests(labels, matrix)

        self.assertEqual(set(detecting_tests), set(labels))
        for label in labels:
            for test in detecting_tests[label]:
                self.assertEqual(matrix[test][label], 1)


if __name__ == "__main__":
    unittest.main()
