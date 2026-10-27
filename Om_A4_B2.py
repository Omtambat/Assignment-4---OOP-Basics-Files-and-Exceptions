MY_NAME = "Om Tambat"


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def set_marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Marks must be between 0 and 100.")

    def get_marks(self):
        return self.__marks

    def __str__(self):
        return f"Name: {self.name}, Marks: {self.__marks}"


# Create three Student objects
student1 = Student(MY_NAME, 90)
student2 = Student("Sai", 70)
student3 = Student("Aryan", 81)

# Print all three
print(student1)
print(student2)
print(student3)