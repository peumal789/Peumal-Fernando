# P16 tk24.py

import tkinter as tk
def get_selpoint():
    sel_start = txt.index('sel.first')
    sel_end =txt.index('sel.first')
    lb['text'] = 'start: {} end: {}'.format(sel_start,sel_end)

root = tk.Tk()
lb = tk.Label()
txt =tk.Text(width=30, height=5)
bt =tk.Button(text='Selected Area', command=get_selpoint)
[w.pack() for w in (lb, txt ,bt)]

root.mainloop()
