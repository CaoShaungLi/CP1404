"""Guitar Testing program"""
from prac_06.guitar import Guitar


def test():
    """Test the guitar class program"""
    name = "Gibson L-5 CES"
    year = 1922
    guitar = Guitar(name, year)
    another_guitar = Guitar("Another Guitar", 2013)
    print(f"{guitar.name} get_age() - Expected 101. Got {guitar.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 10. Got {another_guitar.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")


test()
