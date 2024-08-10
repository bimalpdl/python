# Python allows you to assign values to multiple variables in one line
x,y,z = "Rohini", "Bimal", "Nirmal"   # x = Rohini, y = Bimal , z = Nirmal
print(x,y,z)


# you can assign the same value to multiple variables in one line
x = y = z = "Rohini"    # initialized all (x,y,z ) by value "Rohini"
print(x,y,z)
# using comma(,) to separate variables in print statement will automatically add a whitespace to separate the variables.

# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables.
# This is called unpacking.
names = ["Bimal", "is", "awesome"]
x,y,z = names
# using '+' to concatenate string won't add white space to separate the variables in print() statement and we need to specify white space before/after string manually.
print("Using '+' to concatenate the string: " + x + y + z)
names = ["Bimal ", "is ", "awesome "]
x,y,z = names
print(x+y+z)


# if we try to print integer and string variables using '+' operator, the interpreter will throw an error
# to print int and str variables comma(,) is used to separate the variable
x = 15
y = "Didey"
# print(x + y)      // this will give an error
print(x,y)



# local and global variables in python:
# we need to use 'global' keyword to access the global variable inside a function (if there is a variable containg same variable name)

name = "Bimal"

def greet():
    print("Hello,",name)

greet()


name = "easy"
def didey():
    name = "supportive"
    print("Pyton is",name)  # prints 'Python is supportive' using local variable
didey()
print("Python is", name)    # prints 'Python is easy' using global variable


# accessing and modifying global variable inside the function

x = "awesome"

def myFunc():
    global x     # to access global variable
    x = "fantastic"    # changes the value of global variable 'x' from 'awesome' to 'fantastic'

myFunc()
print("Bimal is", x)
