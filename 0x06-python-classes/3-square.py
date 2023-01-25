#!/usr/bin/python3
"""define a class Square"""

class Square:
    """define a function _init_""

    def _init_(self, size=0):
    """if statement"""
    if type(size is not int
    """raise error"""
    raise TypeError("size must be an integer")
    elif size < 0:
    """raise error"""
    raise ValueError("size must be >= 0")
    else:
    """initialise size"""
    self._size = size
    """defines area function"""
    def area(self):
    """returns area""
   return  self._size**2
