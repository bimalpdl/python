# print(object= separator= end= file= flush=)   // print() function supports these five parameters
# the parameter we generally pass is 'object' parameter
# we can modify each of these parameter according to our use-cases

# end parameter in print()
str1 = "Hello, There!"
str2 = "How are you doing?"
print(str1, end=' ')    # default value of end parameter is '\n' so it prits the newline after printing
print(str2)    # but this will be printed in same line


# sep parameter in print()
print("Hello, there!", "I am", 22, "years old" ,sep='.')   #  the output includes items separated by '.' not by whitespace
# the above statement will separates items by '.' instead of whitespace ' ' (which is it's default behaviour)



# print concatenated string using '+' operator
print(str1 + str2)     # this won't add whitespace inbetween concatenated strings

# output formatting    // done using str.format()
print("The value in str1 is: {}\nAnd the value in str2 is: {}".format(str1,str2))

x = 10
y = 29
z = x + y
print("The sum of {} and {} is {}.".format(x,y,z))
