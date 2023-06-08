#!/usr/bin/python3
import argparse


def infinite_add():
    element = argparse.ArgumentParser(description='print the result of the '
                                                  'addition of all arguments')
    element.add_argument('numbers', type=int, nargs='*')

    tokens = element.parse_args()
    result = tokens.numbers
    print(sum(result))


if __name__ == "__main__":
    infinite_add()
