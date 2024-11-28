"""
CP1404 - Practical 6
Guitar Class

--- Writing the class ---
Estimated : 15 minutes
Actual    : 15 minutes
"""

CURRENT_YEAR = 2024
VINTAGE_AGE = 50

class Guitar:
    """Guitar Class for storing name, year and cost details."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar instance."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Get the age of the guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage based on age."""
        return self.get_age() >= VINTAGE_AGE
