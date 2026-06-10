import tkinter as tk



class OptionsFrame(tk.Frame):

    

    def __init__(self, parent,order):
        main_color = '#171b16'
        border_color = '#41aba1'
        self.border = super().__init__(parent,bg=border_color)

        self.content = tk.Frame(self, bg=main_color)
        self.content.place(x=1,y=50,relwidth=1,width=-2,relheight=1,height=-52,anchor="nw")
        
        #self.fake_background = tk.Frame(self, bg=main_color)
        #self.fake_background.place(x=1,y=0,relwidth=1,width=-2,height=48)

