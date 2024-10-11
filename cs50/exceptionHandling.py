def main():
    x = getInput()
    y = secondNumber()
    z = thirdNumber("Enter one more number: ")
    print(f"The value of x is {x}.")
    print(f"The value of y is {y}.")
    print(f"The value of z is {z}.")

def getInput():
  while True:
    try:
      return int(input("Enter a number: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")


def secondNumber():
  while True:
    try:
        return int(input("Enter another number: "))
    except ValueError:
        pass    # reprompts user input without any error message.


def thirdNumber(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
main()
