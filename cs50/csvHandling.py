with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"Name: {row[0]}, Address: {row[1]}")


"""Notice that rstrip removes the end of each line in our CSV file. split tells the compiler where to find the end of each of our values in our CSV file.
row[0] is the first element in each line of our CSV file. row[1] is the second element in each line in our CSV file."""
print("\n\n")

with open("students.csv") as file:
    for line in file:
        name, address = line.rstrip().split(",")
        print(f"Name: {name}, Address: {address}")

"""Notice that the split function actually returns two values: The one before the comma and the one after the comma.
 Accordingly, we can rely upon that functionality to assign two variables at once instead of one!"""
print("\n\n")
print("CSV sorted according to student names: ")
students = []
with open("students.csv") as file:
    for line in file:
        name, address = line.rstrip().split(",")
        students.append(f"Name: {name}, Address: {address}")

for student in sorted(students):
    print(student)




print()
# CSV to dictionary
students = []
with open("students.csv") as file:
    for line in file:
        name, address = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["address"] = address
        students.append(student)

for student in students:
    print(f"Name: {student["name"]}, Address: {student["address"]}")

print()
students = []
with open("students.csv") as file:
    for line in file:
        name, address = line.rstrip().split(",")
        student = {"name": name, "address": address}
        students.append(student)

for student in students:
    print(f"Name: {student['name']}, Address: {student['address']}")
