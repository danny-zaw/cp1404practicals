"""
CP1404 - Practical 6
ProgrammingLanguage Class
Estimate : 20 minutes
Actual   :
"""

class ProgrammingLanguage:

    def __init__(self, language_name, typing, reflection, year):
        """Initialise instances for language, language, reflection and year."""
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
