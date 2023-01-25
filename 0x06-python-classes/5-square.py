#r/bin/python3

"""define a class Square"""



class Square:
    
    """define _init_ function"""
    
    def _init_(self, size=0):
        
        """initialises size of self with self"""
        
        self.size = size
        

        
        @property
        def size(self):
            """returns _size of self"""
            self._size

            @size.setter
            def size(self, value):
                """if statement"""
                if type(value) is not int:
                    """raise error"""
                    raise TypeError("size must be an integer")
                elif value < 0:
                    """raise error"""
                    raise ValueError("size must be >= 0")
                else:
                    """initialise"""
                    self._size = value

                   """" defines area function"""
                def area(self):
                    """returns area"""
                       return self._size**2
                """defines my_print function"""
                def my_print(self):
                       if self._size == 0:
                       print()
else:
    for i in range(self._size):
        for j in range(self._size):
            print("#", end="")
            print()

  

        
