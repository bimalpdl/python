# The Python range() function generates a sequence of numbers.
# By default, the sequence starts at 0, increments by 1, and stops before the specified number.
for i in range(5):       # create a sequence form 0 to 4
    print(f"{i}.Hello, There!!")


# range() syntax=> range(start,stop,step)
# the start and step arguments are optional
# range() Return Value   => The range() function returns an immutable sequence of numbers.

# range() stop
num = range(5)    # stops after 5 itereations (by default, 0 to 5)
print(list(num))

# print(num)    // this will print ' range(0,5) '


# range(start,stop)
num1 = range(-2,5)     # ranges from -2 to 4
print(list(num1))

num2 = range(5,10)
print(list(num2))

# creates an empty sequence
numbers = range(4, 2)
print(list(numbers))    # []


# range (start, stop, step)
# create a sequence from 2 to 10 with increment of 3
num = range(2,12,3)
print(list(num))   # [2, 5, 8, 11]


# create a sequence from 4 to -3 with increment of -2
num = range (4, -3, -2)    # negative step(increment) is used to loop backward
print(list(num))    # [4, 2, 0, -2]


num = range(0, 5, 1)    # equivalent to range(5)
print(list(num))     # [0, 1, 2, 3, 4]
