#!/usr/bin/python3
"""Module 8-rectangle.py.
Inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class Rectangle that inherits from BaseGeometry.
    Private instances attributes:
        - width
        - height
    """

    def __init__(self, width, height):
        """Initializing a Rectangle instance.
        Args:
           width: width of the Rectangle
           height: height of the Rectangle.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
