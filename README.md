# ALU32 Design and Test

## Overview

This project implements a 32-bit Arithmetic Logic Unit (ALU) for the RISC-V architecture. The ALU32 can perform multiple computations on 32-bit inputs, including addition, subtraction, logical operations, shifts, and comparison operations. The design follows the modular "build it and box it" principle, resulting in a cleaner and more organized ALU. This is a project for the class CS 3410: Computer System Organization, which I took at Cornell during the fall 2022 semester. 

## Description

The ALU32 comprises five primary computational subcircuits:
1. **ne_eq**: Determines equality or inequality.
2. **add_subtract**: Performs addition and subtraction using the `Add32` circuit.
3. **le_gt**: Evaluates less-than or greater-than conditions.
4. **logicgates**: Executes basic logical operations (AND, OR, XOR, NOR).
5. **subshift**: Handles left and right shifts, both logical and arithmetic.

Additional helper circuits, such as `overflow`, `opselect`, and `reverse`, support the ALU's functionality. The project is tested using custom test cases for each subcircuit to validate correctness under various conditions, including edge cases.

## Getting Started

### Dependencies

To run or modify this project, ensure you have:
- **Logisim Evolution**: For viewing and simulating the circuit.
- **Python 3.x**: For running automated test scripts.

### Installing

1. Download and install **Logisim Evolution** if not already installed.
2. Clone the repository to your local machine.
3. Ensure Python 3.x is installed and set up for running test scripts.

### Executing the Program

#### Viewing and Simulating the ALU

1. Open `CS3410_P1.circ` in **Logisim Evolution**.
2. Simulate the ALU32 by providing inputs and observing outputs.
3. Use Logisim’s probe tool to verify values at different points in the circuit.

#### Running Automated Tests

1. Open a terminal in the repository's root directory.
2. Run the following command to execute all test cases:
   ```bash
   python3 ALU_tests.py

## Authors 
Neeharika Kotimreddy
