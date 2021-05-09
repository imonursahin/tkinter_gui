from tkinter import *

root = Tk()

def clickButton():
    global myLabel
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    e.delete(0, "end")
    myLabel.pack(pady=10)
    if myLabel.winfo_exists() == 1:
            print("x")
    myButton["state"] = DISABLED

def deleteElement():
    global myLabel
    myLabel.destroy()
    if myLabel.winfo_exists():
            print("x")
    myButton["state"] = NORMAL

e = Entry(root, width=80)
e.pack(padx=20, pady=20)

myButton = Button(root, text="Enter ur name", command=clickButton)
myButton.pack(pady=15)

deleteButton = Button(root, text="Delete name", command=deleteElement)
deleteButton.pack(pady=15)

root.mainloop()