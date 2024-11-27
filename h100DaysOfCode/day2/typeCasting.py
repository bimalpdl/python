def main():
    totalAmount =  float(input("Enter the bill amount: "))
    tipPercentage = int(input("Enter tip percentace: "))
    totalAmount += totalAmount* (tipPercentage / 100)
    perPerson = int(input("Enter number of people to split the bill: "))
    finalAmount = totalAmount / perPerson
    print("The total bill amount is: ", totalAmount)
    print(f"Final amount per person is: {finalAmount}")






if __name__ == "__main__":
    main()
