# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 13:57:58 2021

OBJECT OREINTATED PROGRAMMING

"""
from math import pi


class Shape:
    """Shape class"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        """Move shape by delta_x and delta_y"""
        self.x = self.x + delta_x
        self.y = self.y + delta_y


class Square(Shape):
    def __init__(self, side=1, x=0, y=0):
        super().__init__(x, y)
        self.side = side

    def area(self):
        self.area = self.side ** 2
        # return self.area

    def perimeter(self):
        self.__perimeter = self.side * 4
        # return self.perimeter


class Circle(Shape):
    def __init__(self, r=1, x=0, y=0):
        """Create a circle with the given radius"""
        super().__init__(x, y)
        self.radius = r

    def circumference(self):
        """Calculate a return circumference"""
        self.circumference = 2 * self.radius * pi
        # return self.circumference

    def area(self):
        self.area = pi * self.radius ** 2
        # return self.area


square1 = Square(side=5)
# print(square1.__perimeter)
print(square1.area)
square1.perimeter()
square1.area()

circle1 = Circle(r=3)
circle1.circumference()
circle1.area()
circle1.move(2, 3)
circle1.x
circle1.y

dir(circle1)

hasattr(circle1, 'radius')
issubclass(Circle, Shape)
issubclass(Shape, Circle)
