# how-to-find-complete-minimal-test-set

A Python-based project for analyzing logic circuits and detecting Stuck-at faults using test vectors.

## Features

- Supports AND, OR, NAND, and NOR gates.
- Simulates healthy and faulty circuits.
- Analyzes 10 possible Stuck-at faults (SA0 and SA1).
- Determines whether each fault is detectable.
- Displays test vectors that detect each fault.
- Supports automatic and manual fault analysis.

## Project Structure

- **Automatic Analysis:** Checks all possible Stuck-at faults and identifies detecting test vectors for each fault.
- **Manual Fault Analysis:** Allows users to select a specific fault location and stuck-at value and analyze its behavior.

## Technologies

- Python
- itertools

## How to Run

Clone the repository:

```bash
git clone https://github.com/mohamadreza-dousti/how-to-find-complete-minimal-test-set.git
```

Navigate to the project directory:

```bash
cd how-to-find-complete-minimal-test-set
cd cmts
```

Run the desired program:

```bash
python main.py
```

OR

```bash
cd how-to-find-complete-minimal-test-set
```

Run the desired program:

```bash
python cmts.py
