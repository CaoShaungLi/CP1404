"""Guitar class program"""

CURRENT_YEAR = 2023
VINTAGE_MINIMUM_YEAR = 50


class Guitar:
    """Represent data of a guitar"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string about guitar"""
        return f"{self.name} ({self.year} : ${self.cost})"

    def get_age(self):
        """Calculate age of the guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage or not"""
        return self.get_age() >= VINTAGE_MINIMUM_YEAR
