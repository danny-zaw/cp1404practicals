"""
CP1404 Practical 9
Test Code for Unreliable Car Class
Estimated: 15 minutes
Actual: 10 minutes
"""

from prac_09.unreliable_car import UnreliableCar

def main():
    """Test code to use Unreliable Car Class"""
    my_unreliable_car = UnreliableCar("Corolla", 100, 50)
    my_unreliable_car.drive(60)

    print(my_unreliable_car)

main()