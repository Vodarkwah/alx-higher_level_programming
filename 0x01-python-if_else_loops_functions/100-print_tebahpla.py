#!/usr/bin/python3
i = ord('z')
while i >= ord('a'):
    if i % 2 != 0:
        j = ord('Z') - (ord('z') - i)
    else:
        j = i
    print("{}".format(chr(j)), end="")
    i = i - 1
