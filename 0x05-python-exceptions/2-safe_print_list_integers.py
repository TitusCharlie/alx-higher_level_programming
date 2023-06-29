#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = integers = 0
    while True:
        try:
            if i < x:
                print("{:d}".format(my_list[i]), end="")
                i += 1
                integers += 1
            else:
                return integers
        except (IndexError, ValueError, TypeError):
            i += 1
