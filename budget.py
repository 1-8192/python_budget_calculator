class Budget(object):
    """
    A class to represent someone's monthly budget.

    ...

    Attributes
    ----------
    income: float
        peron's total income
    budget_map: dict
        Person's budget category and percentage of total budget.
    calculated_budget_map: dict
        Persons's budget category and calculated monthly allowance.
    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    """
    
    # Class variable that allows us to access budget categories. Using a tuple since these should not change
    # by user or code mishap
    budget_categories = ("necessities", "savings", "discretionary")

    def __init__(self, income: float, budget_map: dict = {budget_categories[0]: 50, budget_categories[1]: 20, budget_categories[2]: 30}):
        """
        The constructor for Budget class.
  
        Parameters:
           income (float): A person's total monthly income
           budget_map (dict):  A map of budget category to percentage of total budget.

        """
        self.income = income
        self.budget_map = budget_map
        self.calculated_budget_map = {}
        self.__calculate_budget()
    
    def __calculate_budget(self) -> None:
        """
        Calculates actual totals for monthly budgets based on preset percentages
  
        Parameters:
           self (Budget): class instance
        
        Return:
            None
        """
        for i in self.budget_map.keys():
            self.calculated_budget_map[i] = (self.budget_map[i] / 100) * self.income
    
    def format_for_csv(self) -> tuple:
        """
        returns a tuple ready to be saved into a CSV file with budget information.
  
        Parameters:
           self (Budget): class instance
        
        Return:
            tuple with 2 elements, each a row to be saved to a CSV file
        """
        csv_first_row = ["Your budget"]
        csv_second_row = []
        csv_third_row = []
        csv_fourth_row =["Total income", self.income]
        for i in self.calculated_budget_map.keys():
            csv_second_row.append(i)
            csv_third_row.append(self.calculated_budget_map[i])
        
        return (csv_first_row, csv_second_row, csv_third_row, csv_fourth_row)
    
    def evaluate_budget(self) -> str:
        """
        returns a string summary of recommendations based on budget plan.
  
        Parameters:
           self (Budget): class instance
        
        Return:
            string
        """
        pass

    def __repr__(self) -> str:
        """
        Repr overwrite for the budget class. Showing insight into Budget class instance.
  
        Parameters:
           self (Budget): class instance
        
        Return:
            string
        """
        return "Budget: \n" + "Budget Map: " + str(self.budget_map) + "\n" + "Calculated Budget: " + str(self.calculated_budget_map)

    def __str__(self):
        """
        str overwrite for the budget class. Showing formatted information on the Budget instance
        for printing.
  
        Parameters:
           self (Budget): class instance
        
        Return:
            string
        """
        return "Budget: \n" + "{:<2}  {:<2}  {:<2}\n".format(Budget.budget_categories[0], Budget.budget_categories[1], Budget.budget_categories[2]) + "{:,.2f}       {:,.2f}   {:,.2f}\n".format(
            self.calculated_budget_map[Budget.budget_categories[0]], self.calculated_budget_map[Budget.budget_categories[1]], self.calculated_budget_map[Budget.budget_categories[2]]) + "Total Income: {:,.2f}".format(
            self.income  
            )

if __name__ == '__main__':
    """ Unit testing some class methods below"""
