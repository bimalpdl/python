weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
print(f"Your BMI is {round(weight/(height**2),2)}")
