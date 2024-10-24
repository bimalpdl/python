# Python provides a dedicated csv module to work with csv files.
# The module includes various methods to perform different operations.
# The csv module provides the csv.reader() function to read a CSV file.
import csv
with open("people.csv") as file:
    contents = csv.reader(file)

    for row in contents:
        print(row)


# The csv.DictReader() class can be used to read the CSV file into a dictionary, offering a more user-friendly and accessible method. 
print()
with open("people.csv") as file:
    contents = csv.DictReader(file)

    for row in contents:
        print(row)

# we used csv.DictReader(file), which treats the first row of the CSV file as column headers and each subsequent row as a data record.


# The csv module provides the csv.writer() function to write to a CSV file.
with open("people1.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Name", "Age", "Sex"])
    writer.writerow([1, "Bimal", 22, "Male"])
    writer.writerow([2, "Nirmal", 21, "Male"])
    writer.writerow([3, "Rohini", 31, "Female"])

with open("people1.csv") as file:
    contents = csv.reader(file)
    for row in contents:
        print(row)





























