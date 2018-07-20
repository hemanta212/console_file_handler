import os
from utilities import tdate, exists

class file:
    def __init__(self,filename=tdate()):
        self.filename = filename
        try:
            self.name, self.ext =self.filename.split(".")
            
        except:
            self.name = self.filename
            self.ext = "txt"
            self.filename = self.name + "." + self.ext

        with open(self.filename, 'w'):
            print("file",self.filename,"created!")
        self.open(self.filename)

    @staticmethod
    def rename(old,new):
        if exists(old):
            os.rename(old, new)
            print("file renamed")
        else:
            print("file doesnot exists in the folder")
            
    @staticmethod 
    def open(file):
        if exists(file):
            print("                               Status: EDITING!!  || ",file,"  | ",len(file),"||")
            with open(file,'r') as fr:
                print(fr.read())
                print()
                with open(file, "a") as fw:
                    print("                      any thing you write will be appedded after pressing enter")
                    content = input()
                    fw.write(content) 
        else:
            print("file doesnot exists")
    
    @staticmethod
    def delete(file):
        if exists(file):
            os.remove(file)
            print("file deleted")
        else:
            print("file doesnot exisst!!")
            
