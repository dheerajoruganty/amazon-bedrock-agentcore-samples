"""Python code with various linting issues for testing."""

import os, sys, json
import time
from typing import List

# Missing docstring
def calculate_sum(a,b,c):
    result=a+b+c # Bad spacing
    return result

class poorly_formatted: # Class name not CamelCase
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.z = None # Inconsistent spacing
    
    # Missing docstring
    def DoSomething(self): # Method not snake_case
        pass

# Line too long
def function_with_extremely_long_line():
    really_really_really_really_really_really_really_really_really_really_long_variable_name = "This is a very very very very very very very long string that definitely exceeds the recommended line length"
    return really_really_really_really_really_really_really_really_really_really_long_variable_name

# Unused imports and variables
def function_with_unused():
    unused_var = 42
    another_unused = "test"
    result = 10 + 20
    return result

# Missing type hints
def add_numbers(x, y):
    return x + y

# Comparison with None using ==
def check_value(val):
    if val == None:  # Should use 'is None'
        return False
    elif val != None:  # Should use 'is not None'
        return True

# Using bare except
def risky_function():
    try:
        x = 1 / 0
    except:  # Bare except
        pass

# Mutable default argument
def append_item(item, list_arg=[]):
    list_arg.append(item)
    return list_arg

# Global variable modification
counter = 0

def increment():
    global counter
    counter = counter + 1
    return counter

# Unnecessary else after return
def check_positive(n):
    if n > 0:
        return True
    else:  # Unnecessary
        return False

# Import not at top
def late_import():
    import datetime  # Import should be at top
    return datetime.datetime.now()

# Trailing whitespace and tabs
def mixed_indentation():
	x = 1  # Tab indentation
    y = 2  # Space indentation  
	return x + y  # Mixed

# Multiple statements on one line
def multiple_statements(): x = 1; y = 2; return x + y

# Wildcard import
from os import *  # Avoid wildcard imports

# Redefinition of built-in
def list():  # Shadows built-in
    return []

# Missing final newline