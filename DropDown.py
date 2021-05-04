from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Drop Down ")
root.geometry("400x400")

clickedVar = StringVar()
# Program başlatıldığında seçili olan değer
clickedVar.set("Money")
# Alt ögeler
days = ["Dollar",
        "Bitcoin",
        "Turkish Liras",
        "Euro",
        "Gold",
        "Silver"]

drop = OptionMenu(root, clickedVar, *days)
drop.pack()

def showSelection():
    myLabel= Label(root, text=clickedVar.get())
    myLabel.pack()

myButton = Button(root, text="Show", command=showSelection)
myButton.pack()



root.mainloop()
