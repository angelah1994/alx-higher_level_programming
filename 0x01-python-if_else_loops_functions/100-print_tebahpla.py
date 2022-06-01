#!/usr/bin/python
for ascii_num % 2 == 1:
    ascii_num = ascii_num - 32
    print("{:c}".format(ascii_num), end='')
