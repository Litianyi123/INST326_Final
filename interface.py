"""The interface used by user"""

from tkinter import *


class Interface:
    """The main interface"""

    def __init__(self):
        global root
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
        mylabel = Label(root,text = "Companies and account types are: ")
        mylabel.pack()
    
    def mytotal(self):
        mylabe2 = Label(root,text = "Sum of the total amount is: ")
        mylabe2.pack()

    def mybudget(self):
        mylabe3 = Label(root,text = "Sum of monthly budget is: ")
        mylabe3.pack()


if __name__ == '__main__': 
    myInterface = Interface()
    
