# Source - https://stackoverflow.com/a/16639454
# Posted by kalgasnik, modified by community. See post 'Timeline' for change history
# Retrieved 2026-06-01, License - CC BY-SA 3.0

from tkinter import *
from tkinter.ttk import * 

root = Tk()

s = Style()
s.configure('My.TFrame', background='red')

mail1 = Frame(root, style='My.TFrame')
mail1.place(height=70, width=400, x=83, y=109)
mail1.config()
root.mainloop()
