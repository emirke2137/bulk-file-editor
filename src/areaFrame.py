import tkinter as tk



class AreaFrame(tk.Frame):

    

    def __init__(self, parent):
        main_color ='#171b16'
        border_color='#41aba1'
        self.border = super().__init__(parent,bg=border_color)
        self.content=tk.Frame(self, bg=main_color)
        self.content.pack(fill="both", expand=True, padx=2,pady=2)