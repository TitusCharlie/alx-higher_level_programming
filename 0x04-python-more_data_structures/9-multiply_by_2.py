#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    result = {}
    for k, v in a_dictionary.items:
        if type(v) is not int:
            exit(1)
        result[k] = v * 2
    return result
