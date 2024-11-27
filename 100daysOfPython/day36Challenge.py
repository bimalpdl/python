names = []
while True:
    def main():
        fName = input("Enter your first name: ").strip().capitalize()
        lName = input("Enter your last name: ").strip().capitalize()
        fullName = f"{fName} {lName}"
        if fullName not in names:
            names.append(fullName)
            print("Current list items are: \n", names)
        else:
            print(f"{fullName} already exist in the list.")
        print(fullName)

    main()
