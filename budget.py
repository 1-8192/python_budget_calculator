class Budget(object):
    """
    A class to represent someone's monthly budget.

    ...

    Attributes
    ----------
    income: float
        peron's total income 
    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    """
    def __init__(self, income: float, budget_map: dict = {"necessities": 50, "savings": 20, "discretionary": 30}):
        """
        The constructor for Budget class.
  
        Parameters:
           income (float): A person's total monthly income

        """
        self.income = income
        self.budget_map = budget_map
        self.calculated_budget_map = {}
        self.calculate_budget()
    
    def calculate_budget(self) -> None:
        """
        Calcualtes actual totals for monthly budgets based on preset percentages
  
        Parameters:
           self (Budget): class instance
        
        Return:
            None
        """
        for i in self.budget_map.keys():
            self.calculated_budget_map[i] = self.budget_map[i] / 100 * self.income

    def __repr__(self) -> str:
        """
        Repr overwrite for the budget class
  
        Parameters:
           self (Budget): class instance
        
        Return:
            string
        """
        category_list = list(self.budget_map.keys())
        return "Budget: \n" + "{:<2}  {:<2}  {:<2}\n".format(category_list[0], category_list[1], category_list[2]) + "{:,2}  {:,2}  {:,2}\n".format(self.calculated_budget_map['necessities'], self.calculated_budget_map['savings'], self.calculated_budget_map['discretionary'])

    def __str__(self):
        """
        Repr overwrite for the budget class
  
        Parameters:
           self (Budget): class instance
        
        Return:
            string
        """
        category_list = list(self.budget_map.keys())
        print(category_list)
        return "Budget: \n" + "{:<2}  {:<2}  {:<2}\n".format(category_list[0], category_list[1], category_list[2]) + "{:<2}  {:<2}  {:<2}\n".format(self.calculated_budget_map['necessities'], self.calculated_budget_map['savings'], self.calculated_budget_map['discretionary'])

if __name__ == '__main__':
    pass