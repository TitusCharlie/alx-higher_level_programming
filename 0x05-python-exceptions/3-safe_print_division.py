#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        print("Inside result:{}".format(a / b))
    except ZeroDivisionError:
        print("Inside result: None")
    finally:
        if b != 0:
            return a / b
        else:
            return None
