from random import choice    # or import random
""" when we import only required function from the library, we don't need to specify the module name. ie.

we don't need to do random.choice() instead we do choice() directly as below."""

coin = choice(["Heads", "Tails", "Middle fingle"])    # choice(["Heads", "Tails", "Middle fingle"]) 
""" choice() function takes a list argument """
print(coin)


# random.randint(a,b) => This function will generate a random number between a and b.
from random import randint
num1, num2 = input("Enter two numbers separated by whitespace: ").split()
print(f"num1 = {type(num1)}, num2 = {type(num2)}")
number = randint(int(num1), int(num2))
print(number)



import random
names = ["Bimal", "Rohini", "Nirmal", "Matrika"]
random.shuffle(names)
" random.shuffle() function suffles a list into random order. "
print(names)


import statistics as stat 
print(stat.mean([100, 90]))
""" The mean function takes a list of values. This will print the average of these values """


# sys is a module that allows us to take arguments at the command line.
# argv is a function within the sys module that allows us to learn about what the user typed in at the command line.

import sys
print("Hello, My name is", sys.argv[1])   # try doing "python <fileName.py" <argument>; throws index out of range error if no argument is passed.

if len(sys.argv) < 2: # notice that 1 argument is given by the module itself
    print("Too few arguments.")
elif len(sys.argv) > 2:
    print("Too many arguments.")
else:
    print("Hello, my name is : ", sys.argv[1])

if len(sys.argv) < 2:
    sys.exit("Atleast one argumnet expected.")
# built-in function of sys called exit that allows us to exit the program if an error was introduced by the user.
elif len(sys.argv) > 2:
    sys.exit("Only one argument expected.")
print("My name is: ",sys.argv[1])















