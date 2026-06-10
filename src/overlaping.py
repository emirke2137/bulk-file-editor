import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

# First frame
red_frame = tk.Frame(root, bg="red")
red_frame.place(x=100, y=100, width=250, height=200)

# Second frame
blue_frame = tk.Frame(root, bg="blue")
blue_frame.place(x=180, y=150, width=250, height=200)

# Bring clicked frame to front
red_frame.bind("<Button-1>", lambda e: red_frame.lift())
blue_frame.bind("<Button-1>", lambda e: blue_frame.lift())

root.mainloop()