import tkinter as tk


class SwitchFrame(tk.Frame):
    def __init__(self, parent,order,name,pair):
        self.pair=pair
        self.order=order
        self.parent = parent
        main_color = '#171b16'
        border_color = '#41aba1'
        self.border = tk.Frame(parent,bg=border_color)
        super().__init__(self.border,bg=main_color)
        self.name= tk.Label(self, text=name,bg=main_color,fg=border_color,font=("helvetica",16,"bold"))
        self.name.pack(pady=6)
        self.bind("<Button-1>",lambda e: self.clicked())
        self.name.bind("<Button-1>",lambda e: self.clicked())
        
        

    def place(self):
        w=120
        startpos=300
        overlap=2
        self.border.place(  anchor='sw',
                            rely=1,
                            x=2+self.order*(w+2),
                            y=-(startpos-overlap),
                            height=40,
                            width=w+2)
        super().place(x=1,y=1,width=w,height=40)
        self.border.lift()
        self.lift()
        


    def clicked(self):
        self.pair.clicked()

        self.border.place(height=46)
        super().place(height=46)
        self.border.lift()
        super().lift()
        
        


  


    