#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """print the element of x

    Args:
    my_list(list):the list  to print element from
    x:the number of element of my_list to print
    Returns: 
    the number of elements printed
    """
    count = 0
    for i in range(x):
        try:
            print("{} ".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print()
    return count

