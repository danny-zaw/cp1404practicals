"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random

def main():
    """Get a score from user and generate a random score, then determine results."""
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)

    random_score = random.randint(1,100)
    random_result = determine_result(random_score)
    print(f"Random score: {random_score}, {random_result}")

def determine_result(score):
    """Determine result based on score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()

