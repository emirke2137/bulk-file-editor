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
        self.path=""

        self.button_border=tk.Frame(parent,bg=button_border_color)
        self.button=tk.Label(self.button_border,text="Open Folder",
                            bg=button_color,fg=button_text_color,
                            font=('helvetica',24))
        

        self.arrow_buton=tk.Label(parent)

        self.button_border.place(relx=0.25, rely=0.2,relwidth=0.5,relheight=0.2)
        self.button.pack(padx=1,pady=1,expand=True,fill='both')

        self.header_border=tk.Frame(parent,background=border_color)
        self.background=tk.Frame(self.header_border, background=main_color)
        self.header_path = tk.Label(self.background,
                                        background=main_color, 
                                        text="", 
                                        foreground=text_color,
                                        font=("helvetica",10),
                                        anchor='w',padx=10)

        self.header_name = tk.Label(self.background,
                                        background=main_color, 
                                        text="", 
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


        self.canvas = Canvas(self.root,background=main_color)
        self.scrollbar = Scrollbar(self.root, orient='vertical', command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, background=main_color)

        def on_enter_button(event):
            self.button.configure(bg=button_text_color,fg=button_color)
        def on_leave_button(event):
            self.button.configure(bg=button_color,fg=button_text_color)

        def on_enter_browse(event):
            self.browse_button.configure(bg=button_text_color,fg=button_color)
        def on_leave_browse(event):
            self.browse_button.configure(bg=button_color,fg=button_text_color)

        def on_enter_dir(event):
            event.widget.configure(bg=button_color,fg=main_color)
        def on_leave_dir(event):
            event.widget.configure(bg=main_color,fg=button_color)
        

        def show_directories(event):
            
            path = filedialog.askdirectory()
            open_directory(path)
            
        def goto_directory(event):
            
            open_directory(self.path+'/'+event.widget.cget('text'))

        def open_directory(path):
            file_system.get_contents(path)
            self.path=path
            path=path.split('/')
            dir_name=path[-1]
            path='/'.join(path[:-1])

            files.set_items([x.name for x in file_system.files])

            if len(file_system.directories)>0:

                self.button.pack_forget()
                self.button_border.place_forget()

                [child.destroy() for child in self.scrollable_frame.winfo_children()]
                self.browse_button_border.place(x=10,y=10,relwidth=1, width=-20, height=40)
                self.browse_button.pack(fill='both',expand=True, padx=1,pady=1)

                self.header_border.place(x=70,y=60,relwidth=1, width=-80, height=50)
                self.background.pack(fill="both", expand=True, padx=1, pady=1)
                self.header_path.pack(fill="both", expand=True, padx=1, pady=1)
                self.header_name.pack(fill="both", expand=True, padx=1, pady=1)
                self.header_path.configure(text=path)
                self.header_name.configure(text=dir_name)
                self.up_button_border.place(x=10,y=60, width=50, height =50)
                
                self.canvas.place(x=10,y=120,width=-20,relwidth=1, height=-130, relheight=1)

                
                self.scrollbar.place(relx=1,x=-10,y=120,width=10,relheight=1, height=-130)
                self.canvas.configure(yscrollcommand=self.scrollbar.set)
                self.canvas.create_window((70, 0), window=self.scrollable_frame, anchor="nw", width=280)
                self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

                self.dirs=[]
                for d in file_system.directories:

                    border=tk.Frame(self.scrollable_frame, background=button_color)
                    border.pack(pady=5, fill='x',expand=True)
                    directory=tk.Label(border, text=d.name, background=main_color,fg=button_color)
                    directory.pack(padx=1,pady=1,fill='x',expand=True)
                    self.dirs.append(directory)

                    directory.bind("<Enter>",on_enter_dir)
                    directory.bind("<Leave>",on_leave_dir)
                    directory.bind("<Button>",goto_directory)
            
            else:
                self.canvas.place_forget()
                self.scrollbar.place_forget()
                self.button_border.place(relx=0.25, rely=0.2,relwidth=0.5,relheight=0.2)
                self.button.pack(padx=1,pady=1,expand=True,fill='both')



        self.button.bind("<Enter>",on_enter_button)
        self.button.bind("<Leave>",on_leave_button)
        self.button.bind("<Button>",show_directories)

        self.browse_button.bind("<Enter>",on_enter_browse)
        self.browse_button.bind("<Leave>",on_leave_browse)
        self.browse_button.bind("<Button>",show_directories)




        
        
