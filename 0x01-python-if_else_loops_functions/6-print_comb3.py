#!/usr/bin/python3
for i in range(100):
    for j in range(i+1, 10):
        if i == 99:
            print("{}{}".format(i, j))
            break
        print("{}{}".format(i, j), end=", ")
