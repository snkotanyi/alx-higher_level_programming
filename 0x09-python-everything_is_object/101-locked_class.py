#!/usr/bin/python3
"""
module that containts a clas that avoids
dynmaically created attributes
"""


class LockedClass:
    """no attributes"""
    __slots__ = ['first_name']

    def __init__(self):
        """ Init method """
        pass
