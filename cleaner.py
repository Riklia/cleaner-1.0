import os
import shutil

def printAllFiles(direct):
    for file in os.listdir(direct):
        print(file)
            
def printAllExtF(direct, ext):
    for file in os.listdir(direct):
        if file.endswith("."+ext):
            print(file)
            
def printFilesWithSize(direct):
    print("Example >= 50mb (you can enter size in b, kb, mb and gb")
    sizeStr = input()
    size = float(''.join(x for x in sizeStr if x.isdigit()))
    if sizeStr[-2:] == "kb":
        div = 1000
    elif sizeStr[-2:] == "mb":
        div = 10**6
    elif sizeStr[-2:] == "gb":
        div = 10**9
    else:
        print("Error!")
        return 0
    print(sizeStr[-2:])
    if ">=" in sizeStr:
        for file in os.listdir(direct):
            if os.path.getsize(os.path.join(direct, file))/div >= size:
                print(file)
    elif "<=" in sizeStr:
        for file in os.listdir(direct):
            if os.path.getsize(file)/div <= size:
                print(file)    
    
def clearDir(direct):
    print("Enter \"Clean all\" for deleting all files from this directory")
    string = input()
    if string == "Clean all":
        for file in os.listdir(direct):
            os.remove(os.path.join(direct, file))
            print("Cleaned!")
        
def removeDir(direct):
    print(direct)
    print("Enter \"Remove this directory\" for deleting this directory")
    string = input()
    if string == "Remove this directory":
        shutil.rmtree(direct)
        print("The directory has been removed!")
    
def remFile(direct):
    print("Current directory:", direct)
    file = input("Enter file (in a current directory): ")
    os.remove(os.path.join(direct, file))
    
def remAllExtF(direct, ext):
    for file in os.listdir(direct):
        if file.endswith("."+ext):
            os.remove(os.path.join(direct, file))

def moveTo(direct):
    file = input("Enter a file (only if this file in the current directory): ")
    newDirect = input("Enter a new directory (full path or with +path if this folder in the current directory): ")
    try:
        if newDirect[0] == "+":
            if os.path.isfile(os.path.join(direct, newDirect[1:], file)) == False:
                os.replace(os.path.join(direct, file), os.path.join(direct, newDirect[1:], file))
            else:
                print("File", file, " is already in a destination directory")
        else:
            if os.path.isfile(os.path.join(newDirect, file)) == False:
                os.replace(os.path.join(direct, file), os.path.join(newDirect, file))
            else:
                print("File", file, "is already in a destination directory")
    except FileNotFoundError:        
        print("Cannot find file destination directory")       

def moveFromTo():
    file = input("Enter a full file path: ")
    newDirect = input("Enter a full path of a new directory: ")
    try:
        if os.path.isfile(os.path.join(newDirect, os.path.basename(file))) == False:
            os.replace(file, os.path.join(newDirect, os.path.basename(file)))
        else:
            print("File", file, "is already in a destination directory")
    except FileNotFoundError:        
        print("Cannot find directory or file")   
        
def change():
    newDir = input("Enter path of a new directory:")
    while os.path.isdir(newDir) == False:
        newDir = input("Error. Enter path of a new directory:")
    return newDir

def menu(direct):
    print(direct)
    choice = input("Enter -help for calling help menu\nEnter an action: ")
    while choice != "-exit":
        if choice == "-printAll":
            printAllFiles(direct)
        elif "-printAll+" in choice:
            printAllExtF(direct, choice[10:])
        elif choice == "-printAllWithSize":
            printFilesWithSize(direct)
        elif choice == "-remFile":
            remFile(direct)
        elif "-remFile+" in choice:
            remAllExtF(direct, choice[9:])
        elif choice == "-cleanDir":
            clearDir(direct)
        elif choice == "-removeDir":
            removeDir(direct)
        elif choice == "-moveTo":
           moveTo(direct)
        elif choice == "-moveFromTo":
            moveFromTo()
        elif choice == "-change":
            direct = input("Enter path of a new directory:")
        elif choice == "-where":
            print("Current directory: ", direct)            
        elif choice == "-help":
            print("""Enter:\n-printAll - for printing all files in your directory"\n
            -printAll+ext - for printing all files with specific extension\n
            -printAllWithSize - for printing all files with size >= <= than given
            -clearDir - for deleting all files in your directory\n
            -removeDir - for removing a current directory (with all the files contained in it)\n
            -remFile - for removing file in directory\n
            -remFile+ext - for removing all files with specific extension\n
            -moveTo - for moving file to the new directory
            -change - for changing a current directory\n
            -cleanEmpty - for removing all empty folders\n
            -where - for printing a current directory\n
            -help - for printing help\n
            -exit - for exit""")
        else:
            print("Try again")
        choice = input("Enter an action: ")
    
            
def main():
    print("Cleaner started")
    directory = input("Enter the path of your directory: ")
    while os.path.isdir(directory) == False:
        directory = input("This directory doesn't exist. Enter the path of your directory: ")
    menu(directory)
    
main()