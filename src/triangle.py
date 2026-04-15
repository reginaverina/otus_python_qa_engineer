"""
This module provides functions for calculating triangle roots.
"""
from math import sqrt
from figure import Figure


class Triangle(Figure):
    """Parameters of a triangle."""
    def __init__(self, side_a, side_b, side_c):
        if side_a == 0 or side_b == 0 or side_c == 0:
            raise ValueError("Ops! All sides must be greater than zero.")
        if side_a < 0 or side_b < 0 or side_c < 0:
            raise ValueError("Oh no! Please, use a positive numbers.")
        if side_a + side_b > side_c and side_b + side_c > side_a and side_c + side_a > side_b:
            self.side_a = side_a
            self.side_b = side_b
            self.side_c = side_c
            return
        raise ValueError("Such a triangle cannot be created.")

    @property
    def get_area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        p_a = p - self.side_a
        p_b = p - self.side_b
        p_c = p - self.side_c
        return sqrt(p * p_a * p_b * p_c)

    @property
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
