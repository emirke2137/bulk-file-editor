import tkinter as tk
from areaFrame import AreaFrame
class ConfirmationFrame(AreaFrame):

    def __init__(self,parent):
        self.main_color = '#171b16'
        self.text_color = '#2fc468'
        self.border_color = '#41aba1'
        self.secondary_color = '#49a93b'
        super().__init__(parent,)
        self.content.columnconfigure(0,weight=2)
        self.content.columnconfigure(1,weight=1)
        self.content.rowconfigure(0,weight=1)
        self.content.rowconfigure(1,weight=1)

        area1 = tk.Frame(self.content, bg=self.secondary_color)
        area2 = tk.Frame(self.content, bg=self.secondary_color)
        area3 = tk.Frame(self.content, bg=self.secondary_color)

        area1.grid(column=0,row=0,padx=5,pady=5,sticky="nsew")
        area2.grid(column=0,row=1,padx=5,pady=5,sticky="nsew")
        area3.grid(column=1,row=0,padx=5,pady=5, rowspan=2,sticky="nsew")

        self.apply_button=tk.Label(area3,text="Apply",bg=self.secondary_color, font=("Jura",32))
        self.apply_button.pack(fill="both",expand=True)

        copy_field_container=tk.Frame(area1,bg=self.secondary_color)
        copy_field_container.pack(fill="both",expand=True,padx=5,pady=5)

        copy_field_label = tk.Label(copy_field_container, text="Copy to a new folder ",bg=self.secondary_color,fg=self.main_color,font=('helvetica',16),anchor="w")
        copy_field_label.pack(padx=5,fill="x",expand=True)

        copy_path_input=tk.Label(copy_field_container,text="/home/user/folder...",background=self.main_color,fg=self.secondary_color,font=('helvetica',12),anchor="w")
        copy_path_input.pack(padx=5,fill="x",expand=True)

        self.overwrite=tk.Label(area2,text="Overwrite",bg=self.main_color,fg=self.secondary_color,font=('helvetica',16),anchor="w")
        self.overwrite.pack(padx=5,pady=5,fill="both",expand=True)



