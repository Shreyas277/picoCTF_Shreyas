import os
import sys

def list_files(directory):
    try:
        with os.scandir(directory) as entries:       # by taking path of directory and returns DirEntry objects for each of the file and directory present in the passed directory. DirEntry store name as well as path of this files.
            c=0
            for entry in entries:
                if entry.is_file():              
                    f=open(entry.path , 'r')         # using .path to open the file
                    data=f.read()
                    if "pico" in data:
                        print(f"File: {entry.name}:{c}")
                    else:
                        pass
                    f.close()
                elif entry.is_dir():
                    c+=1    # If c is being getting printed 1 for all the directories then it means all those directories are inside the directory with c not equal to 1 directory .
                    print(f"Directory: {entry.name}:{c}")
                    list_files(entry.path)    # Helps to find word in the files of subdirectories
    except FileNotFoundError:
        print(f"Directory not found: {directory}")
    except PermissionError:
        print(f"Permission denied: {directory}")

if __name__ == "__main__":
     directory = sys.argv[1]   # store the path of the directory which is the passed argument which will be */big-zip-files
     list_files(directory)
