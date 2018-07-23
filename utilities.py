import os
import datetime as dt 

def exists(file):
    '''checks if a file exists (in docs folder)

    input: filename'''
    return os.path.isfile(file)

def tdate():
    '''Gives current date in string form'''
    return str(dt.date.today())

