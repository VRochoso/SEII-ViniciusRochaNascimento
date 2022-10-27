class students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return selg.grade

class course:
    def __init__(self, name, max_stud):
        self.name = name
        self.max_stud = max_stud
        self.students = []
        self.is_active = False