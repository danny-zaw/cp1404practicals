"""
CP1404 Practical 9
Taxi Simulator Program
Estimated: 1 hour 30 minutes
Actual: 3 hours (including breaks)
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    """Display menu to user and perform tasks based on choice."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_cost = 0.0

    print("Let's drive!")
    print(MENU)

    choice = input(">>> ").lower().strip()
    while choice != 'q':
        if choice == 'c':
            display_taxis(taxis)
            current_taxi = choose_taxi(taxis)
        elif choice == 'd':
            total_cost = drive_taxi(current_taxi, total_cost)
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_cost:.2f}")
        print(MENU)
        choice = input(">>> ").lower().strip()

    print(f"Total trip cost: ${total_cost:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

def display_taxis(taxis):
    """Print a list of taxis neatly."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def choose_taxi(taxis):
    """Choose a taxi to drive."""
    number = int(input("Choose taxi: "))
    try:
        current_taxi = taxis[number]
        return current_taxi
    except IndexError:
        print("Invalid taxi choice")

def drive_taxi(current_taxi, total_cost):
    """Drive a taxi for one trip."""
    if current_taxi:
        distance = float(input("Drive how far? "))
        current_taxi.drive(distance)
        trip_cost = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
        total_cost += trip_cost
    else:
        print("You need to choose a taxi before you can drive")

    return total_cost

main()