from copyreg import add_extension
import os
import tkinter as tk
from tkinter import filedialog

from areaFrame import AreaFrame
from switchFrame import SwitchFrame


class OptionsFrame(AreaFrame):

    def __init__(self, parent,order,name,switches,filesystem):
        self.main_color = '#171b16'
        self.border_color = '#41aba1'
        self.text_color = '#49a93b'
        self.name=name
        self.switches=switches
        self.selected_extensions=set()
        self.input_words=[]
        self.filesystem=filesystem
        super().__init__(parent)
       
        self.switch_frame_select = SwitchFrame(parent,order,name,self)
        self.switch_frame_select.place()
        self.switches[name]=self.switch_frame_select

        



        if name=='select':

            label_extensions=tk.Label(self.content,text='extensions',anchor='w',background=self.main_color,fg=self.text_color,font=('helvetica',16))
            label_extensions.pack(padx=10,pady=10,fill='x')
            container_border_extensions=tk.Frame(self.content,bg=self.text_color,)
            container_border_extensions.pack(padx=10,pady=10,fill='x')
            self.container_extensions=tk.Frame(container_border_extensions,bg=self.main_color,height=30)
            self.container_extensions.pack(padx=1,pady=1,fill='x')          
           


            label_words=tk.Label(self.content,text='containing words',anchor='w',background=self.main_color,fg=self.text_color,font=('helvetica',16))
            label_words.pack(padx=10,pady=10,fill='x')
            container_border_words=tk.Frame(self.content,bg=self.text_color)
            container_border_words.pack(padx=10,pady=10,fill='x')
            container_words=tk.Frame(container_border_words,bg=self.main_color)
            container_words.pack(padx=1,pady=1,fill='x')
            self.text_field=tk.Text(container_words,font=('helvetica',16),bg=self.main_color,fg=self.text_color,height=1)
            self.text_field.pack(side='left',fill='x',expand=True)
            def get_word(event):
                text = self.text_field.get("1.0","end-1c")
                print(text)
            self.text_field.bind("<space>",get_word)

            label_size=tk.Label(self.content,text='containing size',anchor='w',background=self.main_color,fg=self.text_color,font=('helvetica',16))
            label_size.pack(padx=10,pady=10,fill='x')
            container_border_size=tk.Frame(self.content,bg=self.text_color)
            container_border_size.pack(padx=10,pady=10,fill='x')
            container_size=tk.Frame(container_border_size,bg=self.main_color)
            container_size.pack(padx=1,pady=1,fill='x')
        elif name=='edit':
            pass


    def clicked(self):
        #move other switches back to the default position
        for x,y in self.switches.items():
            if(x!=self.name):
                y.place()

        #move the option frame up
        self.lift()
        
    def uptade_content(self):
        def on_enter_field(event):
            event.widget.configure(bg=self.text_color,fg=self.main_color)
        def on_leave_field(event):
            event.widget.configure(bg=self.main_color,fg=self.text_color)
        def add_extension(event):
            extension=event.widget.cget("text")
            if extension in self.selected_extensions:   
                self.selected_extensions.remove(extension)
            else:
                self.selected_extensions.add(extension)


        for ext in self.filesystem.extensions_set:
            print(ext)
            border = tk.Frame(self.container_extensions,bg=self.text_color)
            extenstion_label=tk.Label(border,text=ext,font=('helvetica',14),bg=self.main_color,fg=self.text_color)
            extenstion_label.bind("<Enter>",on_enter_field)
            extenstion_label.bind("<Leave>",on_leave_field)
            extenstion_label.bind("<Button-1>",add_extension)

            extenstion_label.pack(padx=1,pady=1)
            border.pack(side = 'left')


      

    
        