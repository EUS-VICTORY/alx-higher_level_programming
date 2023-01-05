#!/usr/bin/python3
for i in range(122, 96, -1):
    print("{:c}".format(chr if (chr % 2 == 0) else (chr - 32)), end='')
