# this is single line comment
"""
this is multi-line comment
"""

print("Hello, There")
# input() is used to take user input and can be directly assigned to the variable
# we can also pass argument to promt for input
name = input("Enter your name: ")    # prompts user to enter their name and assigns it to the variable 'name'
print("Hello, " + name)
print("Hello,", name)     # this automatically adds a whitespace before the passed argument
print(f"Hello, {name}")    # this is the most preferred method



# strip() is used to remove whitespace from beginning and end of the string(if exists) but doesn't remove white space inbetween words
name = name.strip()     # i/p => '     rohini paudel     '    o/p=>'rohini paudel'
print("Hello, " + name)
# capitalize() capitalizes the first letter of first word of given string(str)
name = name.capitalize()  # capitalizes the first letter of first word
# eg : i/p 'bimal paudel'  o/p => 'Bimal paudel'
print("Hello, " + name)
#title()  => capitalizes the first letter of each word in the given string
name = name.title()
# eg : i/p 'bimal paudel'  o/p => 'Bimal Paudel'
print("Hello, " + name)


# we can also use all methods at once:
address = input("Enter your address: ").strip().capitalize().title()
print(f"Is {address} really your addres? ")
