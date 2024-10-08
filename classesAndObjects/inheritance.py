# Parent class with its attributes and method
class Person():
    name = ""
    age = 0

    def greet(self):
        print("Hello, I am method of parent class.")

# child class derived from parent class 'Person'
class SWE(Person):      # childClass(parentClass)

    def addDetails(self):
        print(f"Name: {self.name}, Age: {self.age}")   # accessing the attributes of parent class.

bimal = SWE()
bimal.name = "Bimal"
bimal.age = 22


bimal.greet()    # accessing the method of parent class using the object of child class.
bimal.addDetails()
