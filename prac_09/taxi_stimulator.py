"""Taxi Stimulator"""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Stimulate a taxi and calculate fare."""
    total_fare = 0
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive")
    print(MENU)
    choice = input(">>>").lower()
    while choice != "q":
        if choice == "c":
            print("Taxi available:")
            display_taxi(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = validate_taxi_choice(current_taxi, taxi_choice, taxis)
        elif choice == "d":
            if current_taxi:
                current_taxi.get_fare()
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)
                fare = current_taxi.get_fare()
                total_fare += fare
                print(f"Your {current_taxi.name} trip cost you ${total_fare:.2f}")
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_fare:.2f}")
        print(MENU)
        choice = input(">>>").lower()
    print(f"Total trip cost: ${total_fare:.2f}")
    print("Taxis are now:")
    display_taxi(taxis)


def validate_taxi_choice(current_taxi, taxi_choice, taxis):
    """Validate taxi number chosen by the user."""
    try:
        current_taxi = taxis[taxi_choice]
    except IndexError:
        print("Invalid taxi choice")
    return current_taxi


def display_taxi(taxis):
    """Display taxis to users."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
