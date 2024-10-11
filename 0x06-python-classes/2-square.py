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

	def __init__(self, size=0):
	"""
	Initialize a new Square instance.

	Args:
		size (int): The size of the square.
	"""
	if not isinstance(size, int):
		raise TypeError('size must be an integer')
	if size < 0:
		raise ValueError('size must be >= 0')
	self.__size = size
