import os
from stat import *
from pathlib import Path


class Filesystem:
    def __init__(self,path):
        self.curent_location = path
        self.directories=[]
        self.files=[]


        for item in Path(path).iterdir():     
            if item.is_dir():
                self.directories.append(item)
            elif item.is_file():
                file= File(
                    item.stem,
                    item.suffix,
                    item.stat().st_size,
                    item.stat().st_ctime,
                    filemode(item.stat().st_mode)
                )
                self.files.append(file)

#togle hidden files manualy

class File:
    def __init__(self,name,ext,size,created,permissions):
        self.name=name
        self.ext=ext
        self.size=size
        self.creation_time=created
        self.permissions=permissions
        