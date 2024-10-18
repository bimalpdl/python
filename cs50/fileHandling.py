# conventional way to get user input but it doesn't store the entries permanently.
names = []
inputs = int(input("Enter number of entries: "))
print("Enter names: ")
for _ in range(inputs):
  names.append(input("> "))
print(names)

# The open() function allows you to open a file such that you can read from it or write to it.
# open("fileName", "openMode")
# eg: file1 = open("file.txt", "w")
# w = write mode (overrides the previous values), a = appends the values, r = open file in read mode.
name = input("Enter your name: ")
file = open("file.txt", "a")    # opens the file in append mode, creates a new file if don't already exist.
file.write(name)   # write the content in the file without whitespace.
file.close()

name1 = input("Enter Your Full Name: ")
file1 = open("file1.txt", "a")
file1.write(f"{name1}\n")
file1.close()


# The keyword 'with' allows you to automate the closing of a file.
name2 = input("Enter Your Favorite Color: ")
with open("text", "w") as file:
    file.write(f"{name2}")
