"""
Utility functions for the Python Budget Calculator
"""
from budget import Budget
import csv

def is_valid_as_float(income: str) -> bool:
    """Validating user provided income"""

    # Float conversion here could cause a ValueError, so catching that exception
    try:
        income = float(income)
        return True
    except ValueError:
        return False

def yes_or_no_valid(selection: str) -> bool:
    """Validating user provided income"""
    if selection == "y" or selection == "n":
        return True
    else:
        return False

def print_csv(budget: Budget, file_name: str) -> None:
    """Prints budget into a CSV file"""
    file = open(file_name + '.csv', 'w')
    content = budget.format_for_csv()
    writer = csv.writer(file)
    for i in range(len(content)):
        writer.writerow(content[i])
    file.close()

def confirm_category_percentages() -> dict:
    """Confirms percentages user wants for budget categories"""
    budget_map_dict = {}

    # Wrapping values() method in list since it returns a view.
    while sum(list(budget_map_dict.values())) != 100:
        print("Please make sure you enter values that add to 100%")
        for i in Budget.budget_categories:
            percent = input('Please enter the percetange of income you would like to spend on ' + i + ': ')
    
            while not is_valid_as_float(percent):
                percent = input('There was a problem validating your entry, please entered desired percentage: ')
        
            budget_map_dict[i] = float(percent)
    
    return budget_map_dict