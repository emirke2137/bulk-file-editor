from dir_navigation import DirNavigation
from contentFrame import ContentFrame
from filesystem import Filesystem
from areaFrame import AreaFrame
from optionsFrame import OptionsFrame
import tkinter as tk


#internal file and directory managing system
fs = Filesystem()

# Create main window
root = tk.Tk()
root.geometry("960x720")
root.minsize(960,720)
root.title("Bulk File Editor")



paddings = {'padx': 5, 'pady': 5}
entry_font = {'font': ('Helvetica', 11)}


navigation_frame = AreaFrame(root)
preview_frame = AreaFrame(root)
switches={}
select_options_frame = OptionsFrame(navigation_frame,0,"select",switches)
edit_options_frame = OptionsFrame(navigation_frame,1,"edit",switches)
select_options_frame.switch_frame_select.clicked()

navigation_frame.place(x=0,y=0,relwidth=0.4,relheight=1)
preview_frame.place(relx=0.4,y=0,relwidth=0.6,relheight=1)
edit_options_frame.place(anchor='sw',x=0,rely=1,height=300,relwidth=1)
select_options_frame.place(anchor='sw',x=0,rely=1,height=300,relwidth=1)




files_frame = ContentFrame(preview_frame.content, "Directory Content")
#height=-180
files_frame.place(x=10,y=10,relwidth=1,relheight=1,width=-20, height=-180)
selected_files_frame = ContentFrame(preview_frame.content, "Selected Files",True)
#selected_files_frame.place(anchor='sw', x=20,rely=1,y=-180,relwidth=1,width=-40, height=200)
files_frame.pair(selected_files_frame)
selected_files_frame.pair(files_frame)


confirm_frame = AreaFrame(preview_frame.content)
confirm_frame.place(anchor='sw',x=10,rely=1,y=-10,height=150,relwidth=1,width=-20)


navigation = DirNavigation(navigation_frame.content, fs, files_frame)
if __name__ == "__main__":
    
    root.mainloop()

