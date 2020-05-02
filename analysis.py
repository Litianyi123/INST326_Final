"""Analysis the data"""

import openpyxl
import importing as IP
import sys 

class Analyze:
    """Analyze the data 
    
    Attributes:
        data(dictionary): the dictionary contains all the data
    
    Args:
        data(dictionary): the dictionary contains all the data
    """

    def __init__(self,data):
        """Initial the analyze instance
    
        Args:
        data(dictionary): the dictionary contains all the data
        
        """

        self.data = data 
    
    def company(self):
        """Print all the companies and the account types in the expense tracker
        
        Returns:
            result(list): a list contain all the companies information

        """

        x = 0
        my_company = self.data["Company Name"]
        my_account = self.data["Account"]
        result = []
        for i in my_company:
            my_string = i + " -- " + my_account[x]
            x += 1
            result.append(my_string)

        return result
    def sum_total_amount(self):
        """Sum the total amount due
        
        Returns:
            my_sum(Int): the sum of all the total amount 

        """

        my_sumtotal = 0
        
        total_amount = self.data['Total Amount Due']
        
        for i in total_amount:
            my_sumtotal = my_sumtotal + float(i)

        return my_sumtotal

    def sum_monthly_budget(self):
        """Sum the monthly budget
        
        Returns:
            my_sumbud(Int): the sum of all the total amount 

        """

        my_sumbud = 0
        
        month_bud = self.data['Monthly Budget']
        for i in month_bud:
            my_sumbud = my_sumbud + float(i)

        return my_sumbud

if __name__ == "__main__":
    """Import data and do the anyalze""" 

    my_data = IP.Import("expensetracker.xlsx")
    my_analyze = Analyze(my_data.examine_data())
    print(my_analyze.company())
    print(my_analyze.sum_total_amount())
    print(my_analyze.sum_monthly_budget())
