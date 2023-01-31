#!/usr/bin/python3

""
This module is made up of a function that adds two numbers
"""
def add_integer(a, b=98):
    """Function adds two integers and/or float numbers
       Args:
       a: first number
       b: second number
       Returns:
           the addition of the two given numbers
       Raises:
           TypeError: if a and b aren't integer and/or float numbers
"""
       
       if not isinstance(a, int) and not isinstance(a, float):
           raise TypeError(ä must be an integer")
       if not isinstance(b, int) and not isinstance(b, float):
           raise TypeError("b must be an integer")
       a = int(a)
       b = int(b)
       return (a + b)


