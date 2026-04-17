"""
This module provides functions for calculating rectangle roots.
"""
from figure import Figure


class Rectangle(Figure):
    """Parameters of a rectangle."""
    def __init__(self, side_a, side_b):
        if side_a == 0 and side_b > 0 or side_b == 0 and side_a > 0:
            raise ValueError("Side A or side B must be greater than zero.")
        if side_a < 0 or side_b < 0:
            raise ValueError("Oh no! Please, use a positive numbers.")

        self.side_a = side_a
        self.side_b = side_b

    @property
    def get_area(self):
        return self.side_a * self.side_b

    @property
    def get_perimeter(self):
        return (self.side_a + self.side_b) * 2
