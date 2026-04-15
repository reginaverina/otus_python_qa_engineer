"""
This module provides functions for calculating circle roots.
"""
import math
from figure import Figure


class Circle(Figure):
    """Parameters of a circle."""
    def __init__(self, side_r):
        if side_r == 0:
            raise ValueError("Ops! Radius must be greater than zero.")
        if side_r < 0:
            raise ValueError("Oh no! Please, use a positive numbers.")

        self.side_r = side_r

    @property
    def get_area(self):
        return math.pi * self.side_r ** 2

    @property
    def get_perimeter(self):
        return 2 * math.pi * self.side_r
