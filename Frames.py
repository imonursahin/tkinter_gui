from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Frames")

frame = LabelFrame(root, text="This is frame", padx=5, pady=5)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Exit Button", command=root.quit)
b2 = Button(frame, text="Button")

b.grid(row=0, column=0)
b2.grid(row=1, column=1 )



root.mainloop()