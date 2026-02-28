# Password Strength Checker

A simple, effective Python-based tool to validate the strength of user passwords. This script checks against standard security requirements using regular expressions to ensure passwords are robust and secure.

## Features

The script evaluates the following criteria:

* **Minimum Length:** At least 8 characters.
* **Digits:** Contains at least one numerical digit ($0-9$).
* **Uppercase:** Contains at least one uppercase letter ($A-Z$).
* **Lowercase:** Contains at least one lowercase letter ($a-z$).
* **Special Characters:** Contains at least one special symbol (e.g., `!`, `@`, `#`, `$`, `%`).

## How It Works

The application uses the Python `re` module to perform pattern matching. If a password fails any of the security checks, the script provides specific feedback on what is missing, rather than just a generic "Invalid" message.

## Getting Started

### Prerequisites

* **Python 3.x** installed on your system.

### Running the Script

1. Clone this repository or download the `pass.py` file.
2. Open your terminal.
3. Navigate to the project directory and run:
```bash
python pass.py

```


4. Enter the password you wish to test when prompted.

## Example Output

```text
Password Strength Checker
Enter your password here: P@ssw0rd1
Your password meets all the security standards

```
