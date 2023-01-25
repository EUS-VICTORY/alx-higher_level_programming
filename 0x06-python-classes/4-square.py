#!/usr/bin/python3

"""define a class Square"""



class Square:
    
    """define a function _init_"""
    
    def _init_(self, size=0):
        
        """initialises size of self with self"""
        
        self.size = size
        

        
        @property
        
        def size(self):
            
            """returns _size of self"""
            
            return self._size
        

        
        @size.setter
        
        def size(self, value):
            
        """if statement"""
        if type(value) is not int
        """raise error""
        raise TypeError("size must be an integer")
        elif value < 0:
        """raise Error"""
        raise ValueError("size must be >= 0")
        else:
        """initialise"""
        self._size = value
        """defines area"""
        def are(self):
        """returns areea"""
        return self._size ** 2
