MY_NAME = "Om Dnyaneshwar Tambat"


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def set_marks(self, value):
        if value >= 0 and value <= 100:
            self.__marks = value
            print("Marks updated successfully.")
        else:
            print("Invalid marks. Marks must be between 0 and 100.")

    def get_marks(self):
        return self.__marks

    def grade(self):
        if self.__marks >= 80:
            return "A"
        elif self.__marks >= 60:
            return "B"
        elif self.__marks >= 40:
            return "C"
        else:
            return "Fail"

    def __str__(self):
        return f"Name: {self.name}, Marks: {self.__marks}, Grade: {self.grade()}"


student1 = Student(MY_NAME, 85)

print(student1)

student1.set_marks(100)
print(student1)