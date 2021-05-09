from tkinter import *

root = Tk()
root.title("Class")

class info:        
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        self.myButton = Button(master, text="Click", command= self.clicker)
        self.myButton.pack(pady=20)

    def clicker(self):
        print("this is class")

classRun = info(root)



root.mainloop()