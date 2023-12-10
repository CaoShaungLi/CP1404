"""Playing the Guitar - Guitars client program """

from prac_06.guitar import Guitar


def main():
    """Get guitars information and display name, year, cost and vintage or not"""
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            guitars.append(Guitar(name, year, cost))
            print(f"{Guitar(name, year, cost)} is added to collection.")
        except ValueError:
            print("Invalid input")
        name = input("Name: ")

    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("...snip...")
    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = "(vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("There are no guitars yet.")


main()
