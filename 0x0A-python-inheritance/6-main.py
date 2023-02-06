#!/usr/bin/python3
Basegeometry = __import__('6-basegeometry').BaseGeometry

bg = BaseGeometry()

try:
	print(bg.area())
	except Exception as e:
		print("[{}] {}".format(e.__class__.__name__, e))