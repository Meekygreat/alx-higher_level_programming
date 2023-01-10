#!/usr/bin/python3
"""Module 9-rectangle.py.
Inherit from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class Rectangle that inherits from BaseGeometry.
    Private instances attributes:
        - width
        - height
    Public method area
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

    def __str__(self):
        """Returns a formatted string."""

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """Computes the area of the Rectangle instance.
        Overwrites the area() mthd from BaseGeometry.
        """

        return self.__width * self.__height
