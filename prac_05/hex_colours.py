"""
CP1404 - Prac 5
Program: Hex Colours
"""

COLOUR_TO_CODE = {"Amethyst": "#9966cc", "Aqua": "#00ffff", "Beige": "#f5f5dc", "Black": "#000000",
                  "Blue1": "#0000ff", "Brown": "#a52a2a", "Canary": "#ffff99", "Celeste": "#b2ffff",
                  "Citron": "#9fa91f", "Coral": "#ff7f50"}

colour_name = input("Colour: ")
while colour_name != "":
    try:
        print(f"Hex Code = {COLOUR_TO_CODE[colour_name]}")
    except KeyError:
        print("Invalid colour")
    colour_name = input("Colour: ")

