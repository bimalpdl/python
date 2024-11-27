totalAge = 90 * 365
currentAge = int(input("Enter your current age: "))
currentAgeInDays = currentAge * 365
remainingDays = totalAge - currentAgeInDays
remainingWeeks = remainingDays // 7
remainingMonths = remainingDays // 30
print(f"You have {remainingDays} days, {remainingWeeks} weeks and {round(remainingMonths)} months left.")
print("May you rest in peace soon!")
