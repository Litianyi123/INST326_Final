"""Analysis the data"""
import scraping

class transaction:
    """This class show each transaction identity
    
    Attributes: 
        user(string): the user name
        date(tuple of integer): date of the transaction
        cash(int): the cash  paid or received 
    """

    def __init__(self, user,date,cash):
        self.user = user
        self.date = date
        self.cash = cash
    
    def balance(self):
        """Show the current balance"""

    def money_lose(self,date):
        """The money losed in the time period"""
    
    def money_earned(self,date):
        """The money earned in the time period"""

    def daily_expense(self,date):
        """Show the daily expense by date"""

    def monthly_expense(self,date):
        """Show the monthly expense by date"""

    
if __name__ == "__main__":
    """Scraping the data and do the analysis"""
    # first scrpaing the data by using module in scraping
    pass