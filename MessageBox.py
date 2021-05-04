from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Message Box")


def Popup():
    #                  ("Ekran bar ismi", " popup içeriği" )
    messagebox.showinfo("This is bar text", "Content")

def PopupQuestion():
    response = messagebox.askyesno("This is question popup", "Yes or No?")
    # Yes veya no seçime göre döndürür.
    if response == 1:
        Label(root, text="Yes").pack()
    else:
        Label(root, text="No").pack()


# MessageBox Türleri:
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

B = Button(root, text="Popup", command=Popup)
B.pack()
B2 = Button(root, text="Question Popup", command=PopupQuestion)
B2.pack()


root.mainloop()

