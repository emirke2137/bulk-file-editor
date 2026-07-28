import os
from stat import *
from pathlib import Path


class Filesystem:
    def __init__(self):
        self.extensions_set=set()
        self.max_size=0
        self.selected_idx=set()

    def get_contents(self,path):
        self.curent_location = path
        self.directories=[]
        self.files=[]
        self.extensions_set=set()
        self.max_size=0
        

        for item in Path(path).iterdir():  

            if item.is_dir():
                directory = Directory(
                    item.stem
                )
                self.directories.append(directory)

            elif item.is_file():
                file = File(
                    item.stem,
                    item.suffix,
                    item.stat().st_size,
                    item.stat().st_ctime,
                    filemode(item.stat().st_mode)
                )
                self.extensions_set.add(item.suffix)
                self.files.append(file)
                if item.stat().st_size>self.max_size:
                    self.max_size=item.stat().st_size

            
    def filter(self, ext_set=set(), word_set=set(), size=[]):
        selected=set()
        self.selected_idx=set()
        
        for idx,file in enumerate(self.files):
            
            if (bool(ext_set) and file.ext in ext_set) or (not bool(ext_set)):
               
                if (size and file.size>size[0] and file.size<size[1]) or (not size):
                    
                    if not bool(word_set):
                        selected.add(file.name+file.ext)
                        self.selected_idx.add(idx)
                    else:                        
                        for word in word_set:
                            if word in file.name:
                                selected.add(file.name+file.ext)
                                self.selected_idx.add(idx)
        
        return list(selected)
                
            
    def save(self,path):
        pass


#togle hidden files manualy

class File:
    def __init__(self,name,ext,size,created,permissions):
        self.name = name
        self.ext = ext
        self.size = size
        self.creation_time = created
        self.permissions = permissions

class Directory:
    def __init__(self,name):
        self.name = name
        