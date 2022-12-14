"""
Name: Python Budget Calculator
Author: Alessandro Allegranzi
Date: December, 2022
Description:
The python budget calculator is a simple CLI terminal application that allows the user 
to build a monthly budget to help them plan finances.
"""
from budget import Budget
from budget_utilities import is_valid_as_float, yes_or_no_valid, print_csv, confirm_category_percentages
import sys


FULL_PERCENTAGE = 100

def main():
    """
    Main function running the logic of the terminal application using the Budget class and utility
    function defined in budget_utilities
    """

    income = input('Please enter your monthly income: ')
    
    while not is_valid_as_float(income):
        income = input('There was a problem validating your income, please try again: ')

    standard_budget = input("Would you like to use a standard 50/30/20 budget?[y/n]: ")

    while not yes_or_no_valid(standard_budget):
        standard_budget = input("[y/n]?: ")

    if standard_budget == "y":
        budget = Budget(float(income))
    else:
        category_and_percentages = confirm_category_percentages()
        budget = Budget(float(income), category_and_percentages)
    
    print("Here is your budget plan")
    print(budget)

    print_csv_bool = input("Would you like generate a CSV file of your budget?[y/n]: ")

    while not yes_or_no_valid(print_csv_bool):
        print_csv_bool = input("[y/n]?: ")
    
    if print_csv_bool == "y":
        csv_file_name = input("Please enter desired name for CSV file: ")
        print_csv(budget, csv_file_name)

    print("Thank you for using the Python Budget Calculator")
    sys.exit()

if __name__ == '__main__':
    main()