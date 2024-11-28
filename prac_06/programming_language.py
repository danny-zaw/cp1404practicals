"""
CP1404 - Practical 6
ProgrammingLanguage Class

--- Writing the class ---
Estimate : 15 minutes
Actual   : 16 minutes
"""

class ProgrammingLanguage:
    """ Programming Language Class for storing details of different languages."""

    def __init__(self, language_name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance."""
        self.language_name = language_name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return true if language is dynamic."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return string representation of language."""
        return f"{self.language_name}, {self.typing} Typing, Reflection {self.reflection}, First appeared in {self.year}"
