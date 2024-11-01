"""
CP1404 - Practical 6
ProgrammingLanguage Class
Estimate : 20 minutes
Actual   :
"""

class ProgrammingLanguage:

    def __init__(self, language, typing, reflection, year):
        """Initialise instances for language, language, reflection and year."""
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return true if language is dynamic."""
        return self.is_dynamic().lower == "dynamic"

    def __str__(self):
        """Return string representation of language."""
        return f"{self.language}, {self.typing} Typing, Reflection {self.reflection}, First appeared in {self.year}"
