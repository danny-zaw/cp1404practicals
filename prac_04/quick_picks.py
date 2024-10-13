"""
CP1404 - Prac 4
Quick Pick Program
"""

import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

number_of_quick_picks = int(input("How many quick picks? "))

for i in range(number_of_quick_picks):
    quick_picks = []
    while len(quick_picks) < NUMBERS_PER_PICK:
        random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if random_number not in quick_picks:
            quick_picks.append(random_number)
    quick_picks.sort()
    print(" ".join(f"{number:2}" for number in quick_picks))
