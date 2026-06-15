
from filesystem import Filesystem
from areaFrame import AreaFrame
from optionsFrame import OptionsFrame
import tkinter as tk




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



if __name__ == "__main__":
    #root.mainloop()
    fs = Filesystem("/home/ropuch/rzeczy")
