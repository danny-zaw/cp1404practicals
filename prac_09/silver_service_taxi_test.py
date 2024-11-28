"""
CP1404 Practical 9
Test Code for Silver Service Taxi
"""

from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Test code to use Silver Service Taxi class."""
    my_fancy_taxi = SilverServiceTaxi("Hummer", 200, 2)
    my_fancy_taxi.drive(18)
    # assert my_fancy_taxi.get_fare() == 48.87 # Old assert without rounding
    assert my_fancy_taxi.get_fare() == 48.80
    print(f"Expected: $48.80, Got: ${my_fancy_taxi.get_fare():.2f}")
    print(my_fancy_taxi)

    my_fancier_taxi = SilverServiceTaxi("Porsche", 300, 5)
    my_fancier_taxi.drive(20)
    assert my_fancier_taxi.get_fare() == 127.50
    print(f"Expected: $127.50, Got: ${my_fancier_taxi.get_fare():.2f}")
    print(my_fancier_taxi)

main()