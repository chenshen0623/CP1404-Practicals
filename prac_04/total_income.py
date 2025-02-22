"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display the income report for the specified number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    display_report(incomes)


def display_report(incomes):
    """Display a report on cumulative income based on incomes."""
    print("\nIncome Report\n-------------")
    total = 0
    for i, income in enumerate(incomes, 1):
        total += income
        print(f"Month {i:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()
