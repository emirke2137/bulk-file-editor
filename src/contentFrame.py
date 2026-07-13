import tkinter as tk
from tkinter import Canvas
from tkinter import Scrollbar
class ContentFrame(tk.Frame):
    def __init__(self,parent,label,use_border=False):
        self.main_color = '#171b16'
        self.text_color = '#2fc468'
        self.border_color = '#41aba1'
        self.items={}
        self.items_obj={}
        self.border=None
        if(use_border):
            self.border=tk.Frame(parent,bg=self.border_color)
            super().__init__(self.border,background=self.main_color)
        else:
            super().__init__(parent,background=self.main_color)
        self.header_border=tk.Frame(self,background=self.border_color)
        self.header = tk.Label(self.header_border,
                                background=self.main_color, 
                                text=label, 
                                foreground=self.text_color,
                                font=("helvetica",16),
                                anchor='w',padx=10)
        self.header_border.place(x=10,y=10,width=420, height=50)
        self.header.pack(fill="both", expand=True, padx=1, pady=1)
        
        self.canvas = Canvas(parent,background=self.main_color,bd=1,highlightthickness=0)
        self.scroll = tk.Scrollbar(parent, orient="vertical", command=self.canvas.yview,width=5)
        self.scrollable_frame = tk.Frame(self.canvas, background=self.main_color)
        

        
        #------------------------------------
        #custom scroll command to show scrollball only when needed
        def auto_scrollbar(first, last):
            first = float(first)
            last = float(last)
            if first <= 0.0 and last >= 1.0:
                self.scroll.place_forget()  
            else:
                self.scroll.place(relx=1,x=-10,y=70,width=10,relheight=1, height=-240)

            self.scroll.set(first, last)

        #
        def _test_select(event):
            selected=self.list.curselection()
            
            if not self.pair.winfo_viewable():
                if self.pair.border==None:
                    self.pair.place(anchor='sw', x=20,rely=1,y=-170,relwidth=1,width=-40, height=80)
                    self.place_configure(height=-260)
                    print('no')
                else:
                    print('es')
                    self.pair.border.place(anchor='sw', x=20,rely=1,y=-170,relwidth=1,width=-40, height=80)
                    self.pair.pack(padx=1,pady=1,fill="both", expand=True)

            self.pair.list.delete(0,tk.END)
            for i in range(len(selected)):
                print(i,selected[i])
                self.pair.list.insert(tk.END, self.items[selected[i]])
                self.pair.list.itemconfig(i,fg=self.text_color)
                self.place_configure(height=-(260+i*20))
                if self.pair.border==None:
                    self.pair.place_configure(height=80+i*20)
                else:
                    self.pair.border.place_configure(height=80+i*20)
        #add max height
        #
        #------------------------------------


   
        self.canvas.configure(yscrollcommand=auto_scrollbar)
        

    def pair(self,pair):
        self.pair=pair

    def set_items(self,list):
   
        self.items=list
        self.clear_items()
        self.pair.clear_items()
        self.canvas.place(x=20,y=70,relwidth=1, relheight=1, width=-30,height=-240)
        self.scroll.place(relx=1,x=-10,y=70,width=10,relheight=1, height=-240)
        self.canvas.create_window((10, 0), window=self.scrollable_frame, anchor="nw", width=400)
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        for i in range(len(list)):
            print(list[i])
            
            elem=tk.Label(self.scrollable_frame, text=list[i],fg=self.border_color,background=self.main_color,anchor="w")
            elem.pack(padx=1,pady=1,fill='x')
            self.items_obj.append(elem)
            
            
        print(len(self.scrollable_frame.winfo_children()))
        print(self.scrollable_frame.winfo_reqheight())
        print(self.canvas.bbox("all"))

    def clear_items(self):
        [child.destroy() for child in self.scrollable_frame.winfo_children()]
        for obj in self.items_obj:
            obj.pack_forget()
        self.items_obj=[]



    
           
    
        
        

        