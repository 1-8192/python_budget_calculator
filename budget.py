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
        Calculates actual totals for monthly budgets based on preset percentages. Private method called upon initialization
  
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
            tuple with 4 elements, each a row to be saved to a CSV file
        """
        csv_first_row = ["Your budget"]
        csv_second_row = []
        csv_third_row = []
        csv_fourth_row =["Total income", self.income]
        for i in self.calculated_budget_map.keys():
            csv_second_row.append(i)
            csv_third_row.append(self.calculated_budget_map[i])
        
        return (csv_first_row, csv_second_row, csv_third_row, csv_fourth_row)
    
    def evaluate_budget(self) -> set:
        """
        returns a set of strings with recommendations based on budget plan.
  
        Parameters:
           self (Budget): class instance
        
        Return:
            set of str
        """
        advice_set = set()
        
        if self.budget_map[Budget.budget_categories[1]] >= 20 and self.budget_map[Budget.budget_categories[2]] <= 30:
            advice_set.add("Your overall budget looks pretty good.")
        if self.budget_map[Budget.budget_categories[1]] < 20:
            advice_set.add("You may want to consider setting aside a larger portion of your income to savings.")
        if self.budget_map[Budget.budget_categories[2]] > 30:
            advice_set.add("You may want to consider spending less each month on non-essential things.")
        if self.budget_map[Budget.budget_categories[0]] > 50:
            advice_set.add("Your monthly costs for rent/utilities etc. may be slightly high for your income level. Consider downsizing.")
        
        if len(advice_set) == 0:
            advice_set.add("We aren't really able to advise you, sorry.")
        
        return advice_set

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

    """Testing that calculate_budget() work correctly on initialization """
    # Case 1 = using default budget plan
    expected_budget_map = {
        Budget.budget_categories[0]: 500.0,
        Budget.budget_categories[1]: 200.0,
        Budget.budget_categories[2]: 300.0,
        }
    budget = Budget(1000)
    assert expected_budget_map == budget.calculated_budget_map, "Did not generate expected budget breakdown, got: {}".format(budget.calculated_budget_map)

    # Case 2 = using custom budget plan percentages
    budget_map = {
        Budget.budget_categories[0]: 15,
        Budget.budget_categories[1]: 30,
        Budget.budget_categories[2]: 65,
    }
    expected_budget_map = {
        Budget.budget_categories[0]: 150.0,
        Budget.budget_categories[1]: 300.0,
        Budget.budget_categories[2]: 650.0,
        }
    budget = Budget(1000, budget_map)
    assert expected_budget_map == budget.calculated_budget_map, "Did not generate expected budget breakdown, got: {}".format(budget.calculated_budget_map)

    """Testing the format_for_csv() method"""
    budget = Budget(1000)
    csv_tuple = budget.format_for_csv()
    expected_tuple = (
        ["Your budget"],
        ["necessities", "savings", "discretionary"],
        [500.0, 200.0, 300.0],
        ["Total income", 1000]
    )
    assert expected_tuple == csv_tuple, "Did not get expcted csv rows, got: {}".format(csv_tuple)

    """Testing the evaluate_budget() method"""
    # Case 1 = using default budget percentages
    budget = Budget(1000)
    evaluated_budget = budget.evaluate_budget()
    expected_set = {"Your overall budget looks pretty good."}
    assert expected_set == evaluated_budget, "Did not get expcted advice, got: {}".format(evaluated_budget)

    # Case 2 = using different percentages
    budget_map = {
        Budget.budget_categories[0]: 60,
        Budget.budget_categories[1]: 5,
        Budget.budget_categories[2]: 35,
    }
    budget = Budget(1000, budget_map)
    evaluated_budget = budget.evaluate_budget()
    expected_set = {
        "You may want to consider setting aside a larger portion of your income to savings.",
        "You may want to consider spending less each month on non-essential things.",
        "Your monthly costs for rent/utilities etc. may be slightly high for your income level. Consider downsizing."
        }
    assert expected_set == evaluated_budget, "Did not get expcted advice, got: {}".format(evaluated_budget)