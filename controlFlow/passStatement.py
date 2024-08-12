# pass statement is a null statement which can be used as a placeholder for future code
# it is used as place holder for if statement, class or function
# which are declared but nothing is defined within them and we plan to define them in future
# If we declare a funcion/class/if statement wihtout any definition the interpreter will throw an error
# To avoid that we use 'pass' keyword
number = 10
if number >= 10:  # if statement is declared but noting is defined inside the if block
    pass    # nothing happens when the pass is executed. It results in no operation (NOP).
    # if we don't declare 'pass', the interpreter will thrown an error saying empty if/function/class can't be declared
print("Hello, there!")

# The difference between a comment and a pass statement in Python is that
# while the interpreter ignores a comment entirely, pass is not ignored.

def greet():
    pass

print("Pass statement from greet() function.")

class Person:
    pass
print("Pass statement from Person class")
