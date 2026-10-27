import json

# List of student dictionaries
students = [
    {"name": "Om", "marks": 85, "grade": "A"},
    {"name": "Rahul", "marks": 90, "grade": "A+"},
    {"name": "Sai", "marks": 78, "grade": "B"}
]

# Write students to JSON file
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

# Read students.json
with open("students.json", "r") as file:
    data = json.load(file)

# Print name and grade
for student in data:
    print("Name:", student["name"], "Grade:", student["grade"])