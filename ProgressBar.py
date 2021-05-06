from tkinter import *
from tkinter import ttk

root = Tk()

Button(text="Click For ProgressBar", command=lambda: generate_numbers()).grid()

def generate_numbers():
    progress_bar = ttk.Progressbar(orient=HORIZONTAL, length=500) # Progress bar'ın uzunluğu
    progress_bar.grid() # Progress bar'ı ekranda gösterme
    
    progress_bar["maximum"] = len(range(1,10001)) # Progress bar'ın ilerleme sayısı
    
    progress_count = 0
    for value in range(1,10001):
        progress_count += 1
        progress_bar["value"] = progress_count 
        progress_bar.update() # İlerleme çubuğunun rengini güncelleme
        
root.mainloop()