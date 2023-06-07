#!/usr/bin/python3
digit = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - digit)), end="")
    digit = 32 if digit == 0 else 0
