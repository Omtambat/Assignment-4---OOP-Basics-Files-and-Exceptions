import csv

# Three students
students = [
    ["Om", 85],
    ["Rahul", 90],
    ["Aryan", 78]
]

# Write students to CSV file
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Header row
    writer.writerow(["name", "marks"])

    # Student data
    writer.writerows(students)

# Read students.csv
with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)