# ASH Scanner Validation Test

This directory contains renamed test files to validate that the ASH security scanner workflow runs all scanners properly without skipping them.

## Test Files

- **bad_python_code.py** - Python with linting and formatting issues
- **bad_javascript_code.js** - JavaScript with various code quality problems  
- **security_vulnerabilities.py** - Python with intentional security vulnerabilities
- **security_vulnerabilities.js** - JavaScript with security issues

## Expected Results

With the updated ASH workflow that installs scanner dependencies, all scanners should now show PASSED/FAILED status instead of SKIPPED:

- **bandit** - Should detect Python security issues
- **semgrep** - Should detect security patterns in both languages
- **detect-secrets** - Should find hardcoded secrets
- **checkov** - Should run infrastructure checks

## Purpose

This tests the fix for the ASH workflow where scanners were being skipped due to missing UV dependencies. The workflow now manually installs scanner tools via pip.

**WARNING: These files contain intentional vulnerabilities for testing only!**