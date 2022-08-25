#!/usr/bin/python3
def uppercase(str):
    j = ord('A')
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            i = ord(c) - ord('a')
            c = chr(i + j)
        print("{:s}".format(c), end='')
    print("")
