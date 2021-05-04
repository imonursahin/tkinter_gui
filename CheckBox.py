from tkinter import *

root = Tk()
root.title("checkbox")
root.geometry("400x400")

var = StringVar()

# Varsayılan değeri 0 veya 1 'dir. onvalue - offvalue ile belirli değeri yazdırır.

c = Checkbutton(root, text="check this box", variable=var, offvalue="off", onvalue="on")
c.deselect()
c.pack()


def showResult():
    myLabel = Label(root, text=var.get())
    myLabel.pack()

myButton = Button(root, text="show", command= showResult )
myButton.pack()



root.mainloop()