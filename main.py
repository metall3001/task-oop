
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
    """Добавляем новые обьекты"""
        self.courses_finished = []
        self.courses_in_progress = []
        self.grades = {}
        self.grades_list = []
        self.ave_grade = float

    """Переопределяем класс"""
    def __str__(self):
        text = (f'Имя: {self.name}',
                f'Фамилия: {self.surname}',
                f'Средняя оценка за задачи: {float(sum(self.grades.values()/len(self.grades.keys())))}',
                f'Текущие курсы: {self.courses_in_progress}',
                f'Прошедшие курсы: {self.courses_finished}')

        return text

    def add_final_course(self, course):
        self.courses_finished.append(course)

    def add_courses_in_progress(self, course):
        self.courses_in_progress.append(course)

    """Попытка оценить Лектора"""

    def rate_lector(self, lecturer, course, digit):
        if isinstance(lecturer, Lecturer):
            if course in self.courses_in_progress and course in lecturer.course_lect:
                lecturer.rate.append(digit)
            else:
                print('Ошибочка вышла')
        else:
            print('Вероятно, это не Лектор')


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in self.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


    """Переопределяем класс"""
    def __str__(self):
        text_rev = (
            f'Имя: {self.name}',
            f'Фамилия: {self.surname}'
        )
        return text_rev


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        """Добавляем новые обьекты"""
        self.rate = []
        self.course_lect = []
        """Добавляем среднюю оценку"""
        self.ave_rate = float

    """Переопределяем класс"""
    def __str__(self):
        text_lect = (f'Имя: {self.name}',
                     f'Фамилия: {self.surname}',
                     f'Средняя оценка: {float(sum(self.rate))/len(self.rate)}')
        return text_lect


student_list = []
student_1 = Student('Тор', 'Одинсон', 'мужской')
student_1.add_final_course('Программист PHP')