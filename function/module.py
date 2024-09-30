# Module is a file that contains code to perform a specific task.
# A module may contain variables, functions, classes etc

import addition      # importing userdefined module (addition.py is imported as 'addition')
print(addition.add(10,15,5))    # add is a function defined inside addition.py(addition module)

# The Python standard library contains well over 200 modules. We can import a module according to our needs.
import math 
print("The value of Pi is:", math.pi)
print("The value of e is:", math.e)

# we can also import a module by renaming it.
import time as t 
print("Current time is:", t.ctime())
print("Current time in UNIX time system is:", t.time())

# Note that the name time is not recognized in our scope.
# Hence, time.time() is invalid, and t.time() is the correct implementation.

# We can import specific names from a module without importing the module as a whole.
from math import pi # import only pi from math module
print(pi)   # IDK why we didn't use math.pi may be because we only have imported pi or sth

# import all names from the standard module math
from math import *
print("Value of e is:", math.e)
# Importing everything with the asterisk (*) symbol is not a good programming practice. 
# This can lead to duplicate definitions for an identifier. 



# we can use the dir() built-in function to list all the function names in a module.
print(dir(addition))
print()

# All the names defined in our current namespace can be found out using the dir() function without any arguments.
print(dir())

