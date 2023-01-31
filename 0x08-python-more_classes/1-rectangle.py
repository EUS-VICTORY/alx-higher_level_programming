#!/usr/bin/python3
"""Defines Rectangle class"""

class Rectangle:
    """Rectangle"""
    def _init_(self, width=0, height=0):
        """initialise width and height"""
        self.width = width
        self.height = height

    @property

    def width(self):
        """width getter"""
        return self._width
    @width.setter
    def width(self, value):
        if type(value) is not int:
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self._width = value

    @property
    def height(self):
        """height getter"""
        return self._height
   @height.setter
    def height(self, value):
        if type(value) is not int:
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    self._height = value

    
