# Calculator CLI

A robust, interactive command-line calculator built with Python. This utility provides a clean terminal interface for executing fundamental arithmetic operations, complete with input validation and error handling.

## Features

- **Standard Arithmetic Operations**: Supports addition, subtraction, multiplication, and division.
- **Robust Error Handling**: Safely catches non-numeric inputs and handles division-by-zero scenarios gracefully.
- **Interactive Menu-Driven Interface**: Keeps the session active for multiple calculations until explicitly terminated by the user.
- **Unit Tested**: Core mathematical functions are thoroughly tested to ensure reliability.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/abhranilsingharoy-cloud/calculator-cli.git
   ```
2. Navigate into the project directory:
   ```bash
   cd calculator-cli
   ```

### Usage

Run the calculator using the Python interpreter:
```bash
python calculator.py
```

You will be presented with a prompt to select your desired operation. Simply input your choice and follow the on-screen instructions.

### Running the Tests

To verify the mathematical logic, you can execute the integrated test suite:
```bash
python -m unittest test_calculator.py
```

## Architecture

The project emphasizes modularity by separating core arithmetic logic from the CLI interaction layer. This separation of concerns ensures that the code is maintainable and functions can be easily imported and reused in other modules.
