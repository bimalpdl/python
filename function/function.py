# function without any parameters or return statements
def greet():
    print("Hello there, how are you doing?")

greet()


# function with parameter
def greet1(name):    # name is parameter
    print("Hello,", name, ", how are you doing?")
greet1("Bimal")   # Bimal is argument

# actual value that is passed to the function is argument


# function with return statement
def find_square(num1):
    return num1 * num1
print("Square of 5 is:",find_square(5))

# function with default parameter
def greet2(name,message = "Hello"):
    print(message, name)

greet2("Bimal")
print("Rohini","Have a good day!")


# python keyword argument:
def greet3(lastName, firstName):
    print("First name:",firstName, "Last name :", lastName)

greet3(lastName = "Paudel", firstName = "Bimal")
