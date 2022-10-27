from hashlib import sha3_224


class students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_stud):
        self.name = name
        self.max_stud = max_stud
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_stud:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

s1 = students("vincius", 27, 95)
s2 = students("rocha", 27, 90)
s3 = students("nascimento", 27, 100)

course = Course("Sistemas Embarcados 2", 2)
course.add_student(s2)
course.add_student(s2)
print(course.add_student(s3))
print(course.students[0].name)
print(course.get_average_grade())