# 'strip()' method removes whitespace from the beginning and the end of the string

name = input("Enter your name: ")
name = name.strip()    
print(f"Hello, {name}!")



# title() method capitalize the first letter of each word
# eg: input=> bimal paudel ; op=> Bimal Paudel
fname = input("Enter your full name in all lowercase: ")
fname = fname.strip().title() 
# Remove whitespace from the str and capitalize the first letter of each word
# we can even do: fname = input("Enter full name").strip().title()
print(f"Hello, {fname}!")


# You can run functions on (inside another) functions. The inner function is run first, and then the outer one is run. First, the input function is run. Then, the float function.
x = float(input("Value of x?: "))
y = float(input("Value of y?: "))
z = x / y 
# Create a rounded result
a = round(x / y)
b = round(x / y, 3)  # rounds upto 3 decimal points
print(f"{x} / {y} = {z}")
print(f"After applying round() function: {x} / {y} = {a}")
print(f"After applying round(x/y,3) function: {x} / {y} = {b}")

# Print the result
print(f"{z:.2f}")

# Print the formatted result
m = 10000
print(f"{m:,}")

