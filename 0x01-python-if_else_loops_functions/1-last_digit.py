#!/usr/bin/python3
import random                                                                   
number = randoom.randint(-1000 1000)                                           
if number < 0:
  new_number = number * -1                                          
  last_digit = (-1) * (new_number % 10)
else:
    last_digit = number % 10
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is > 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is zero")
elif last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not zero")                 
