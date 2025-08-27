"""Sample file with potential security issues for testing."""

import pickle
import subprocess
import os
from typing import Any


def unsafe_deserialization(data: bytes) -> Any:
    """Unsafe deserialization that could execute arbitrary code."""
    # This is unsafe - pickle can execute arbitrary code
    return pickle.loads(data)


def unsafe_command_execution(user_input: str) -> str:
    """Execute shell command with user input - potential command injection."""
    # This is vulnerable to command injection
    result = subprocess.check_output(f"echo {user_input}", shell=True)
    return result.decode()


def hardcoded_password() -> dict:
    """Function with hardcoded credentials."""
    # Hardcoded credentials - security issue
    config = {
        "username": "admin",
        "password": "secretpassword123",
        "api_key": "sk-1234567890abcdef"
    }
    return config


def sql_injection_vulnerable(user_id: str) -> str:
    """SQL query vulnerable to injection."""
    # This is vulnerable to SQL injection
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return query


def path_traversal_vulnerable(filename: str) -> str:
    """File operation vulnerable to path traversal."""
    # Vulnerable to path traversal attacks
    file_path = f"/var/data/{filename}"
    with open(file_path, 'r') as f:
        return f.read()


def weak_random_generation() -> int:
    """Using weak random for security purposes."""
    import random
    # Using non-cryptographic random for security
    return random.randint(100000, 999999)


def eval_user_input(expression: str) -> Any:
    """Using eval with user input - dangerous."""
    # eval() with user input is extremely dangerous
    return eval(expression)


def insecure_temp_file() -> str:
    """Create temp file insecurely."""
    import tempfile
    # Predictable temp file name
    temp_file = f"/tmp/myapp_temp_{os.getpid()}.txt"
    with open(temp_file, 'w') as f:
        f.write("temporary data")
    return temp_file


if __name__ == "__main__":
    # Example usage (DO NOT RUN WITH UNTRUSTED INPUT)
    print("This file contains intentional security issues for testing")
    print("DO NOT use this code in production!")
    
    # These are examples of what NOT to do
    config = hardcoded_password()
    print(f"Config loaded: {config['username']}")
    
    # Demonstrating SQL injection vulnerability
    query = sql_injection_vulnerable("1 OR 1=1")
    print(f"Generated query: {query}")