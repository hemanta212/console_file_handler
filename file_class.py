import os
from utilities import tdate, exists


class file:
    '''A class use for creating file

    input:filename(optional) creates a file in docs dir.'''
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
        ''' Renames a file if it exists (in docs folder)

        input: old filename, new filename '''

        if exists(old):
            os.rename(old, new)
            print("file renamed")
        else:
            print("file doesnot exists in the folder")
            
    @staticmethod 
    def open(filename):
        ''' opens a file for appending if exists in docs folder

        input:existing filename'''
        if exists(filename):
            print("                               Status: EDITING!!  ||",filename,"  | ",len(filename),"||")
            with open(filename,'r') as fr:
                print(fr.read())
                print()
                with open(filename, "a") as fw:
                    print("                      any thing you write will be appedded after pressing enter")
                    content = input()
                    print(len(content))
                    if filename == tdate() + ".txt" or filename == ".txt":
                        if len(content) >=4:
                            word_list = content.split(" ")
                            new_file_name = word_list[0] +".txt" 
                            file.rename(filename,new_file_name)
                    fw.write(content) 
        else:
            print("file doesnot exists")
    
    @staticmethod
    def delete(file):
        '''Delete a file if exists (in docs folder)

        input:filename''' 
        if exists(file):
            os.remove(file)
            print("file deleted")
        else:
            print("file doesnot exisst!!")
            
