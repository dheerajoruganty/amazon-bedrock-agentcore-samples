# Problematic Code Test

This directory contains code with intentional issues to test that our GitHub Actions workflows properly detect and report problems.

## Files

### Linting Issues
- **linting_issues.py** - Python code with formatting, style, and quality issues
- **linting_issues.js** - JavaScript code with various linting problems

### Security Vulnerabilities
- **vulnerable_code.py** - Python code with security vulnerabilities
- **vulnerable_code.js** - JavaScript code with security vulnerabilities

## Expected Workflow Results

This PR should trigger failures/warnings in:

1. **Python Linting** - Should detect multiple issues:
   - Missing docstrings
   - Formatting violations
   - Unused variables
   - Line length issues
   - Missing type hints

2. **JavaScript Linting** - Should detect:
   - Missing semicolons
   - Using var instead of let/const
   - Console.log statements
   - eval() usage
   - Formatting issues

3. **ASH Security Scan** - Should detect:
   - Hardcoded credentials
   - SQL injection vulnerabilities
   - Command injection risks
   - Weak cryptography
   - Path traversal vulnerabilities

4. **CodeQL** - Should identify security and quality issues

## WARNING

**These files contain intentional security vulnerabilities and bad code for testing purposes only. DO NOT use any of this code in production!**

## Updated Testing
This PR now includes the latest ASH workflow fixes to ensure all scanners run properly instead of being skipped.