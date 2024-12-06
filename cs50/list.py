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
    print(f"{i+1} : {students[i]}")
