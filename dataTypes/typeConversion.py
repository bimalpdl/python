# Python supports integers, floating-point numbers and complex numbers.
# They are defined as int, float, and complex classes in Python.
# We can use the type() function to know which class a variable or a value belongs to.

num, num1, num2 = 521, 152.02 , 87+5j      # to initialize the different variables with different values at once.
print(f"Data type of {num} is, {type(num)}")
print(f"Data type of {num1} is, {type(num1)}")
print(f"Data type of {num2} is, {type(num2)}")


# we can declare numbers with different number systems ie. Binary, Octal and Hexadecimal
# 0b or 0B prefix is used to represent the Binary number
print(0B001000)    # here,0B is prefix and 001000 represents decimal 8 so 8 is printed on the console

# 0o or 0O prefix is used to represtn the Octal number
print(0o135)   # 0o is prefix and 135 is octal number, which is 93 in decimal

# 0x or 0X prefix is used to represent the Hexadecimal number
print(0xAB + 12)        # 0x is prefix for hexadecimal and AB+12 is hexadecimal number, which is 183 in decimal


# typeConversion in Python
# Python uses both implicit and explicit type conversion
# Operations like addition, subtraction convert integers to float implicitly (automatically), if one of the operands is float.
num2 = 5
num4 = 21.05
num5 = "152"
print(f"Data type of num2 is {type(num2)} and data type of num4 is {type(num4)}")
print(f"The sum of {num2} and {num4} is {num2 + num4}")
print("After sum the data type of the result is float")

# We can also use built-in functions like int(), float() and complex() to convert between types explicitly.
#  These functions can even convert from strings.

print(f"Type conversion of num2 from int to float {float(num2)}")
print(f"Type conversion of num4 from float to int {int(num4)}")
print(f"Type conversion of string and int to float : {float(num5) + float(num2)}")
