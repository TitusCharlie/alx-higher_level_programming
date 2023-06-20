#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    result = a_dictionary.copy()
    for i in list(a_dictionary):
        result[i] *=2 
#    for k, v in a_dictionary.items():
 #       result[k] = v * 2
    return result
