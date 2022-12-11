"""
Name: Python Budget Calculator
Author: Alessandro Allegranzi
"""
from budget import Budget

def main():
    income  = input('Please enter your monthly income: ')
    budget = Budget(float(income))
    print("Your income is: ", budget.income)

if __name__ == '__main__':
    main()