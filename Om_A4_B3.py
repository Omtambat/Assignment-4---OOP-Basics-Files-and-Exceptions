class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def set_marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
            print("Marks updated successfully.")
        else:
            print("Invalid marks! Marks must be between 0 and 100.")

    def get_marks(self):
        return self.__marks


# Create a student
student = Student("Om", 85)

print("Old marks:", student.get_marks())

# Try to set marks to 150
student.set_marks(150)

# Check marks after invalid update
print("Marks after trying to set 150:", student.get_marks())