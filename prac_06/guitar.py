"""
CP1404 - Practical 6
Program   : Guitar
Estimated : 25 minutes
Actual    :
"""

CURRENT_YEAR = 2024
VINTAGE_THRESHOLD = 50

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """ """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """ """
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """ """
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """ """
        return self.get_age() >= VINTAGE_THRESHOLD
