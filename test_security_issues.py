#!/usr/bin/env python3
"""
Test file with intentional security issues for ASH testing
"""

import subprocess
import pickle
import os

# Hardcoded credentials (security issue)
API_KEY = "sk-1234567890abcdef"
PASSWORD = "admin123"
SECRET_TOKEN = "secret_abc123"

def unsafe_command_execution(user_input):
    """Execute shell command with user input - command injection vulnerability"""
    command = f"ls {user_input}"
    result = subprocess.call(command, shell=True)  # Security issue: shell=True
    return result

def unsafe_pickle_load(data):
    """Unsafe deserialization - pickle vulnerability"""
    return pickle.loads(data)  # Security issue: unsafe deserialization

def sql_injection_example(user_id):
    """SQL injection vulnerability example"""
    query = f"SELECT * FROM users WHERE id = {user_id}"  # SQL injection
    return query

def weak_random_generation():
    """Weak random number generation"""
    import random
    return random.random()  # Security issue: weak PRNG

def path_traversal_vulnerability(filename):
    """Path traversal vulnerability"""
    file_path = f"/var/uploads/{filename}"
    with open(file_path, 'r') as f:  # No path validation
        return f.read()

# Hardcoded URL with credentials
DATABASE_URL = "postgresql://admin:password123@localhost:5432/mydb"

if __name__ == "__main__":
    # Test the vulnerable functions
    unsafe_command_execution("../etc/passwd")
    print(f"Using API key: {API_KEY}")
    weak_random_generation()