#!/usr/bin/python3
"""
The module made up of a function that prints a square with the character #
"""
def print_square(size):
    """Function that prints a square with the character #
    Args:
    size: size of the square printed
    
    Return:
    No return
    Raises:
    TypeError: if size of square is not an integer number
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range size:
        print("#" * size)
        
