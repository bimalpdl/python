def main():

    # Output using our own function
    name = input("What's your name? ")
    hello(name)

    # Output without passing the expected arguments
    hello()


# Create our own function
def hello(to="world"):
    print("hello,", to)

main()


def parent():
    x = int(input("Enter a number: "))
    print(f"Square of {x} is {square(x)}") # calling function inside print() function

def square(num):
    return num * num

parent()
