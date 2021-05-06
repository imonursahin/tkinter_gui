from tkinter import *

root = Tk()

firstLabel1 = Label(root, text="Hello")
secondLabel2 = Label(root, text="My name is Onur")
thirdLabel3 = Label(root, text="Read my blogs: onursahin.net ")

# Grid birbirleriyle kesişen yatay, dikey ya da açısal çizgilerin oluşturduğu yapılar
# 0'dan başlayarak numaralandırılmıştır

firstLabel1.grid(row=0, column=0)
secondLabel2.grid(row=1, column=5)
thirdLabel3.grid(row=1,column=1)


root.mainloop()



