import tkinter as tk
class ContentFrame(tk.Frame):
    def __init__(self,parent,content_list,label):
        main_color = '#171b16'
        text_color = '#2fc468'
        border_color = '#2fc468'
        super().__init__(parent,background=main_color)
        self.header_border=tk.Frame(self,background=border_color)
        self.header = tk.Label(self.header_border,
                                background=main_color, 
                                text=label, 
                                foreground=text_color,
                                font=("helvetica",16),
                                anchor='w',padx=10)
        self.header_border.place(x=10,y=10,width=420, height=50)
        self.header.pack(fill="both", expand=True, padx=1, pady=1)

        
        self.items={}
        for x in content_list:
            item=tk.Label(self,text=x,fg=text_color)
            self.items[x]=item
            #item.pack(anchor='w',fill=tk.X)
            
        
        

        