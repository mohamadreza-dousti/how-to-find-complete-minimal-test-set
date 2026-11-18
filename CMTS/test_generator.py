from itertools import product

def generate_tests() -> list[tuple[int, int, int]]:
    return list(product((0, 1), repeat=3))
