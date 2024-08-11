num = int(input("Enter a number: "))
i = 1
while i <=10:
    print(f"{num} x {i} = {num*i}")
    i += 1
    print("While loop terminated.")


# infinite loops:
"""
num = 14

while num > 10:    # the test condition is always true so it will create an infinite loop.
    print("Hello, There!!")


while True:     # test condition is always true so it will create infinite loop
    print("Hello,world!!)

"""


# terminating the loop using 'break'
num = int(input("Enter a number: "))
i = 1
while True:
        print(f"{num} x {i} = {num * i}")
        i += 1
        if i == 11:
            print("Loop terminated by break.")
            break


# a while loop can have an optional else clause - that is executed once the loop condition is False
num = 0
while num <= 5:
    print(f"The value of num is {num}")
    num += 1
else:
    print("The loop condition is false, and this is else statement of while loop.")
