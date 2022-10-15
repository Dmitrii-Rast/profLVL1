import tkinter as tk
class Call:
    def __init__(self,n):
        self.n=n
    def call_window(self):
        self.window=tk.Tk()
        self.window.geometry ("800x600")
        self.window.mainloop()
call=Call(0)
call.call_window()