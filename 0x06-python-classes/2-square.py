#!/usr/bin/python3

"""defines a class named Square"""



class Square:
    
    """defines a function named _init_ """
    
    def _init_(self, size=0):
        
        """if statement"""
        
        if type(size) != int:
            
            """raise an error"""
            
            raise TypeError("size must be an integer")
        
        elif size < 0
        
        """raise an error"""
        
        raise ValueError("size must be >= 0")
    
else:
    
    """initialise _size of self with size"""
    
    self._size = size
    
