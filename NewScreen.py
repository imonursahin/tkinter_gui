from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Open New Screen")


def open():
    top = Toplevel()
    buttonQuit = Button(top, text="Close Screen", command=top.destroy)
    buttonQuit.pack()

B = Button(root, text="New Screen", command=open)
B.pack()

mainloop()