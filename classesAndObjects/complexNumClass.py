class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def displayValues(self):
        print(self.real, "+", self.imag,"i")

    def sum(self, number):
        real = self.real + number.real
        imag = self.imag + number.imag
        result = Complex(real, imag)  # result is an object of Complex class
        return result

n1 = Complex(10,5)
n2 = Complex(7,-2)
n1.displayValues()
n2.displayValues()

result = n1.sum(n2)
print("Result: ", result.real, "+", result.imag,"i")
