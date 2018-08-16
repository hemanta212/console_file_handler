from file_class import file
import sys
import os

#moving to the dir from where this file is running.
curfile = os.path.realpath(__file__)
curdir = str(os.path.dirname(curfile))
#print(curdir)
#making a folder for storing files.
docs = curdir + "/docs/"
try:
    os.mkdir(docs) # if it is new environment
except FileExistsError:
    pass#changing current dir to that file
os.chdir(docs) 

def runner():
    '''Manages the flow of file_class.py functions '''

    print("create |   open   |   rename    |    delete ")
    try:
        response = input().lower()#prints a pretty menu & receives user choice
    except:
        print("Bad input!")
        runner()
    args = response.split(" ")#receiving user choice as lists
    #filtering first keyword and analyzing no of cmds in user response and assinging respective funcs 
    if args[0]== "create": 
        if len(args) == 1: 
            file()
        elif len(args) == 2 and args[1]!= " " and args[1] != "":
            file(args[1])
        else:
            file()

    elif len(args) == 2 and  args[0] == "delete":
        file.delete(args[1])
    elif len(args) == 3 and args[0] == "rename":
        file.rename(args[1], args[2])
    elif len(args) == 2 and args[0] == "open":
        file.open(args[1])
    else:
        print("Invalid argument provided!")
        runner()

    print("                      Press q to Quit other keys to Restart!              ")
    prompt = input().lower()
    try:
    	if prompt == "q":
        	sys.exit()
    except:
    	sys.exit()
    else:
        runner()

if __name__ == "__main__":
    runner()
