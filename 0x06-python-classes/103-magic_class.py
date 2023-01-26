#!/usr/bin/python3
"""declares a class called magic class"""
import math

class MagiClass:
    """declaration of _init_ function"""
    def _init_(self, radius=0):
        """initialisation of _MagiClass_ radius with 0"""
        self._MagicClass_radius = 0
        if type(radius) is not int and type radius is not float:
            raise TypeError("radius must be a number")
        self._MagicClass_radius = radius
    """defines a function named area"""
    def area(self):
        """returns area"""
        return self._MagicClass_radius ** 2 * mathpie
    """defines a function named circumference"""
    def circumference(self):
        """returns circumference"""
        return 2 * mathpie * self._MagicClass_radius
        
