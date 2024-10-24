# we need to open a file first to perform any operations on it—we use the open() function to do so.
# file = open("fileName", "openMode")  
# by default, open mode is read(r) and text(t) mode.
# other available modes are: w = write, a = append, x = exclusive creation, t = text, b = binary, + = both read and write.

# to open file in both read, write and binary mode:
# file = open("fileName", "+b")

# opening file using full path(absolute path):
filePath = "/home/bimal/Python/cs50/file.txt"
file = open(filePath, "a")
text = "Hello there! How are you doing?"
file.write(text)
file.close()

with open(filePath) as file:    # using 'with' will automatically closes the file without having to manually close it using close() function.
    for line in file:
        print(line)

file = open("/home/bimal/Python/100daysOfPython/day35.py")   # also can use this method to open file using absolute path.
content = file.read()
print(content)


# to write content in file:
file = open("testFile", "w") # note that when we open file in 'write' mode, new file will be created if the file doesn't exists and is overridden with new contents if file contains sth.
text = "Hello there! This is some random text example."
file.write(text)
file.close()

with open("testFile", "w") as file:
    file.write("The previous texts are overwritten.")

with open("testFile") as file:
    for line in file:
        print(line)


# If an exception occurs while working with a file, the code exists without closing the file. Hence, it's a good practice to use the try...finally block.
try: 
    file = open("testFile")
    content = file.read()
    print(content)

finally:
    print("File closed successfully.")
    file.close()
# Here, the finally block is always executed, so we have kept the close() function inside it. This ensures that the file will always be closed. 





