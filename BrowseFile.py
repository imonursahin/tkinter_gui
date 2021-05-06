from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("600x300")

# Yüklenecek dosyanın adının görüneceği alan
Text_Field = Text(height=1, width=40)
Text_Field.insert(INSERT, "")
Text_Field.grid(row=0, column=0)

# Buton oluşturma
# Bu buton dosyayı seçmemize yardımcı olacak butondur.
Button(text="Browse File", command=lambda: browse_file(Text_Field)).grid(row=0, column=1)

# Dosyayı seçme fonksiyonu
def browse_file(Text_Field):
    file = filedialog.askopenfilename(initialdir = "/") #C: sürücüsünden açılacaktır. Dosyayı seçtikten sonra dosya dizini ekranda görüntülenecektir.
    file = file.replace("/", "\\", file.count('/')) 
    Text_Field.delete("1.0", END) 
    Text_Field.insert(INSERT, file)
    
# Yüklene dosyanın bilgilerini gösterme
Button(text="show file name", command=lambda: extract_file_name(Text_Field.get("1.0", "end-1c"))).grid()

# Dosya Adını görüntülemek için fonksiyon tanımlama
def extract_file_name(file_name):
    print(file_name)
    
root.mainloop()