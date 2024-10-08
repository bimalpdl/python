# Exceptions abnormally terminate the execution of a program.
# The try...except block is used to handle exceptions in Python. 
# we place the code that might generate an exception inside the try block. Every try block is followed by an except block.
# When an exception occurs, it is caught by the except block. The except block cannot be used without the try block.
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print(numerator, "/", denominator, "=", result)
except:
    print("Denominator can't be zero!")
# If none of the statements in the try block generates an exception, the except block is skipped



# For each try block, there can be zero or more except blocks. Multiple except blocks allow us to handle each exception differently.

# The argument type of each except block indicates the type of exception that can be handled by it.


try:
    evenNumbers = [2,4,6,8]
    print(evenNumbers[5])
except ZeroDivisionError:
    print("Can't divide by zero!")
except IndexError:
    print("You're trying to access the index out of the bound!") 
# we are trying to access a value to the index 5. Hence, IndexError exception occurs.
# When the IndexError exception occurs in the try block,
   #   The ZeroDivisionError exception is skipped.
   #    The set of code inside the IndexError exception is executed.




# In some situations, we might want to run a certain block of code if the code block inside try runs without any errors.
# For these cases, you can use the optional else keyword with the try statement.
try:
    number = int(input("Enter a number: "))
    assert number % 2 == 0
    # The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.
except:
    print(f"{number} is not an even number!")
else:
    try:
        reciprocal = 1 / number
        print(reciprocal)
    except:
        print("Can't divide by zero!")
finally:
    print("Finally block is always executed!")




# In Python, the finally block is always executed no matter whether there is an exception or not.
# The finally block is optional. And, for each try block, there can be only one finally block.









