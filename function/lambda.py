# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# anonymous function (lambda expression) to calculate the square of given number
square = lambda a: a*a   # assigning the anonymous function to a variable 'square' which is used to call it.
num = int(input("Enter a number to find its square: "))
print(square(num))


# function to evaluate 5x+6y

result = lambda x,y: 5*x + 6*y
print("Enter values of x and y to evaluate 5x+6y: ")
xValue = int(input("Enter value of x: "))
yValue = int(input("Enter value of y: "))
result1 = result(xValue,yValue)  # calling the function with variable name 'result' and assigning it to variable result1
print(result1)


# everything in python is an object so, we can pass a function as an argument in another function
list1 = [2,5,6,8,4,2,10,7,19,6]
print("Original list: ")
print(list1)
print("List after filtering only even numbers: ")
evenNumbers = list(filter(lambda a: a % 2 == 0, list1))
# first parameter in filter() function is return and second is passed parameter. In this case, list1 is passed as parameter and even numbers is returned by filter() function with the help of lambda funtion. We didn't assign anonymous function to any variable since it can directly return the value to filter function as an argument.
print(evenNumbers)

print("List after doubling the even numbers: ")
double = list(map(lambda a: a*2, evenNumbers))
print(double)

















