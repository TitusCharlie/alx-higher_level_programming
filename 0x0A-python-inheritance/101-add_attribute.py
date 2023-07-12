#!/usr/bin/python3
"""
===============================
module that adds new attributes
===============================
"""


def add_attribute(class, obj, attr):
  """add attr to an obj"""
  
  if class.obj == NULL:
    class.obj = attr
  else:
    raise TypeError("can't add new attribute")
