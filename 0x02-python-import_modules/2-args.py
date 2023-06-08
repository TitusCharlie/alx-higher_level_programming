#!/usr/bin/python3
import argparse

def list_of_argv():
    string = argparse.ArgumentParser(description='print all the arguments in a particulat format')
    string.add_argument('words', nargs='*')
    word = string.parse_args()
    result = word.words
    if len(result) == 0:
        print("0 argument")
    if len(result) > 0:
        if len(result) == 1:
            print("1 argument:")
        else:
            print(f"{len(result)} arguments:")
        num = 1
        for value in result:
            if len(result)== 1:
                print(f"{num}: {value}")
            else:
                print(f"{num}: {value}")
                num += 1


if __name__ == "__main__":
    list_of_argv()
