import os
class Filesystem:
    def __init__(self,path):
        self.curent_location = path
        self.directories=[]
        self.files=[]


        for item in os.scandir(path):
            print(item.stat().st_size)
            if item.is_dir():
                self.directories.append(item)
            elif item.is_file():
                file={
                    
                }
                self.files.append(file)

#togle hidden files manualy

class File:
    def __init__(self,name,ext,size):
        self.name=name
        self.ext=ext
        self.size=size