# Test Workflow Samples

This directory contains sample Python files created specifically to test GitHub Actions workflows:

## Files

1. **sample_clean.py** - A clean Python file that should pass all linting checks
   - Proper docstrings
   - Type hints
   - Good formatting
   - Following PEP 8 standards

2. **sample_with_issues.py** - A file with intentional linting issues to test detection
   - Missing docstrings
   - Formatting issues
   - Unused variables
   - Line length violations
   - Missing type hints
   - Other common linting problems

3. **test_security.py** - A file with intentional security vulnerabilities to test security scanning
   - Hardcoded passwords
   - SQL injection vulnerabilities
   - Command injection risks
   - Unsafe deserialization
   - Path traversal vulnerabilities
   - Weak random number generation

## Purpose

These files are created to validate that the following GitHub Actions workflows are functioning correctly:
- Ash workflow (security scanning)
- Dependabot
- Linting checks

**WARNING**: The security issues in `test_security.py` are intentional for testing purposes. Do not use any of that code in production environments.