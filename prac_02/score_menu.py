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
