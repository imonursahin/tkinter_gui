# Kütüphaneyi yüklüyoruz.
from tkinter import *
# Tkinterda her şey widgettır.
# Pencereyi TK sınıfına atıyoruz.
root = Tk()

# Pencereye metin eklemek için Label sınıfı kullanılır.
firstLabel = Label(root, text="Tkinter GUI")
#Labeli ekranda göstermek için kullanılır.
firstLabel.pack()

# .pack() widgeti ekrana yazdırır.
root.mainloop()

# Kodun sınırsız döngü olarak çalışması için mainloop() yazıyoruz.
