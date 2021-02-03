import tkinter as tk
class Application(tk.Frame):

    def __init__(self,master=None):

        super().__init__(master)
        master.title('Get Text Box data')
        master.geometry('350x150')
        self.pack()
        self.create_widget()

    def create_widget(self):
        self.lb = tk.Label(self)
        self.lb ['text'] ='Labe1(appl)'
        self.lb.pack(side = 'top')
        self.en = tk.Entry(self)
        self.en.pack()
        self.en.focus_set()
        self.bt = tk.Button(self,text ='Button',command=self.print_txtval)
        self.bt.pack(side='bottom')
