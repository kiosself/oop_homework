class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lectuer(self, lectuer, course, grade):
        if isinstance(lectuer, Lectuer) and course in self.courses_in_progress and course in lectuer.courses_attached:
            if course in lectuer.grades:
                lectuer.grades[course] += [grade]
            else: lectuer.grades[course] = grade

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lectuer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

tom = Lectuer('Tom','Wilson')
jerry = Student('Jerry', "Maker", 'Male')
jerry.courses_in_progress = 'Python', 'Ruby'
tom.courses_attached = 'Ruby', 'Python'
jerry.rate_lectuer(tom,'Ruby', 10)
jerry.rate_lectuer(tom,'Python', 7)

print(tom.name, tom.surname, tom.grades)
