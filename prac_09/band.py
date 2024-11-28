"""
CP1404 Practical 9
Band Class
"""

class Band:
    """Band Class."""

    def __init__(self, name=""):
        """Initialise a Band instance."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band."""
        return f"{self.name} {', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return string on musician playing first or no instrument."""
        return "\n".join(musician.play() for musician in self.musicians)