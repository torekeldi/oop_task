class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lec(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress
                and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade(self):
        grade_list = []
        for v in self.grades.values():
            grade_list += v
        return sum(grade_list) / len(grade_list)

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_grade()}\n'
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {', '.join(self.finished_courses)}')

    def __eq__(self, other):
        if isinstance(other, Student) or isinstance(other, Lecturer):
            return self.avg_grade() == other.avg_grade()
        else:
            print('Объект сравнения не является экземпляром классов Student, Lecturer')

    def __ne__(self, other):
        if isinstance(other, Student) or isinstance(other, Lecturer):
            return self.avg_grade() != other.avg_grade()
        else:
            print('Объект сравнения не является экземпляром классов Student, Lecturer')

    def __lt__(self, other):
        if isinstance(other, Student) or isinstance(other, Lecturer):
            return self.avg_grade() < other.avg_grade()
        else:
            print('Объект сравнения не является экземпляром классов Student, Lecturer')

    def __gt__(self, other):
        if isinstance(other, Student) or isinstance(other, Lecturer):
            return self.avg_grade() > other.avg_grade()
        else:
            print('Объект сравнения не является экземпляром классов Student, Lecturer')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grade(self):
        grade_list = []
        for v in self.grades.values():
            grade_list += v
        return sum(grade_list) / len(grade_list)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade()}'

    def __eq__(self, other):
        if isinstance(other, Student) or isinstance(other, Lecturer):
            return self.avg_grade() == other.avg_grade()
        else:
            print('Объект сравнения не является экземпляром классов Student, Lecturer')

    def __ne__(self, other):
        if isinstance(other, Student) or isinstance(other, Lecturer):
            return self.avg_grade() != other.avg_grade()
        else:
            print('Объект сравнения не является экземпляром классов Student, Lecturer')

    def __lt__(self, other):
        if isinstance(other, Student) or isinstance(other, Lecturer):
            return self.avg_grade() < other.avg_grade()
        else:
            print('Объект сравнения не является экземпляром классов Student, Lecturer')

    def __gt__(self, other):
        if isinstance(other, Student) or isinstance(other, Lecturer):
            return self.avg_grade() > other.avg_grade()
        else:
            return 'Объект сравнения не является экземпляром классов Student, Lecturer'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def avg_grade_hw(students, course):
    grade_list = []
    for student in students:
        if isinstance(student, Student) and course in student.courses_in_progress and student.grades[course]:
            grade_list += student.grades[course]
    return sum(grade_list) / len(grade_list)


def avg_grade_lec(lecturers, course):
    grade_list = []
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and lecturer.grades[course]:
            grade_list += lecturer.grades[course]
    return sum(grade_list) / len(grade_list)


some_reviewer = Reviewer('Watcher', 'Seen')
print(some_reviewer)

some_lecturer = Lecturer('Jan', 'Lupin')
some_student = Student('Bale', 'Dan', 'Male')
some_lecturer.courses_attached.extend(['math'])
some_lecturer.courses_attached.extend(['biology'])
some_student.courses_in_progress.extend(['math'])
some_student.courses_in_progress.extend(['biology'])
some_student.rate_lec(some_lecturer, 'math', 10)
some_student.rate_lec(some_lecturer, 'math', 5)
some_student.rate_lec(some_lecturer, 'math', 7.5)
some_student.rate_lec(some_lecturer, 'biology', 10)
some_student.rate_lec(some_lecturer, 'biology', 5)
some_student.rate_lec(some_lecturer, 'biology', 7.5)
print(some_lecturer)

some_student.add_courses('physics')
some_student.add_courses('algebra')
some_reviewer.courses_attached = ['math']
some_reviewer.rate_hw(some_student, 'math', 10)
some_reviewer.rate_hw(some_student, 'math', 5)
some_reviewer.rate_hw(some_student, 'math', 7.5)
print(some_student)

print(some_lecturer == some_student)
print(some_lecturer != some_student)
print(some_lecturer > some_student)
print(some_lecturer < some_student)
print(some_lecturer == some_reviewer)

some_student1 = Student('student1', 'lastname1', 'Male')
some_student1.courses_in_progress = ['math']
some_reviewer.rate_hw(some_student1, 'math', 10)
some_reviewer.rate_hw(some_student1, 'math', 10)
some_student2 = Student('student2', 'lastname2', 'Male')
some_student2.courses_in_progress = ['math']
some_reviewer.rate_hw(some_student2, 'math', 9)
some_reviewer.rate_hw(some_student2, 'math', 9)
print(avg_grade_hw([some_student1, some_student2], 'math'))

some_lecturer1 = Lecturer('lecturer1', 'lastname1')
some_lecturer1.courses_attached = ['math']
some_student.rate_lec(some_lecturer1, 'math', 10)
some_student.rate_lec(some_lecturer1, 'math', 10)
some_lecturer2 = Lecturer('lecturer2', 'lastname2')
some_lecturer2.courses_attached = ['math']
some_student.rate_lec(some_lecturer2, 'math', 5)
some_student.rate_lec(some_lecturer2, 'math', 5)
print(avg_grade_lec([some_lecturer1, some_lecturer2], 'math'))
