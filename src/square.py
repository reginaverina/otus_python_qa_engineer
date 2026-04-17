"""
This module provides functions for calculating square roots.
"""
from rectangle import Rectangle


class Square(Rectangle):
    """Parameters of a square."""
    def __init__(self, side_a):
        if side_a == 0:
            raise ValueError("Your number must be greater than zero.")
        if side_a < 0:
            raise ValueError("Oh no! Please, use a positive number.")

        super().__init__(side_a, side_a)

    @property
    def get_area(self):
        return self.side_a ** 2

    @property
    def get_perimeter(self):
        return self.side_a * 4
