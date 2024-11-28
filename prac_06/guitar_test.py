"""
CP1404 - Practical 6
Test Program for Guitar class

--- Completing the test program ---
Estimated : 10 minutes
Actual    : 9 minutes
"""

from prac_06.guitar import Guitar

guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013, 26035.40)

print(f"{guitar.name} get_age() - Expected 102. Got {guitar.get_age()}")
print(f"{another_guitar.name} get_age() - Expected 11. Got {another_guitar.get_age()}")
print(f"{guitar.name} - Expected True. Got {guitar.is_vintage()}")
print(f"{another_guitar.name} is vintage() - Expected False. Got {another_guitar.is_vintage()}")