"""Analysis the data"""

import importing as IP
import sys 

class Analyze:
    
    def __init__(self,data):
        self.data = data 
    
if __name__ == "__main__":
    my_data = IP.Import("expensetracker.xlsx")
    print(my_data.examine_data())
    my_analyze = Analyze(my_data.examine_data())
    