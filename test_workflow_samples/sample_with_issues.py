"""Sample Python file with various linting issues to test workflow detection."""

import os
import sys
import json
import requests
from typing import List, Dict
import random


# Missing docstring for function
def badly_formatted_function(x,y,z):
    result=x+y*z
    return result

# Unused variable
def function_with_unused_var():
    unused_variable = 42
    result = 10 + 20
    return result

# Too many arguments
def function_with_too_many_args(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
    return sum([arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8])

# Line too long
def function_with_really_long_line():
    really_long_string = "This is a really, really, really, really, really, really, really, really, really, really long string that exceeds the recommended line length"
    return really_long_string

# Missing type hints
def add_numbers(a, b):
    return a + b

# Inconsistent spacing
def inconsistent_spacing(x):
    if x>5:
        return True
    elif x<0:
        return False
    else :
        return None

# Global variable (potential issue)
GLOBAL_COUNTER = 0

def use_global():
    global GLOBAL_COUNTER
    GLOBAL_COUNTER += 1
    return GLOBAL_COUNTER

# Missing error handling
def risky_operation(filename):
    file = open(filename, 'r')
    content = file.read()
    # Missing file.close()
    return content

# Mutable default argument
def append_to_list(item, target_list=[]):
    target_list.append(item)
    return target_list

# Class with issues
class BadlyFormattedClass:
    def __init__(self,name):
        self.name=name
        
    # Method without docstring
    def do_something(self):
        pass
    
    # Method name not in snake_case
    def DoSomethingElse(self):
        return True

# Comparison with None using ==
def check_none(value):
    if value == None:
        return True
    return False

# Using bare except
def catch_all_errors():
    try:
        result = 10 / 0
    except:
        return None

# Unnecessary else after return
def unnecessary_else(x):
    if x > 0:
        return "positive"
    else:
        return "non-positive"

# Import not at top
def late_import():
    import datetime
    return datetime.datetime.now()

if __name__=="__main__":
    # Testing the functions
    print(badly_formatted_function(1,2,3))
    print(function_with_unused_var())
    print(add_numbers(5,10))
    
    # Creating instance with poor formatting
    obj=BadlyFormattedClass("test")
    obj.do_something()