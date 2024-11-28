"""
CP1404 Practical 9
Unreliable Car Class
Estimated: 15 minutes
Actual: 12 minutes
"""

from prac_09.car import Car
import random

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """Initialize an Unreliable Car instance, based on parent class Car"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car depending on the reliability of the car."""
        if random.randint(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        return 0