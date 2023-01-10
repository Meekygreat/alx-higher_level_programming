#!/usr/bin/python3
"""Module 10-square.py
a class Square that inherits from Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class Square that inherits from Rectangle
    Private instance attribute size.
    Public method area().
    """

    def __init__(self, size):
        """Initializing a Square.
        Args:
           - size: size of the square.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return super().__str__()

    def area(self):
        """Computes the area of a Square instance.
        Overwrites the area() mthd from Rectangle.
        """

        return self.__size ** 2
