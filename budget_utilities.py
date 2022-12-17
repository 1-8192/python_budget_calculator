"""
Utility constants and functions for the Python Budget Calculator
"""
from budget import Budget
import csv

FULL_PERCENTAGE = 100

WELCOME_MESSAGE = """
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Welcome to the Python Budget Calculator! This is a simple CLI    '
' App to help you plan a monthly budget. Please answer the prompts '
' to get started.                                                  '
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""

def is_valid_as_float(income: str) -> bool:
    """
        Validating user provided income
  
        Parameters:
           income (str): user provided income. str since it comes from input function
        
        Return:
            Bool
    """
    # Float conversion here could cause a ValueError, so catching that exception
    try:
        income = float(income)
        return True
    except ValueError:
        return False

def yes_or_no_valid(selection: str) -> bool:
    """
        Validating whether a user selected yer or no option
  
        Parameters:
           selection (str): user provided selection
        
        Return:
            Bool
    """
    if selection == "y" or selection == "n":
        return True
    else:
        return False

def print_csv(budget: Budget, file_name: str) -> None:
    """"
        Prints budget into a CSV file
  
        Parameters:
           budget (Budget class): user's budget
           file_name (str): desired name for file
        Return:
            None
    """
    file = open(file_name + '.csv', 'w')
    content = budget.format_for_csv()
    try:
        writer = csv.writer(file)
        for i in range(len(content)):
            writer.writerow(content[i])
    except Exception as e:
        # A few things could go wrong here, so generally catching any exception
        print("We're sorry, something went wrong creating the CSV file: ", e)
    else:
        print("We printed your results to a CSV file.")
    finally:
        # Always making sure we close the file
        file.close()

def confirm_category_percentages() -> dict:
    """"
        Confirms and validates user selected percentages for
        budget categories.
  
        Parameters:
           budget (Budget class): user's budget
           file_name (str): desired name for file
        Return:
            dict
    """
    budget_map_dict = {}

    # Wrapping values() method in list since it returns a view.
    while sum(list(budget_map_dict.values())) != FULL_PERCENTAGE:
        print("Please make sure you enter values that add to 100%")
        for i in Budget.budget_categories:
            percent = input('Please enter the percetange of income you would like to spend on ' + i + ': ')
    
            while not is_valid_as_float(percent):
                percent = input('There was a problem validating your entry, please entered desired percentage: ')
        
            budget_map_dict[i] = float(percent)
    
    return budget_map_dict

if __name__ == '__main__':
    """ 
    Unit testing some functions. Some of the functions require user interaction or file
    printing, so we're not boothering setting up tests for those since we're not using
    any dedicated testing libraries that might be better for it. 
    """

    """Testing is_valid_as_float function"""
    assert True == is_valid_as_float('300')
    assert False == is_valid_as_float('%^STAG')

    """Testing yes_or_no_valid function"""
    assert True == yes_or_no_valid("y")
    assert False == yes_or_no_valid("What's up?")