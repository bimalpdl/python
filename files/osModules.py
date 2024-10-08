import os
print("Current working directory is: ", os.getcwd())  # getcwd() is equivalent to 'pwd' in python




os.chdir("/home/bimal/Python/")   # chdir() method is used to change the current working directory. It is equivalent to 'cd'.
print("Now changed to:", os.getcwd())


os.mkdir("testDir")   # used to make a directory

print(os.listdir("/home/"))  # list files and folders in specified path location


os.rename("testDir","new_testDir") # renames file or directory ("oldName","newName")

os.remove("fileName")    # used to remove specified file

os.rmdir("emptyDirName")    # used to delete specified empty directory

# to delete a non-empty directory, use 'rmtree("folderName")' which is defined inside 'shutil' module(we need to import 'shutil' module first. 




