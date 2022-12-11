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
    
    def calculate_budget(self):
        for i in self.budget_map.keys():
            self.calculated_budget_map[i] = self.budget_map[i] / 100 * self.income

if __name__ == '__main__':
    pass