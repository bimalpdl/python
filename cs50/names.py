name = input("Enter your name: ")
with open("names.txt", "a") as file:
    file.write(f"{name}\n")


with open("names.txt", "r") as file:
    lines = file.readlines()

    for line in lines:
        print("Hello,", line.rstrip(),"!")   
        # The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.

"""
concise way to implement read operation is: 
with open("names.txt", "r") as file:
    for line in file:
    print("Hello, ", line.rstrip(), "!")

    we can read directly from the file rather than assigning to to lines variable.
"""

# to sort the names first and greet:
names = []
with open("names.txt") as file:
    for line in file:
        # we can also sort the file directly as => for line in sorted(file):
        names.append(line.rstrip())    # reads the file contents and adds the contents to the list 'names'

for name in sorted(names):   # sortes the list 'names' before printing
    print(f"Hello, {name}!")

