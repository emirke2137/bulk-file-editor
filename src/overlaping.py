import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

# First frame
red_frame = tk.Frame(root, bg="red")
red_frame.place(x=100, y=100, width=250, height=200)

# Second frame
blue_frame = tk.Frame(root, bg="blue")
blue_frame.place(x=180, y=150, width=250, height=200)
def xd(name):
    print(name)
    red_frame.lift()

def xd1(name):
    print(name)
    blue_frame.lift()

# Bring clicked frame to front
red_frame.bind("<Button-1>", lambda e: xd("xdddd"))
blue_frame.bind("<Button-1>", lambda e: xd1("lol"))

root.mainloop()