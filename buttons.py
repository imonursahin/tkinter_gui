from tkinter import *

root = Tk()
# Butona tıklanıldığında gerçekleştireceği işlev için fonksiyon oluşturulur.

def buttonClick():
    firstLabel = Label(root, text="Clicked button!")
    firstLabel.pack()

# Fonksiyonun çalışması için command parametresine fonksiyonun adı yazılır.

firstButton = Button(root, text="CLick Me", padx=50, pady = 50, command=buttonClick, fg="blue", bg="gold")
firstButton.pack()

# Butonu devre dışı bırakmak için state=DISABLED
# fg ve bg buton renkleri için kullanılır.




root.mainloop()

