# Password Strength Checker & Generator

A simple, effective Python-based tool to validate the strength of user passwords or generate new ones. This script uses regular expressions and cryptographically secure randomizing to ensure your credentials are robust.

## Features

The script now offers two primary modes:

* **Password Validator:** Checks against standard security requirements (Length, Digits, Uppercase, Lowercase).
* **Random Password Generator:** Automatically creates a 16-character strong password using `secrets`.
* **Expanded Character Support:** Now includes all standard symbols via `string.punctuation`.

## How It Works

1. **Validation:** The application uses the Python `re` module to perform pattern matching. If a password fails, it provides specific feedback on what is missing.
2. **Generation:** Using the `secrets` module, the script pulls random characters from a pool of letters, digits, and symbols to form a non-predictable string.

## Getting Started

### Prerequisites

* **Python 3.x** installed on your system (Works on Fedora/Linux).

### Running the Script

1. Open your terminal in the project directory.
2. Run the command:
```bash
python pass.py

```


3. Enter **1** to check a password or **2** to generate a random one.

## Example Output

```text
Choose: (1) Check Password (2) Generate Random: 2
Generated Password: k#9Fv2_zL!pQ7m*X

```

