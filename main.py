from file_class import file
import sys

def runner():
    print("create |   open   |   rename    |    delete ")
    response = input().lower()
    args = response.split(" ")
    if args[0]== "create":
        if len(args) == 1: 
            file()
        elif len(args) == 2:
            file(args[1])

    elif len(args) == 2 and  args[0] == "delete":
        file.delete(args[1])
    elif len(args) == 3 and args[0] == "rename":
        file.rename(args[1], args[2])
    elif len(args) == 2 and args[0] == "open":
        file.open(args[1])
    else:
        print("INvalid argument provided!!")
        runner()

    print("                      press q to quit other to restart!              ")
    prompt = input().lower()
    if prompt == "q":
        sys.exit()
    else:
        runner()

if __name__ == "__main__":
    runner()
