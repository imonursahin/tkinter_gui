import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Combobox')


def moneys_changed(event):
    msg = f'Selected:  {moneys_cb.get()}'
    showinfo(title='Results', message=msg)

moneys = ('Bitcoin', 'Dollars', 'TRY', 'Euro', 'Gold', 'Silver')

label = ttk.Label(text="Select")
label.pack(fill='x', padx=5, pady=5)

# combobox oluşturma
selected_moneys = tk.StringVar()

moneys_cb = ttk.Combobox(root, textvariable=selected_moneys)
moneys_cb['values'] = moneys
moneys_cb['state'] = 'readonly' 
moneys_cb.pack(fill='x', padx=5, pady=5)

moneys_cb.bind('<<ComboboxSelected>>', moneys_changed)

root.mainloop()