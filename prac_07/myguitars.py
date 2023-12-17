"""My Guitars client program"""
from prac_07.guitar import Guitar

FILE_NAME = 'guitars.csv'


def main():
    """Display existing guitars and prompt user for new guitar to add and display."""
    guitars = []
    in_file = open(FILE_NAME, 'r')
    for line in in_file:
        information = line.strip().split(',')
        guitar = Guitar(information[0], information[1], information[2])
        guitars.append(guitar)
    in_file.close()

    for guitar in guitars:
        print(guitar)
    print()
    guitars.sort()
    for guitar in guitars:
        print(guitar)

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        out_file = open(FILE_NAME, 'a')
        new_guitar = f"{name},{year},{cost}"
        print(new_guitar, file=out_file)
        out_file.close()
        name = input("Name: ")
    # for guitar in guitars:
    #     print(guitar)


main()
