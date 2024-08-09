# implicit type conversion
# Python promotes the conversion of the lower data type (integer) to the higher data type (float) to avoid data loss.
num = 189 # int type
num1 = 12.38    # float type
result = num + num1    # converts the int to float in result
print(f"The sum of {num} and {num1} is {result} and type of result is {type(result)}")


# explicit type conversion aka typecasting
# We get TypeError, if we try to add str and int. For example, '12' + 23. Python is not able to use Implicit Conversion in such conditions.
# We use the built-in functions like int(), float(), str(), etc to perform explicit type conversion.


num = 167
numStr = '123'
# print(num + numStr)     // this will throw an error since we're  trying to add 'int' to 'str'
print(f"Type of 'numStr' before conversion is: {type(numStr)}")
# explicit type conversion
numStrToInt = int(numStr)
print(f"Type of 'numStr' after conversion is: {type(numStrToInt)}")
print(num + numStrToInt)

# also can be done directly as:
print(f"{num} + {numStr} = {num + int(numStr)}")
