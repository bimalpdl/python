listOfShame = []

def prettyPrint():
    for row in listOfShame:
        for column in row:
            print(f"{column:^10}", end = " | ")
        print()

def deleteRecord():
# we can't delete the individual item / single item from list of list (table)
# so we need to delete the entire row

    name = input("Enter the name to delete: ")
    for row in listOfShame:
        if name in row:
            listOfShame.remove(row)

while True:
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    gender = input("Enter your gender: ")
    row = [name, age, gender]    # 
    listOfShame.append(row)
    removeItem = input("Do you want to delete any item?: ")
    if removeItem.strip().lower()[0]  == "y":
        deleteRecord()
    terminate = input("Exit? y/n: ")
    print("Current list items are: ")
    prettyPrint()
    if terminate.strip().lower()[0] == "y":
        break






