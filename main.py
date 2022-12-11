"""
Name: Python Budget Calculator
Author: Alessandro Allegranzi
"""
from budget import Budget

def main():
    """Main function running the logic of the terminal application"""

    income = input('Please enter your monthly income: ')
    
    while not income_is_valid(income):
        income = input('There was a problem validating your income, please try again: ')

    standard_budget = input("Would you like to use a standard 50/30/20 budget?[y/n]: ")

    while not yes_or_no_valid(standard_budget):
        standard_budget = input("[y/n]?: ")

    if standard_budget == "y":
        budget = Budget(float(income))
        print("Your income is: ", budget.income)
        print("Your budget target is: ", budget.budget_map)
        print("Your calculated budget is: ", budget)


def income_is_valid(income: str) -> bool:
    """Validating user provided income"""
    try:
        income = float(income)
        return True
    except:
        return False

def yes_or_no_valid(selection: str) -> bool:
    """Validating user provided income"""
    if selection == "y" or selection == "n":
        return True
    else:
        return False

def print_csv():
    """Prints budget into a CSV file"""
    pass

if __name__ == '__main__':
    main()