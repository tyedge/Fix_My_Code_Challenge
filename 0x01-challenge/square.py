#!/usr/bin/python3
""" This module defines the Square class """


class Square():
    """ This class defines square instances """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ New instance of a square """
        new = ['width', 'height']
        if not args:
            for key, value in kwargs.items():
                if key in new:
                    setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Defines the str method for an instance of the square """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
