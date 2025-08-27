"""Python file with security vulnerabilities for ASH and CodeQL testing."""

import os
import pickle
import subprocess
import hashlib
import random
from typing import Any


# SQL Injection vulnerability
def get_user_data(user_id: str):
    """Vulnerable to SQL injection."""
    # Never use string formatting for SQL queries
    query = f"SELECT * FROM users WHERE id = {user_id}"
    # In real code, would execute: cursor.execute(query)
    return query


# Command injection vulnerability
def run_system_command(filename: str):
    """Vulnerable to command injection."""
    # Never use shell=True with user input
    result = subprocess.run(
        f"cat {filename}",
        shell=True,
        capture_output=True,
        text=True
    )
    return result.stdout


# Hardcoded credentials (security issue)
def connect_to_database():
    """Contains hardcoded credentials."""
    DATABASE_PASSWORD = "admin123"  # Never hardcode passwords
    API_KEY = "sk-1234567890abcdefghijklmnop"  # Never hardcode API keys
    SECRET_TOKEN = "secret_token_12345"  # Never hardcode tokens
    
    connection_string = f"postgresql://admin:{DATABASE_PASSWORD}@localhost/db"
    return connection_string


# Unsafe deserialization
def load_user_data(serialized_data: bytes) -> Any:
    """Vulnerable to unsafe deserialization attacks."""
    # pickle.loads can execute arbitrary code
    return pickle.loads(serialized_data)


# Path traversal vulnerability
def read_file(filename: str):
    """Vulnerable to path traversal attacks."""
    # No input validation allows ../../../etc/passwd
    filepath = f"/var/data/{filename}"
    with open(filepath, 'r') as f:
        return f.read()


# Weak cryptography
def hash_password(password: str):
    """Uses weak hashing algorithm."""
    # MD5 is cryptographically broken, never use for passwords
    return hashlib.md5(password.encode()).hexdigest()


# Insecure random number generation
def generate_token():
    """Uses insecure random for security-sensitive operation."""
    # random module is not cryptographically secure
    token = random.randint(100000, 999999)
    return str(token)


# Eval with user input (code injection)
def calculate_expression(expr: str):
    """Vulnerable to code injection via eval."""
    # eval() executes arbitrary Python code
    result = eval(expr)
    return result


# XXE vulnerability in XML parsing
def parse_xml(xml_string: str):
    """Vulnerable to XML External Entity attacks."""
    import xml.etree.ElementTree as ET
    # Default XML parser is vulnerable to XXE
    root = ET.fromstring(xml_string)
    return root


# SSRF vulnerability
def fetch_url(url: str):
    """Vulnerable to Server-Side Request Forgery."""
    import urllib.request
    # No validation allows internal network access
    response = urllib.request.urlopen(url)
    return response.read()


# Insecure temporary file
def create_temp_file(data: str):
    """Creates predictable temporary file."""
    # Predictable filename in shared directory
    temp_file = f"/tmp/app_temp_{os.getpid()}.txt"
    with open(temp_file, 'w') as f:
        f.write(data)
    return temp_file


# Using assert for security (gets removed in optimized code)
def validate_admin(user_role: str):
    """Incorrectly uses assert for security check."""
    # assert statements are removed with python -O
    assert user_role == "admin", "Unauthorized access"
    return True


# Logging sensitive information
def process_payment(card_number: str, cvv: str):
    """Logs sensitive payment information."""
    import logging
    # Never log sensitive data
    logging.info(f"Processing payment for card: {card_number}, CVV: {cvv}")
    return "Payment processed"


# Race condition vulnerability
COUNTER = 0

def increment_counter():
    """Has race condition in multi-threaded environment."""
    global COUNTER
    # Not thread-safe, can lead to race conditions
    temp = COUNTER
    temp = temp + 1
    COUNTER = temp
    return COUNTER


# Open redirect vulnerability
def redirect_user(next_url: str):
    """Vulnerable to open redirect attacks."""
    # No validation allows redirect to malicious sites
    return f"Location: {next_url}"


if __name__ == "__main__":
    # Example of unsafe operations (DO NOT RUN)
    print("This file contains intentional security vulnerabilities")
    print("For testing ASH and CodeQL security scanning only")
    
    # These would be flagged by security scanners
    password = "weak_password"
    weak_hash = hash_password(password)
    print(f"Weak hash: {weak_hash}")
    
    # Hardcoded secret in string
    secret = "aws_secret_access_key_AKIAIOSFODNN7EXAMPLE"