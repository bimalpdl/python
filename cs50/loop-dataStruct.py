def main():
    display(getInput())

def display(n):
    print(f"Printing the string {n} times: ")
    for _ in range(n):
        '''If we are never going to use the value of variable we can simply use underscore _ instead of any variable like i '''
        print("Oh, hello there!")

def getInput():
    while True:
        x = int(input("Enter a number: "))
        if x > 0:
            return x
        

main()


# list with loop
students = ["Bimal", "Rohini", "Matrika", "Nirmal"]
print("Elements in the list are: ")
for i in range(len(students)):
    """ to print position as well as elements in students list """
    print(f"{i+1} : {students[i]}")



# dictionaries 
students = {
        "Bimal" : "Myself",
        "Rohini" : "Didey",
        "Nirmal" : "Brother",
        "Matrika" : "Sister",}

for student in students:
    print(student)    # only prints the keys

for student in students:
    print(f"{student} : {students[student]}")    # prints both keys and values


for student in students:
    print(student, students[student], sep=" -> ")    # separates keys and values with '->'


details = [
        {"name" : "Bimal", "address" : "Kadaghari", "age": 22, "child":None},
        {"name" : "Nirmal", "address" : "Kadaghari", "age": 21, "child":None},
        {"name" : "Rohini", "address" : "Mulpani", "age": 31, "child": "Shreewi"}
        ]

for detail in details:
    print(detail["name"], detail["address"], detail["age"], detail["child"], sep = " : ")  # prints only values
print()


for detail in details:
   print(detail)
