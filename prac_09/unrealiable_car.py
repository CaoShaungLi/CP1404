import random

from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that indicates reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an Unreliable Car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with reliability"""
        return f"{super().__str__()}, reliability = {self.reliability}"

    def drive(self, distance):
        """Drive like parent car but only if the random number is greater than reliability"""
        if random.randint(0, 100) < self.reliability:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self._odometer += distance
            return distance
        else:
            return 0
