# conventional way to get user input but it doesn't store the entries permanently.
names = []
inputs = int(input("Enter number of entries: "))
print("Enter names: ")
for _ in range(inputs):
  names.append(input("> "))
# Notice that rstrip has the effect of removing the extraneous line break at the end of each line.
print(names.rstrip())

# The open() function allows you to open a file such that you can read from it or write to it.
# open("fileName", "openMode")
# eg: file1 = open("file.txt", "w")
# w = write mode (overrides the previous values), a = appends the values, r = open file in read mode.
# if we don't specify the openMode, by default, it opens the file in read mode:
# eg: with open("names.txt") as file
name = input("Enter your name: ")
file = open("file.txt", "a")    # opens the file in append mode, creates a new file if don't already exist.
file.write(name)   # write the content in the file without whitespace.
file.close()

name1 = input("Enter Your Full Name: ")
file= open("file.txt", "a")
file.write(f"{name1}\n")
file.close()


# The keyword 'with' allows you to automate the closing of a file.
colors = []
print("Enter Your Favorite Color: ")
with open("text", "w") as file:
    for _ in range (3):
        colors.append(input("> "))
        file.write(f"{colors}\n")


with open("text", "r") as file:
    lines = file.readlines()
print(type(lines))

with open("names.txt", "r") as file:
    lines  = file.readlines()

for line in lines:
    print("Hello, ", line.rstrip())

