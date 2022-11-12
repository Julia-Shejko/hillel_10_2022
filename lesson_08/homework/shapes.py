"""
Any instance of a Shape class should return. It may be:

    Rectangle
    ----
    |  |
    ----

    or Circle
      --
     -  -
      --
"""

from abc import ABC, abstractmethod
from random import choice


class Shape(ABC):
    @staticmethod
    @abstractmethod
    def draw():
        pass


class Rectangle(Shape):
    @staticmethod
    def draw():
        print("----\n|  |\n----")


class Circle(Shape):
    @staticmethod
    def draw():
        print(" -- \n-  -\n --")


def get_shape() -> Shape:
    """
    This function should return any instance of a Shape class
    """
    options: list = [Rectangle, Circle]
    return choice(options)


def main():

    shape: Shape = get_shape()
    shape.draw()


if __name__ == "__main__":
    main()
