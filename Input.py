from tkinter import *

root = Tk()

# Kullanıcının değer girmesini sağlayacak entry alanı.
e = Entry(root, width=50, borderwidth=2)
e.pack()
e.insert(0, "Enter your name")


def bFunc():
    hello = "Hello, " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

firstButton = Button(root, text="Enter", padx=20, pady = 20, command=bFunc)
firstButton.pack()


root.mainloop()