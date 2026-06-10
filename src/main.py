from areaFrame import AreaFrame
from optionsFrame import OptionsFrame
from tkinter.ttk import Style
import tkinter as tk



# Create main window
root = tk.Tk()
root.geometry("960x720")
root.minsize(960,720)
root.title("Bulk File Editor")


paddings = {'padx': 5, 'pady': 5}
entry_font = {'font': ('Helvetica', 11)}



menu_frame = AreaFrame(root)
preview_frame = AreaFrame(root)
navigation_frame =AreaFrame(menu_frame)

select_options_frame = OptionsFrame(menu_frame,0)
edit_options_frame = tk.Frame(menu_frame,bg='blue')

#layout:
#nav
#switch buttons out of frame
#edit

menu_frame.place(x=0,y=0,relwidth=0.4,relheight=1)
preview_frame.place(relx=0.4,y=0,relwidth=0.6,relheight=1)

navigation_frame.place(x=0,y=0,relwidth=1,relheight=0.55)
select_options_frame.place(x=1,rely=0.5,relwidth=1,width=-1,relheight=0.5,anchor="nw")

#edit_options_frame.place(x=1,rely=0.5,relwidth=1,width=-1,relheight=0.5)








if __name__ == "__main__":
    root.mainloop()
