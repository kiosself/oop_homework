from statistics import mean


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
                lectuer.grades[course] += grade
            else:
                lectuer.grades[course] = grade
        else:
            print('Ошибка')

    def __lt__(self, other):
        self_student_grades = mean(self.grades.values())
        other_student_grades = mean(other.grades.values())
        if self_student_grades < other_student_grades:
            return True
        else:
            return False

    def __rt__(self, other):
        self_student_grades = mean(self.grades.values())
        other_student_grades = mean(other.grades.values())
        if self_student_grades > other_student_grades:
            return True
        else:
            return False

    def __eq__(self, other):
        self_student_grades = mean(self.grades.values())
        other_student_grades = mean(other.grades.values())
        if self_student_grades == other_student_grades:
            return True
        else:
            return False

    def __str__(self):
        ans = 'Имя: {} \nФамилия: {}'.format(self.name, self.surname)
        ans += '\nСредняя оценка за домашние задания: {}'.format(mean(self.grades.values()))
        ans += '\nКурсы в процессе изучения: {}'.format(', '.join(str(i) for i in self.courses_in_progress))
        ans += '\nЗавершенные курсы: {}'.format(', '.join(str(i) for i in self.finished_courses))
        ans += "\n-----------------------------------------------------"
        return ans


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lectuer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        ans = 'Имя: {} \nФамилия: {}'.format(self.name, self.surname)
        ans += '\nСредняя оценка за лекции: {}'.format(mean(self.grades.values()))
        ans += "\n-----------------------------------------------------"
        return ans

    def __lt__(self, other):
        self_student_grades = mean(self.grades.values())
        other_student_grades = mean(other.grades.values())
        if self_student_grades < other_student_grades:
            return True
        else:
            return False

    def __rt__(self, other):
        self_student_grades = mean(self.grades.values())
        other_student_grades = mean(other.grades.values())
        if self_student_grades > other_student_grades:
            return True
        else:
            return False

    def __eq__(self, other):
        self_student_grades = mean(self.grades.values())
        other_student_grades = mean(other.grades.values())
        if self_student_grades == other_student_grades:
            return True
        else:
            return False


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += grade
            else:
                student.grades[course] = grade
        else:
            print('Ошибка')

    def __str__(self):
        ans = 'Имя: {} \nФамилия: {}'.format(self.name, self.surname)
        ans += "\n-----------------------------------------------------"
        return ans


# Reviewers start -------------------------
kay = Reviewer('Kay', 'Thompson')
kay.courses_attached = 'Ruby', 'Python'

olaf = Reviewer('Olaf', 'Swanson')
olaf.courses_attached = 'Ruby', 'Python'
# Reviewers end ---------------------------

# Lectuers start --------------------------
tom = Lectuer('Tom', 'Wilson')
tom.courses_attached = 'Ruby', 'Python'

anita = Lectuer('Anita', 'Falco')
anita.courses_attached = 'Ruby', 'Python'
# Lectuers end ---------------------------

# Students start --------------------------
jerry = Student('Jerry', "Maker", 'Male')
jerry.courses_in_progress = 'Ruby', 'Python'
jerry.finished_courses = 'Intro', 'Basic'

taker = Student('Taker', "Shelby", 'Male')
taker.courses_in_progress = 'Ruby', 'Python'
taker.finished_courses = 'Intro', 'Basic'
# Students end ------------------------------

kay.rate_hw(jerry, 'Ruby', 10)
kay.rate_hw(jerry, 'Python', 7)

olaf.rate_hw(taker, 'Ruby', 9)
olaf.rate_hw(taker, 'Python', 6)

taker.rate_lectuer(anita, 'Ruby', 10)
taker.rate_lectuer(anita, 'Python', 7)

jerry.rate_lectuer(tom, 'Ruby', 9)
jerry.rate_lectuer(tom, 'Python', 3)

print(kay)
print(jerry)
print(taker)
print(tom)
print(anita)
print(jerry < taker)
print(jerry > taker)
print(jerry == taker)
print(tom < anita)
print(tom > anita)
print(tom == anita)