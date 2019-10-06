#!/usr/bin/python3
""" This module defines the Square class """


class Square():
    """ This class defines square instances """

    width = 0
    height = 0

    def __init__(self, size=0):
        """ New instance of a square """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ New instance of a square """
        new = ['width', 'height', 'size']
        if not args:
            for key, value in kwargs.items():
                if key in new:
                    setattr(self, key, value)
                self.width = kwargs[key]
                self.height = kwargs[key]

    @property
    def size(self):
        """ This getter function returns the size of a Square instance """
        return self.size

    @size.setter
    def size(self, size):
        """ This setter function validates and sets the size of a Square\
        instance """
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """ Perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Defines the str method for an instance of the square """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(size=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
