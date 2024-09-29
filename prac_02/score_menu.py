"""
CP1404 Practical 2
Score Menu Program

Pseudocode:

function main()
    print menu
    get option
    while option != "Q"
        if option == "G"
            get valid score
        elif option == "P"
            result = determine_result(score)
            print result
        elif option == "S"
            print_stars(score)
        print menu
        get option
    print Thanks for playing

function get_valid_score(score)
    while score < 0 or score > 100
        print Not valid message
        get score
    return score

function determine_result(score)
    if score < 0 or score > 100
        return Invalid score
    else if score >= 90
        return Excellent
    else if score >= 50
        return Passable
    else
        return Bad

function print_stars(score)
    for each score in score
        print *
"""


def main():
    """Print menu and print results based on option."""
    menu = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
    print(menu)
    option = input(">>> ").upper()
    while option != "Q":
        if option == "G":
            score = int(input("Enter your score: "))
            score = get_valid_score(score)
        elif option == "P":
            result = determine_result(score)
            print(result)
        elif option == "S":
            print_stars(score)
            print()
        print(menu)
        option = input(">>> ").upper()
    print("Thanks for playing!")

def get_valid_score(score):
    """Get a valid score between 0 and 100 inclusive."""
    while score < 0 or score > 100:
        print("Score must be between 0 and 100")
        score = int(input("Enter your score: "))
    return score

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

def print_stars(score):
    """Print stars based on score."""
    for i in range(score):
        print("*", end="")

main()


