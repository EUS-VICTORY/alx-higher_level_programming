#!/bin/bash/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d} ".format(my_list[i]))
        except IndexError:
            count += 1
    return count
