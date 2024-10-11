#!/usr/bin/python3
"""
Module 0-add_integer
contains one method and accepts two values of int or loat type
and casts them to int beore adding and
Returning an int sum
"""

def add_integer(a, b=98):
    """
      Return the summation of two arguments
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        if type(a) is float:
            a = int(a)
        if type(b) is float:
            b = int(b)
        return a + b
