import tkinter as tk
from tkinter import filedialog

class DirNavigation():
    def __init__(self,parent,file_system,files):
        main_color = '#49a93b'
        text_color = '#053836'
        border_color = '#41aba1'
        
        self.button_border=tk.Frame(parent,bg=border_color)
        self.button=tk.Label(self.button_border,text="Open Folder",
                            bg=main_color,fg=text_color,
                            font=('helvetica',24))
        

        self.arrow_buton=tk.Label(parent)
        self.header_border=tk.Frame(parent,background=border_color)
        self.header = tk.Label(self.header_border,
                                background=main_color, 
                                text="path", 
                                foreground=text_color,
                                font=("helvetica",16),
                                anchor='w',padx=10)

        self.button_border.place(relx=0.25, rely=0.2,relwidth=0.5,relheight=0.2)
        self.button.pack(padx=1,pady=1,expand=True,fill='both')

        def on_enter(event):
            self.button.configure(bg=text_color,fg=main_color)
        def on_leave(event):
            self.button.configure(bg=main_color,fg=text_color)
        def show_directories(event):
            
            dir_name = filedialog.askdirectory()
            file_system.get_contents(dir_name)
            #self.button.pack_forget()
            #self.button_border.place_forget()
            

            files.set_items([x.name for x in file_system.files])
            
            

        self.button.bind("<Enter>",on_enter)
        self.button.bind("<Leave>",on_leave)
        self.button.bind("<Button>",show_directories)


        
        
