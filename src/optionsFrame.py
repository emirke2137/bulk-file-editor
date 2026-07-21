from copyreg import add_extension
import os
import tkinter as tk
from tkinter import filedialog

from areaFrame import AreaFrame
from switchFrame import SwitchFrame


class OptionsFrame(AreaFrame):

    def __init__(self, parent,order,name,switches,filesystem,files_frame=None):
        self.main_color = '#171b16'
        self.border_color = '#41aba1'
        self.text_color = '#49a93b'
        self.highlight_color = '#c7faa7'
        self.font=('helvetica',16)
        self.name=name
        self.switches=switches
        self.selected_extensions=set()
        self.input_words=set()
        self.conversion={
            "kB":1000,
            "mB":1000000,
            "gB":1000000000
        }
        self.selected_unit="kB"
        self.size_range=[0,0]
        self.filesystem=filesystem
        self.files_frame=files_frame
        super().__init__(parent)
       
        self.switch_frame_select = SwitchFrame(parent,order,name,self)
        self.switch_frame_select.place()
        self.switches[name]=self.switch_frame_select

        



        if name=='select':

            label_extensions=tk.Label(self.content,text='extensions',anchor='w',background=self.main_color,fg=self.text_color,font=self.font)
            label_extensions.pack(padx=10,pady=10,fill='x')
            container_border_extensions=tk.Frame(self.content,bg=self.text_color,)
            container_border_extensions.pack(padx=10,pady=10,fill='x')
            self.container_extensions=tk.Frame(container_border_extensions,bg=self.main_color,height=30)
            self.container_extensions.pack(padx=1,pady=1,fill='x')          
           

            label_words=tk.Label(self.content,text='containing words',anchor='w',background=self.main_color,fg=self.text_color,font=self.font)
            label_words.pack(padx=10,pady=10,fill='x')
            container_border_words=tk.Frame(self.content,bg=self.text_color)
            container_border_words.pack(padx=10,pady=10,fill='x')
            container_words=tk.Frame(container_border_words,bg=self.main_color)
            container_words.pack(padx=1,pady=1,fill='x')
            self.text_field=tk.Text(container_words,font=self.font,bg=self.main_color,fg=self.text_color,height=1)
            self.text_field.pack(side='left',fill='x',expand=True)
            
            def get_word(event):
                self.input_words = set(self.text_field.get("1.0",tk.END).split())
                self.update_selection()
                print(self.input_words)

            self.text_field.bind("<space>",get_word)


            label_size=tk.Label(self.content,text='size',anchor='w',background=self.main_color,fg=self.text_color,font=self.font)
            label_size.pack(padx=10,pady=10,fill='x')
            container_border_min=tk.Frame(self.content,bg=self.text_color)
            container_border_min.pack(side='left',padx=10,pady=10,)
            tk.Label(self.content,text=" - ", bg=self.main_color,fg=self.text_color,font=self.font).pack(side='left',padx=1,pady=1,)

            container_border_max=tk.Frame(self.content,bg=self.text_color)
            container_border_max.pack(side='left',padx=10,pady=10,)
            self.container_min=tk.Text(container_border_min,bg=self.main_color,fg=self.text_color,height=1,width=8)
            self.container_min.pack(padx=1,pady=1)
            self.container_max=tk.Text(container_border_max,bg=self.main_color,fg=self.text_color,height=1,width=8)
            self.container_max.pack(padx=1,pady=1)
            self.container_min.insert('1.0','0')
            self.container_max.insert('1.0','0')
            option_kb_border=tk.Frame(self.content,bg=self.text_color)
            option_kb_border.pack(side='left',padx=10,pady=10,)
            self.option_kb=tk.Label(option_kb_border,text="kB",bg=self.highlight_color,fg=self.text_color,font=('helvetica',12))
            self.option_kb.pack(padx=1,pady=1)
            option_mb_border=tk.Frame(self.content,bg=self.text_color)
            option_mb_border.pack(side='left',padx=10,pady=10,)
            self.option_mb=tk.Label(option_mb_border,text="mB",bg=self.main_color,fg=self.text_color,font=('helvetica',12))
            self.option_mb.pack(padx=1,pady=1)
            option_gb_border=tk.Frame(self.content,bg=self.text_color)
            option_gb_border.pack(side='left',padx=10,pady=10,)
            self.option_gb=tk.Label(option_gb_border,text="gB",bg=self.main_color,fg=self.text_color,font=('helvetica',12))
            self.option_gb.pack(padx=1,pady=1)
            
            def on_enter_field(event):
                event.widget.configure(bg=self.text_color,fg=self.main_color)
            def on_leave_field(event):
                if event.widget.cget("text") ==self.selected_unit:
                    event.widget.configure(bg=self.highlight_color,fg=self.text_color)
                else:
                    event.widget.configure(bg=self.main_color,fg=self.text_color)
            def on_pick(event):
                self.option_kb.configure(bg=self.main_color,fg=self.text_color)
                self.option_mb.configure(bg=self.main_color,fg=self.text_color)
                self.option_gb.configure(bg=self.main_color,fg=self.text_color)
                self.selected_unit = event.widget.cget("text")
                
                self.size_range[0]=int(self.container_min.get('1.0',tk.END))*self.conversion[self.selected_unit]
                self.size_range[1]=int(self.container_max.get('1.0',tk.END))*self.conversion[self.selected_unit]
                self.update_selection()

            def on_min_modified(event):
                
                value = self.container_min.get("1.0", "end-1c")
                if value.isdigit():
                    self.size_range[0]=int(value)*self.conversion[self.selected_unit]
                    self.update_selection()
                else:
                    self.container_min.delete("end-2c", "end-1c")
                
                

            def on_max_modified(event):
                value = self.container_max.get("1.0", "end-1c")
                if value.isdigit():
                    self.size_range[1]=int(value)*self.conversion[self.selected_unit]
                    self.update_selection()
                else:
                    self.container_max.delete("end-2c", "end-1c")
                
                

            self.option_kb.bind("<Enter>",on_enter_field)
            self.option_kb.bind("<Leave>",on_leave_field)
            self.option_kb.bind("<Button-1>",on_pick)
            self.option_mb.bind("<Enter>",on_enter_field)
            self.option_mb.bind("<Leave>",on_leave_field)
            self.option_mb.bind("<Button-1>",on_pick)
            self.option_gb.bind("<Enter>",on_enter_field)
            self.option_gb.bind("<Leave>",on_leave_field)
            self.option_gb.bind("<Button-1>",on_pick)
            self.container_min.bind("<KeyRelease>", on_min_modified)
            self.container_max.bind("<KeyRelease>", on_max_modified)

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
            if event.widget.cget("text") in self.selected_extensions:
                event.widget.configure(bg=self.highlight_color,fg=self.text_color)
            else:
                event.widget.configure(bg=self.main_color,fg=self.text_color)
        def add_extension(event):
            extension=event.widget.cget("text")
            if extension in self.selected_extensions:   
                self.selected_extensions.remove(extension)
                event.widget.configure(bg=self.main_color,fg=self.text_color)
                self.update_selection()
            else:
                self.selected_extensions.add(extension)
                event.widget.configure(bg=self.highlight_color,fg=self.text_color)
                self.update_selection()

        [child.destroy() for child in self.container_extensions.winfo_children()]
        for ext in self.filesystem.extensions_set:
            
            border = tk.Frame(self.container_extensions,bg=self.text_color)
            extenstion_label=tk.Label(border,text=ext,font=('helvetica',14),bg=self.main_color,fg=self.text_color)
            extenstion_label.bind("<Enter>",on_enter_field)
            extenstion_label.bind("<Leave>",on_leave_field)
            extenstion_label.bind("<Button-1>",add_extension)

            extenstion_label.pack(padx=1,pady=1)
            border.pack(side = 'left')

        
        if self.size_range[1]==0:
            self.size_range[1]=self.filesystem.max_size
            self.container_max.delete("1.0", tk.END)
            self.container_max.insert("1.0",self.filesystem.max_size//self.conversion[self.selected_unit]+1)


    def update_selection(self):
        selected=self.filesystem.filter(self.selected_extensions,self.input_words,self.size_range)
        self.files_frame.update_selection(selected)
    
  
