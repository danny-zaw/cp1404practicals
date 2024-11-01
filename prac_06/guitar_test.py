"""
CP1404 - Practical 5
Test Program for Guitar class
"""

from prac_06.guitar import Guitar

guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013, 26035.40)

print(f"Gibson L-5 CES get_age() - Expected 102. Got {guitar.get_age()}")
print(f"Another Guitar get_age() - Expected 11. Got {another_guitar.get_age()}")
print(f"Gibson L-5 CES is_vintage() - Expected True. Got {guitar.is_vintage()}")
print(f"Another Guitar is vintage() - Expected False. Got {another_guitar.is_vintage()}")