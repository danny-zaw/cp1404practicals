"""
CP1404 - Practical 7
Program: My Guitars


"""

import csv

from prac_07.guitar import Guitar

FILENAME = 'guitars.csv'

def main():
    """Load guitars from CSV and display them in sorted order."""
    guitars = load_guitars()

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)

        print(f"{name} ({year}) : ${cost} added.\n")
        name = input("Name: ")

    guitars.sort(reverse=True)
    display_guitars(guitars)

    save_guitars(guitars)
    print(f"List of guitars saved to {FILENAME}")


def load_guitars():
    """Load a list of guitars from CSV file."""
    guitars = []
    in_file = open(FILENAME, 'r', newline='')
    in_file.readline()
    reader = csv.reader(in_file) # use default dialect, Excel
    for row in reader:
        name, year, cost = row[0], int(row[1]), float(row[2])
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
    in_file.close()

    return guitars

def display_guitars(guitars):
    """Display list of guitars."""
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>25} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

def save_guitars(guitars):
     """Save list of guitars to a CSV file."""
     with open(FILENAME,'w', newline='') as out_file:
         for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

main()