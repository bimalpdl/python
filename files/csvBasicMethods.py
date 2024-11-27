import csv
with open("people1.csv") as file:
    content = csv.DictReader(file)
    for row in content:
        print(row)


with open("people2.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Name", "Age", "Sex"])
    writer.writerow([1, "Bimal", 22, "Male"])
    writer.writerow([2, "Rohini", 31, "Female"])
    writer.writerow([3, "Nirmal", 21, "Male"])

with open("people2.csv") as file:
    content = csv.DictReader(file)
     
    for row in content:
        print(row)