from tkinter import Tk, Label, font
from clock import Clock


root = Tk()
root.resizable(False, False)

Clock(root)

root.mainloop()