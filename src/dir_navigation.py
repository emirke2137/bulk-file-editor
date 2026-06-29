import tkinter as tk
from tkinter import filedialog
from tkinter import Canvas
from tkinter import Scrollbar

class DirNavigation():
    def __init__(self,parent,file_system,files):
        button_color = '#49a93b'
        button_text_color = '#053836'
        button_border_color = '#41aba1'

        main_color = '#171b16'
        text_color = '#2fc468'
        border_color = '#41aba1'
        self.root=parent

        self.button_border=tk.Frame(parent,bg=button_border_color)
        self.button=tk.Label(self.button_border,text="Open Folder",
                            bg=button_color,fg=button_text_color,
                            font=('helvetica',24))
        

        self.arrow_buton=tk.Label(parent)

        self.header_border=tk.Frame(parent,background=button_border_color)
        self.header = tk.Label(self.header_border,
                                background=button_color, 
                                text="path", 
                                foreground=button_text_color,
                                font=("helvetica",16),
                                anchor='w',padx=10)

        self.button_border.place(relx=0.25, rely=0.2,relwidth=0.5,relheight=0.2)
        self.button.pack(padx=1,pady=1,expand=True,fill='both')


        self.header_border=tk.Frame(parent,background=border_color)
        self.header = tk.Label(self.header_border,
                                        background=main_color, 
                                        text="wolololo", 
                                        foreground=text_color,
                                        font=("helvetica",16),
                                        anchor='w',padx=10)

        self.up_button_border=tk.Frame(parent,background=border_color)
        self.up_button = tk.Label(self.up_button_border,
                                        background=main_color, 
                                        text="wolololo", 
                                        foreground=text_color,
                                        font=("helvetica",16),
                                        anchor='w',padx=10)

        self.browse_button_border=tk.Frame(parent,bg=button_border_color)
        self.browse_button=tk.Label(self.browse_button_border,text="Browse",
                            bg=button_color,fg=button_text_color,
                            font=('helvetica',20))


        def on_enter_button(event):
            self.button.configure(bg=button_text_color,fg=button_color)
        def on_leave_button(event):
            self.button.configure(bg=button_color,fg=button_text_color)

        def on_enter_browse(event):
            self.browse_button.configure(bg=button_text_color,fg=button_color)
        def on_leave_browse(event):
            self.browse_button.configure(bg=button_color,fg=button_text_color)




        def show_directories(event):
            
            dir_name = filedialog.askdirectory()
            file_system.get_contents(dir_name)
            
            files.set_items([x.name for x in file_system.files])
            if len(file_system.directories)>0:
                self.button.pack_forget()
                self.button_border.place_forget()

                self.browse_button_border.place(x=10,y=10,relwidth=1, width=-20, height=40)
                self.browse_button.pack(fill='both',expand=True, padx=1,pady=1)

                self.header_border.place(x=70,y=60,relwidth=1, width=-80, height=50)
                self.header.pack(fill="both", expand=True, padx=1, pady=1)
                
                self.up_button_border.place(x=10,y=60, width=50, height =50)
                canvas = Canvas(self.root,background=main_color)
                canvas.place(x=10,y=120,width=-20,relwidth=1, height=-130, relheight=1)

                scrollbar = Scrollbar(self.root, orient='vertical', command=canvas.yview)
                scrollbar.place(relx=1,x=-10,y=120,width=10,relheight=1, height=-130)

                canvas.configure(yscrollcommand=scrollbar.set)
                scrollable_frame = tk.Frame(canvas)

                canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
                scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

                for i in range(30):
                    tk.Label(scrollable_frame, text=f"Item {i+1}", width=10).pack(pady=5)


            
            

        self.button.bind("<Enter>",on_enter_button)
        self.button.bind("<Leave>",on_leave_button)
        self.button.bind("<Button>",show_directories)

        self.browse_button.bind("<Enter>",on_enter_browse)
        self.browse_button.bind("<Leave>",on_leave_browse)
        self.browse_button.bind("<Button>",show_directories)


        
        



        
        
