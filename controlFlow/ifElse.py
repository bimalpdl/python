number = int(input("Enter a number: "))
# Python uses indentation to define a block of code, such as the body of an if/else statement.
if number > 0:
    print("{} is greater than zero.".format(number))
elif number < 0:
    print(f"{number} is less than zero.")
else:
    print(number," is equal to zero.")

print("Hello from forever-printing line.")

# nested if/else

num = int(input("Enter a number: "))
if num > 0:
    print(f"{num} is a positive number.")
    if num % 2 == 0 and num % 3 ==0:
        print("{} is divisible by both 2 and 3".format(num))
    elif num % 2 == 0:
        print(f"{num} is multiple of 2.")
    elif num % 3 == 0:
        print(f"{num} is multiple of 3.")
    else:
        print(f"{num} is neither multiple of 2, nor of 3.")
else:
    print(f"{num} is a negative number.")
