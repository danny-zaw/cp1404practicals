# 2. Debugging

"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
    """Get score from user and determine result."""
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)

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

