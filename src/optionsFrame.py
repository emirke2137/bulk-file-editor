import os
import tkinter as tk
from tkinter import filedialog

from areaFrame import AreaFrame
from switchFrame import SwitchFrame


class OptionsFrame(AreaFrame):

    def __init__(self, parent,order,name,switches):
        main_color = '#171b16'
        border_color = '#41aba1'
        self.name=name
        self.switches=switches
        super().__init__(parent)
       
        self.switch_frame_select = SwitchFrame(parent,order,name,self)
        self.switch_frame_select.place()
        self.switches[name]=self.switch_frame_select


    def clicked(self):
        #move other switches back to the default position
        for x,y in self.switches.items():
            if(x!=self.name):
                y.place()

        #move the option frame up
        self.lift()
        
        

      

    
        