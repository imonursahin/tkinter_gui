from tkinter import *

root = Tk()

Label(text="LISTBOX").grid()

# Boş listbox oluşturma
listbox_obj = Listbox()
listbox_obj.grid() 

# İlk elemanı ekleme
listbox_obj.insert(END, "first")

# İkinci elemanı ekleme
listbox_obj.insert(END, "second") 

# Üçüncü elemanı ekleme
listbox_obj.insert(END, "third") 

root.mainloop()