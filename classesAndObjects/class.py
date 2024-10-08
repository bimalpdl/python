# class with only attribute / property
class Person:
    name = ""
    age = 0 # 
p1 = Person()  # objectName = className()
p1.name =  "Bimal"
p1.age = 22
print(f"Name:{p1.name} Age:{p1.age}")

# class with attributes as well as method
class Square:
    length = 0.0
    breadth = 0.0

    def calcArea(self):    # first parameter of method inside class must be 'self'
        # 'self' specifies the current object
        print("Area of the square is:", self.length * self.breadth)

s1 = Square()
s1.length = 15.5
s1.breadth = 12.5
s1.calcArea()

# class constructor
class Rectangle:
    # constructor is defined as '__init__' function

    def __init__(self, length = 0.0, breadth = 0.0):
        self.length = length
        self.breadth = breadth
        print(f"Length of rectangle is: {self.length} and Breadth is: {self.breadth}.")

r1 = Rectangle(25,16)
print("Area of the rectangle is:", 2*(r1.length * r1.breadth))












