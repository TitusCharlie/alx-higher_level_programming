#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    result = {}
    for k, v in a_dictionary.items():
        if type(v) is not int:
            result[k] = v
        else:
            result[k] = v * 2
    return result
