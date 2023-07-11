#!/usr/bin/python3
"""
=====================
module 2-append_write
=====================
"""


def append_write(filename="", text=""):
    """writes a string to a text file"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
