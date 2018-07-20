import os
import datetime as dt 

def exists(file):
    return os.path.isfile(file)

def tdate():
    return str(dt.date.today())

