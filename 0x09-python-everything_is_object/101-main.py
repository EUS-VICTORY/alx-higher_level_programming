#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

lc = Lockedclass()
lc.first_name = "John"
try:
    lc.last_name = "Snow"
except Excception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
    
