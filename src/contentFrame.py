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

        
        self.canvas.configure(yscrollcommand=auto_scrollbar)
        
    def update_selection(self,selected):
        print(selected)
        
        if selected:
            size = self.pair.set_selected(selected)
            self.place_configure(height=-(180+size))
            self.canvas.place_configure(height=-(240+size))


            
        else:
            self.pair.border.place_forget()
            self.pair.place_forget()
            self.pair.pack_forget()
            self.pair.canvas.place_forget()
            self.pair.scroll.place_forget()
            self.place_configure(height=-180)

            def auto_scrollbar(first, last):
                first = float(first)
                last = float(last)
                if first <= 0.0 and last >= 1.0:
                    self.scroll.place_forget()  
                else:
                    self.scroll.place(relx=1,x=-10,y=70,width=10,relheight=1, height=-240)

                self.scroll.set(first, last)

            self.canvas.configure(yscrollcommand=auto_scrollbar,bg=self.main_color)
            self.canvas.place_configure(height=-240)
            


                
    def pair(self,pair):
        self.pair=pair

    #list files in current directory
    def set_items(self,list):
    
        self.items=list
        self.clear_items()
        self.pair.clear_items()
        self.canvas.place(x=20,y=70,relwidth=1, relheight=1, width=-30,height=-240 )
        self.scroll.place(relx=1,x=-10,y=70,width=10,relheight=1, height=-240)
        self.canvas.create_window((10, 0), window=self.scrollable_frame, anchor="nw")
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        for item in list:
            
            elem=tk.Label(self.scrollable_frame, text=item,fg=self.border_color,background=self.main_color,anchor="w", font=('helvetica',14))
            elem.pack(padx=1,pady=1,fill='x')
            self.items_obj.append(elem)
            
    #remove listed files
    def clear_items(self):
        [child.destroy() for child in self.scrollable_frame.winfo_children()]
        for obj in self.items_obj:
            obj.pack_forget()
        self.items_obj=[]

    
    #intended for paired frame - list files that are selected
    def set_selected(self,list):

        #space needed for canvas based on the number of items
        size=min(len(list)*24,320)
    
        #dynamic scrollbar for selected files - only show when needed
        def auto_scrollbar2(first, last):
            #confirm box height + margins + selected files frame height 
            offset=150 + 20+ size 
            first = float(first)
            last = float(last)
            if first <= 0.0 and last >= 1.0:
                self.scroll.place_forget()  
            else:
                self.scroll.place(relx=1,x=-31,rely=1, y=-offset,width=10, height=size)
            
            self.scroll.set(first, last)

        #dynamic scrollbar for all files
        def auto_scrollbar1(first, last):
                first = float(first)
                last = float(last)
                if first <= 0.0 and last >= 1.0:
                    self.pair.scroll.place_forget()  
                else:
                    self.pair.scroll.place(relx=1,x=-10,y=70,width=10,relheight=1, height=-(240+size+100))

                self.pair.scroll.set(first, last)

        self.canvas.configure(yscrollcommand=auto_scrollbar2)
        print(size)
        #add frame for selected items if not added yet
        if not self.winfo_viewable():
            if self.border==None:
                self.place(anchor='sw', x=20,rely=1,y=-170,relwidth=1,width=-40, height=size+80)
                
            else:
                
                self.border.place(anchor='sw', x=20,rely=1,y=-170,relwidth=1,width=-40, height=size+80)
                self.pack(padx=1,pady=1,fill="both", expand=True)
                self.pair.canvas.place_configure(height=-260-size-80)
        self.pair.canvas.configure(yscrollcommand=auto_scrollbar1)

           
        self.clear_items()
        self.border.place_configure(height=size+80)     
        self.canvas.place(anchor='sw', x=21,rely=1,y=-171,relwidth=1,width=-42, height=size-1)   
        self.scroll.place(relx=1,x=-31,rely=1, y=-170-size,width=10, height=size)
        self.canvas.create_window((10, 0), window=self.scrollable_frame, anchor="nw")
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        for item in list:
            
            elem=tk.Label(self.scrollable_frame, text=item,fg=self.border_color,background=self.main_color,anchor="w", font=('helvetica',14))
            elem.pack(padx=1,pady=1,fill='x')
            
            self.items_obj.append(elem)

        #frames total height, for the other frame to adjust
        return size+100






    
           
    
        
        

        