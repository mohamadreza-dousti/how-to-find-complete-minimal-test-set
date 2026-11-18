from test_generator import generate_tests
from faults import all_single_faults

def simulate_fault_for_test(circuit, test, fault):
    healthy = circuit.simulate(*test)
    faulty = circuit.simulate(*test, fault=fault)
    return {
        "healthy_output": healthy["Y"],
        "faulty_output": faulty["Y"],
        "detected": int(healthy["Y"] != faulty["Y"]),
        "healthy_values": healthy,
        "faulty_values": faulty,
    }

def run_fault_simulation(circuit):
    results = {}
    for test in generate_tests():
        results[test] = {}
        for fault in all_single_faults():
            result = simulate_fault_for_test(circuit, test, fault)
            results[test][f"{fault['location']}-SA{fault['stuck_at']}"] = result
    return results
