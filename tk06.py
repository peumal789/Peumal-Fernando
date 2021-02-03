import tkinter as tk

def action_btn_press():
        print('Button was pressed!')

import tkinter as tk
root = tk.Tk()
root.title('Widget creation')
root.geometry("350x150")
lb =tk.Label(text='LABEL-1')
bt = tk.Button(text='BUTTON-1')
bt = tk.Button(text='BUTTON-2')
bt = tk.Button(text='BUTTON-3',command=action_btn_press)
lb.pack()
bt.pack()
root.mainloop()