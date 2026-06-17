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
        container=tk.Frame(self, background=main_color)
        container.place(x=20,y=70,relwidth=1, relheight=1,height=-300, width=-30)
        self.list = tk.Listbox(container,background=main_color,bd=0,relief="flat",highlightthickness=0)
        self.scroll = tk.Scrollbar(container, orient="vertical", command=self.list.yview)
        self.scroll.pack(side="right",fill='y')

        #------------------------------------
        #custom scroll command to show scrollball only when needed
        def auto_scrollbar(first, last):
            first = float(first)
            last = float(last)
            print(first,last)
            if first <= 0.0 and last >= 1.0:
                self.scroll.pack_forget()  # hide
            else:
                self.scroll.pack(side="right",fill='y')

            self.scroll.set(first, last)
        #------------------------------------


        self.list.config(yscrollcommand=auto_scrollbar)
        self.list.pack(fill="both",expand=True)
        
        self.items={}
        for i in range(len(content_list)):
            self.items[content_list[i]]=i
            self.list.insert(tk.END, content_list[i])
            self.list.itemconfig(i,fg=text_color)

    
           
            
        
        

        