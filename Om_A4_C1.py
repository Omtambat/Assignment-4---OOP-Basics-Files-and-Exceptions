# YourName_A4_C.py

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def set_marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid marks! Marks must be between 0 and 100.")

    def get_marks(self):
        return self.__marks


# Create three students
student1 = Student("Om", 85)
student2 = Student("Rahul", 90)
student3 = Student("Amit", 78)

# Write students to file
with open("students.txt", "w") as file:
    file.write(student1.name + "," + str(student1.get_marks()) + "\n")
    file.write(student2.name + "," + str(student2.get_marks()) + "\n")
    file.write(student3.name + "," + str(student3.get_marks()) + "\n")

# Read the same file and print each line
with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())