# tk25.pyw

import tkinter as tk
def get_text():
    print(txt.get('1.5','3.4'))

root = tk.Tk()
txt =tk.Text(width=30,height=5)
bt =tk.Button(text='Get Rowl Co16 to Row3 Co14', command=get_text )
[w.pack() for w in(txt,bt)]

root.mainloop()