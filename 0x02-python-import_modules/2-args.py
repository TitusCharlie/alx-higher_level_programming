#!/usr/bin/python3

def list_of_argv():
    string = input()
    argv = string.split()
    if len(argv) > 0:
        if len(argv) > 1:
            print(f"{len(argv)} arguments:")
            num = 1
            for value in argv:
                print(f"{num}: {value}")
                num += 1
        else:
            print(f"1 argument:\n{len(argv)}: {string}")
    else:
        print("0 argument.")


if __name__ == "__main__":
    list_of_argv()
