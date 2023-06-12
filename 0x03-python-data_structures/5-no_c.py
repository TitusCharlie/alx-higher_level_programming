#!/usr/bin/python3
def no_c(my_string):
    result = ""
#    new_string = ""
    for i in range(len(my_string)):
        new_string = my_string[i]
        if new_string == 'C' or new_string == 'c':
            result += ""
        else:
            result += new_string
    return result
