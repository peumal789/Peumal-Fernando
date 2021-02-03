#P13 tk20
import tkinter as tk

root = tk.Tk
strvar = tk.StringVar()
en = tk.Entry(textvariable=strvar)
strvar.set('hello world')
en.pack()

root.mainloop()