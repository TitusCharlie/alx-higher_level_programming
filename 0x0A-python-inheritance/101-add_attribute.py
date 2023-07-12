#!/usr/bin/python3
"""
===============================
module that adds new attributes
===============================
"""


def add_attribute(obj, name, value):
  """add attr to an obj"""
  
  if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
