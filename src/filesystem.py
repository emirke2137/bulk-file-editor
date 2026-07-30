import os
from stat import *
from pathlib import Path
import shutil


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
               
                if (size and file.size>=size[0] and file.size<=size[1]) or (not size):
                    
                    if not bool(word_set):
                        selected.add(file.name+file.ext)
                        self.selected_idx.add(idx)
                    else:                        
                        for word in word_set:
                            if word in file.name:
                                selected.add(file.name+file.ext)
                                self.selected_idx.add(idx)
        
        return list(selected)
                
            
    def save(self,sourcepath,destpath,idx,new_name):
        try:
            shutil.copyfile(sourcepath+"/"+self.files[idx].get_name(),
                            destpath+"/"+new_name+self.files[idx].ext)
            return (True,"")
        except shutil.SameFileError:
            return (False,f"File with name {new_name} already exists")
        except Exception as e:
            return (False,f"An error occurred: {e}")

    def rename(self,sourcepath,idx,new_name):
        try:
            os.rename(sourcepath+"/"+self.files[idx].get_name(),
                    sourcepath+"/"+new_name+self.files[idx].ext)
            return (True,"")
        except Exception as e:
            return (False,f"An error occurred: {e}")

    def make_copy_dir(self,path):
        path=Path(path)
        
        try:
            path.mkdir()
            return (True,"")
        
        except FileExistsError:
            
            if path.is_dir():
                if any(path.iterdir()):
                    return(False,f"Directory '{path}' already exists and is not empty")
                else:
                    return (True,"")
            else:
                return(False,f"'{path}' exist and is a file.")
        except PermissionError:
            return(False,f"Permission denied: Unable to create '{path}'.")
        except Exception as e:
            return(False,f"An error occurred: {e}")
            
    


class File:
    def __init__(self,name,ext,size,created,permissions):
        self.name = name
        self.ext = ext
        self.size = size
        self.creation_time = created
        self.permissions = permissions

    def get_name(self):
        return self.name+self.ext

class Directory:
    def __init__(self,name):
        self.name = name
        