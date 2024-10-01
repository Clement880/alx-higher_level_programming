#!/usr/bin/python3
"""
Module 1-square
This module defines a class named Square with a private instance attribute size.
"""

class Square:
    """
    Class that defines a square.

    Attributes:
        size (int): The size of the square (private).
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
