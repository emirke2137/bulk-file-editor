import tkinter as tk

from areaFrame import AreaFrame


class ConfirmationFrame(AreaFrame):

    def __init__(self,parent,filesystem,edits):
        self.main_color = '#171b16'
        self.border_color = '#41aba1'
        self.secondary_color = '#49a93b'
        self.button_text_color = '#053836'
        self.should_overwrite = False
        self.filesystem=filesystem
        self.edits=edits
        self.path=""
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

        self.apply_button=tk.Label(area3,text="Apply",bg=self.secondary_color,fg=self.button_text_color, font=("Helvetica",32))
        self.apply_button.pack(fill="both",expand=True)

        copy_field_container=tk.Frame(area1,bg=self.secondary_color)
        copy_field_container.pack(fill="both",expand=True,padx=5,pady=5)

        copy_field_label = tk.Label(copy_field_container, text="Copy to a new folder ",bg=self.secondary_color,fg=self.main_color,font=('helvetica',16),anchor="w")
        copy_field_label.pack(padx=5,fill="x",expand=True)

        self.copy_path_input=tk.Label(copy_field_container,text=self.path,background=self.main_color,fg=self.secondary_color,font=('helvetica',12),anchor="w")
        self.copy_path_input.pack(padx=5,fill="x",expand=True)

        self.overwrite=tk.Label(area2,text="Overwrite",bg=self.main_color,fg=self.secondary_color,font=('helvetica',16),anchor="w")
        self.overwrite.pack(padx=5,pady=5,fill="both",expand=True)

        def on_enter_copy_field(event):
            copy_field_container.configure(bg=self.secondary_color)
            copy_field_label.configure(bg=self.secondary_color,fg=self.main_color)
            self.copy_path_input.configure(bg=self.main_color,fg=self.secondary_color)

        def on_enter_overwrite_field(event):
            self.overwrite.configure(bg=self.secondary_color,fg=self.main_color)
        def on_leave_copy_field(event):
            if self.should_overwrite == True:
                copy_field_container.configure(bg=self.main_color)
                copy_field_label.configure(bg=self.main_color, fg=self.secondary_color)
                self.copy_path_input.configure(bg=self.secondary_color,fg=self.main_color)

        def on_leave_overwrite_field(event):
            if self.should_overwrite == False:
                self.overwrite.configure(bg=self.main_color,fg=self.secondary_color)
            
        def set_copy(event):
            self.should_overwrite=False
            self.overwrite.configure(bg=self.main_color,fg=self.secondary_color)

        def set_overwrite(event):
            self.should_overwrite=True
            copy_field_container.configure(bg=self.main_color)
            copy_field_label.configure(bg=self.main_color, fg=self.secondary_color)
            self.copy_path_input.configure(bg=self.secondary_color,fg=self.main_color)
            tk.messagebox.showwarning(message="After clicking APPLY the original file names will be overwriten. This action is irreversible.")

        def on_click_path(event):
            self.should_overwrite=False
            self.overwrite.configure(bg=self.main_color,fg=self.secondary_color)
            #open file dialog
            
        
        def on_enter_apply(event):
            self.apply_button.configure(bg=self.button_text_color,fg=self.secondary_color)
            
        def on_leave_apply(event):
            self.apply_button.configure(bg=self.secondary_color,fg=self.button_text_color)
            

        def on_click_apply(event):
            new_name=self.edits.preview.cget("text")
            if new_name =="" or not bool(filesystem.selected_idx):
                if not bool(filesystem.selected_idx):
                    tk.messagebox.showinfo(message="No files selected")
                else:
                    tk.messagebox.showinfo(message="Enter new name in the Edit tab")
            else:
                
                if self.should_overwrite==False:
                    success=self.filesystem.make_copy_dir(self.path+"-copy/")
                    if success[0]==False:
                        tk.messagebox.showerror(title="Couldn't create new folder.", message=f"Perhaps a folder with path {self.path+"-copy/"} already exist")
                        return "aborted"

                
            
                count=0
                successfully_renamed=0
                for idx in filesystem.selected_idx:
                    count+=1
                    new_name=new_name[:-1*self.edits.appendix_size]
                    print(filesystem.files[idx].get_name())
                    count_str=str(count)
                    appendix=""
                    print(len(count_str))
                    if len(count_str)<self.edits.appendix_size:
                        extra_zeors=["0"]*(self.edits.appendix_size-len(count_str))
                        appendix: str="".join(extra_zeors)
                    new_name=new_name+appendix+count_str
                
                    if self.should_overwrite==False:
                        print(new_name)
                        self.filesystem.save(self.path,self.path+"-copy",idx,new_name)
                    
                    else:
                        
                        is_renamed=self.filesystem.rename(self.path,idx,new_name)
                        if is_renamed[0]:
                            successfully_renamed+=1
                        else:
                            tk.messagebox.showerror(title="Couldn't rename file", 
                                                    message=f"Couldn't rename file {self.path} to {new_name}")

                tk.messagebox.showinfo(title="Renaming finished",message=f"{successfully_renamed} files out of {count} renamed successfully")
                        
                        

                        


                        



        copy_field_container.bind("<Enter>",on_enter_copy_field)
        copy_field_container.bind("<Leave>",on_leave_copy_field)
        copy_field_container.bind("<Button-1>",set_copy)
        copy_field_label.bind("<Enter>",on_enter_copy_field)
        copy_field_label.bind("<Leave>",on_leave_copy_field)
        copy_field_label.bind("<Button-1>",set_copy)
        self.copy_path_input.bind("<Enter>",on_enter_copy_field)
        self.copy_path_input.bind("<Leave>",on_leave_copy_field)
        self.copy_path_input.bind("<Button-1>",on_click_path)

        self.overwrite.bind("<Enter>",on_enter_overwrite_field)
        self.overwrite.bind("<Leave>",on_leave_overwrite_field)
        self.overwrite.bind("<Button-1>",set_overwrite)

        self.apply_button.bind("<Enter>",on_enter_apply)
        self.apply_button.bind("<Leave>",on_leave_apply)
        self.apply_button.bind("<Button-1>",on_click_apply)




