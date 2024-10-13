# f-strings

name = "Bimal"
age = "22"
sex = "male"
print("Hello, there! My name is {}, I am {} years old I am a {}".format(name, age, sex))


word = "Hello, my name is {name}, and I am {age} years old.".format(age=age, name = name)
" Note that here we are using format() in a variable instead of print() function."
""" using varName = varName allows us to change the order of occurance in format() function. 
ie. we can place age = age first and name = name second eventhough name occured first and age occured second in the given text. """
print(word)

for i in range(10):
    print("The number is: {count}".format(count = i))  # i is assigined to count local variable

# most elegant way of writing f-string is:
word1 = f"Hello, my name is {name} and I am {age} years old."
print(word1)

# we can use f-string with triple qoute format as follows:
word2 = f"""Hello, there! I am {name}.

I am {age} years old.
"""
print(word2)


for i in range(1, 30):
    print(f"Day {i: <3} of 100")   # {varname: <length}   used to align accorgint to specified length, here we've specified 3 length
""" <, >, ^ represents aligh left, aligh right and align center respectively."""
