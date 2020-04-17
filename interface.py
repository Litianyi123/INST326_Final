"""The interface used by user"""

from tkinter import *

root = Tk()
root.title("Expense Tracker")

def myClick():
    """Create a button to let user interact with"""

    mylabel = Label(root,text = "Success")
    mylabel.pack()

def reload():
    """Reload the interface to clear the information"""
    root.update()

mybutton1 = Button(root,text="Click to start!", command = myClick,width = 25, height = 5)
mybutton1.pack()

mybutton2 = Button(root,text="Reload", command = reload,width = 25, height = 5)
mybutton2.pack()

root.mainloop()