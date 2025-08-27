# Clean Code Test

This directory contains clean, well-formatted code examples to test that our GitHub Actions workflows properly pass valid code.

## Files

- **clean_example.py** - Python code following PEP 8 standards with proper type hints and documentation
- **clean_example.js** - JavaScript code with proper JSDoc comments and modern ES6+ syntax

## Purpose

These files should:
1. Pass all Python linting checks
2. Pass all JavaScript linting checks  
3. Not trigger any security warnings from ASH
4. Not trigger any CodeQL issues

This validates that our workflows correctly identify clean code and don't produce false positives.