"""The interface used by user"""

from tkinter import *


class Interface:
    """The main interface"""

    def __init__(self):
        global root
        root = Tk()
        root.title("Expense Tracker")
        mybutton1 = Button(root,text="Click to start!", command = self.mybutton,width = 25, height = 5)
        mybutton1.pack()
        root.mainloop()


    def mybutton(self):
        """Create a button to let user interact with"""
        mybutton2 = Button(root,text="Company and Acount type", command = self.mycompany,width = 25, height = 5)
        mybutton2.pack()
     

    def mycompany(self):
        mylabel = Label(root,text = "Your Daily Payment Is: ")
        mylabel.pack()
        

if __name__ == '__main__': 
    myInterface = Interface()
    
