"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of numbers_of_month."""
    incomes = []
    numbers_of_month = int(input("How many numbers_of_month? "))

    for month in range(1, numbers_of_month + 1):
        income = float(input(f"Enter income for month {str(month)}: "))
        # income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    print_report(incomes, numbers_of_month)


def print_report(incomes, numbers_of_month):
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, 1):
        # income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")
        # print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
