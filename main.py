"""
Name: Python Budget Calculator
Author: Alessandro Allegranzi
Date: December, 2022
Description:
The python budget calculator is a simple CLI terminal application that allows the user 
to build a monthly budget to help them plan finances. Run the main.py file in your IDE,
or run `python3 main.py` in the terminal to start the application.
"""
from budget import Budget
from budget_utilities import is_valid_as_float, yes_or_no_valid, print_csv, confirm_category_percentages, WELCOME_MESSAGE
import sys

def main():
    """
    Main function running the logic of the terminal application using the Budget class and utility
    function defined in budget_utilities
    """
    
    # Starting with a welcome message and asking for income
    print(WELCOME_MESSAGE)
    income = input('Please enter your monthly income: ')
    
    while not is_valid_as_float(income):
        income = input('There was a problem validating your income, please try again: ')

    # Here we are confirming if he user would like specific budget percentages for our splits
    standard_budget = input("Would you like to use a standard 50/30/20 budget?[y/n]: ")

    while not yes_or_no_valid(standard_budget):
        standard_budget = input("[y/n]?: ")

    # Creating a budget for the user, and printing the budget for them to see
    if standard_budget == "y":
        budget = Budget(float(income))
    else:
        category_and_percentages = confirm_category_percentages()
        budget = Budget(float(income), category_and_percentages)
    
    print("Here is your budget plan")
    print(budget)

    # As a little bit of fun, if the user wants we can look over their budget and offer very general, safe
    # advice for improvement, like trying to save more. 
    evaluate_budget_bool = input("Would you like us to evaluate your budget? Please bear in mind we are not liensed fiancial planners, this is very general advice [y/n]: ")

    while not yes_or_no_valid(evaluate_budget_bool):
        evaluate_budget_bool= input("[y/n]?: ")
    
    if evaluate_budget_bool == "y":
        print(" ".join(budget.evaluate_budget()))

    # Giving the option to reallocate budget cateogires if the user desires 
    recalculate_budget = input("Would you like re-allocate percentages to your budget categories?[y/n]: ")

    while not yes_or_no_valid(recalculate_budget):
        recalculate_budget = input("[y/n]?: ")

    if recalculate_budget == "y":
        category_and_percentages = confirm_category_percentages()
        budget.amend_budget_calculations(category_and_percentages)
        print("Here is your revised budget plan")
        print(budget)

    # Giving the option to save the budget to a csv file
    print_csv_bool = input("Would you like generate a CSV file of your budget?[y/n]: ")

    while not yes_or_no_valid(print_csv_bool):
        print_csv_bool = input("[y/n]?: ")
    
    if print_csv_bool == "y":
        csv_file_name = input("Please enter desired name for CSV file: ")
        print_csv(budget, csv_file_name)

    # Exiting the App
    print("Thank you for using the Python Budget Calculator")
    sys.exit()

if __name__ == '__main__':
    main()