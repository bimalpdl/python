# intro to dictionary
name: str = input("Enter your name: ")
email: str = input("Enter your email: ")
phoneNum: str = input("Enter your phone number: ")  # we are intentionally making the phoneNumber string because won't perform any mathematical operations on those number and if 0 appeared in the beginning, the interpreter won't messup with it.
address: str = input("Enter your address: ")
age: int = int(input("Enter your age: "))
details = {"name": name, "age": age, "email": email, "phoneNum": phoneNum, "address": address}
print()
print(f"""Name: {details["name"]}""") # we're using triple quotes with f-string so that we don't get error using double quote inside dictionary key declaration.
# print(f"Name: {details["name"]}")      // this will throw an error
print(f"Age: {details['age']}")
print(f"Email: {details['email']}")
print(f"Address: {details['address']}")
print(f"Phone Number: {details['phoneNum']}")

