"""The main file for intergrating analysis, interface, scraping files"""

import analysis as AN
import importing as IP
import sys
import argparse
from tkinter import *


class Interface:
    """The main interface"""

    def __init__(self,analyze):
        global root
        self.analyze = analyze
        root = Tk()
        root.title("Expense Tracker")
        mybutton1 = Button(root,text="Start", command = self.mybutton,width = 25, height = 5)
        mybutton1.pack()
        root.mainloop()
        


    def mybutton(self):
        """Create a button to let user interact with"""
        mybutton2 = Button(root,text="Company and Acount Type", command = self.mycompany,width = 25, height = 5)
        mybutton2.pack()
        mybutton3 = Button(root,text="Sum of The Total Amount Due", command = self.mytotal,width = 25, height = 5)
        mybutton3.pack()
        mybutton4 = Button(root,text="Sum of The Monthly Budget", command = self.mybudget,width = 25, height = 5)
        mybutton4.pack()

    def mycompany(self):
        mylabel = Label(root,text = self.analyze.company())
        mylabel.pack()
    
    def mytotal(self):
        mylabe2 = Label(root,text = self.analyze.sum_total_amount())
        mylabe2.pack()

    def mybudget(self):
        mylabe3 = Label(root,text = self.analyze.sum_monthly_budget())
        mylabe3.pack()


def parse_args(my_args_list):
    """Create a parse_args condition
    
    Args:
        my_args_list(list): sys input list
    
    Returns:
        args: the parser object createed
    """

    parser = argparse.ArgumentParser(description='Process the path')
    parser.add_argument('file_name',type = str, help='File name')
    args = parser.parse_args(my_args_list)
    return args

def main(path):
    my_data = IP.Import(path)
    my_analyze = AN.Analyze(my_data.examine_data())
    my_if = Interface(my_analyze)
    

if __name__ == "__main__":
    """The main function that integrating all the branch of the app"""

    new_args = parse_args(sys.argv[1:])
    main(sys.argv[1])


    