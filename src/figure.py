"""
This module provides functions for calculating abstract class roots.
"""
from abc import ABC, abstractmethod


class Figure(ABC):
    """Parameters of an abstract figure."""
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("The other figure must be an instance of Figure.")
        return self.get_area + other_figure.get_area
