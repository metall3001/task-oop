class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def add_cour_attached(self, course):
        self.courses_attached.append(course)


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grades_list = []
        self.ave_grade = float

    def __str__(self):
        text = (f" Имя: {self.name}",
                f" Фамилия: {self.surname}",
                f" Средняя оценка за задания: {float(sum(self.grades.values())/len(self.grades.keys()))}",
                f" В данный момент учимся: {self.courses_in_progress}",
                f" Закончил обучение: {self.finished_courses}")
        return text

    def add_fin_course(self, course):
        self.finished_courses.append(course)

    def add_progress_courses(self, course):
        self.courses_in_progress.append(course)

    def rate_lect(self, lecturer, course, digit):

        if isinstance(lecturer, Lecturer):
            if course in self.courses_in_progress and course in lecturer.course_lect:
                lecturer.rate.append(digit)

            else:
                print('Ошибочка вышла')
        else:
            print('Вероятно, это не Лектор')

    def average_grade(self):
        self.ave_grade = sum(self.grades.values())/len(self.grades.keys())
        return self.ave_grade

    def __eq__(self, other):
        return self.ave_grade == other.ave_grade


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.finished_courses:
            if course in student.grades:
                student.grades[course] = int(grade)
                student.grades_list.append(int(grade))
            else:
                return "Ошибочка вышла"
        else:

            return 'Ошибочка вышла'

    def __str__(self):
        text_rev = (f"Имя: {self.name}",
                    f"Фамилия: {self.surname}"
        )
        return text_rev


class Lecturer(Mentor):
    def __init__ (self, name, surname):
        self.name = name
        self.surname = surname
        self.rate = []
        self.course_lect = []
        self.ave_rate = float

    def __str__(self):
        text_lec = (f"Имя: {self.name}",
                    f"Фамилия: {self.surname}",
                    f"Средняя оценка за лекции: {float(sum(self.rate))/len(self.rate)}")
        return text_lec

    def add_cour_lect(self, course):
        self.course_lect.append(course)

    def add_ave_rate(self):
        self.ave_rate = (sum(self.rate)) / len(self.rate)
        return self.ave_rate

    def __eq__(self, other):
        return self.ave_rate == other.ave_rate


student_list = []
student1 = Student('Тор', 'Одинсон', 'мужской')
student1.add_fin_course('Владение молотом')
student1.add_fin_course('Владение секирой')
student1.grades['Владение молотом'] = None
student1.grades['Владение секирой'] = None
student1.add_progress_courses("Полет верхом на секире")
student1.add_progress_courses("Радужный мост")

student_list.append(student1)
student2 = Student('Локи', 'Йотонхеймский', 'мужской')
student2.add_fin_course('Владение молотом')
student2.add_fin_course('Владение секирой')
student2.add_progress_courses("Радужный мост")
student2.add_progress_courses("Полет верхом на секире")
student2.grades['Владение молотом'] = None
student2.grades['Владение секирой'] = None
student_list.append(student2)


lecturer1 = Lecturer('Один', 'Всеотец')
lecturer1.add_cour_lect('Радужный мост')
lecturer2 = Lecturer('Гном', 'Эйтри')
lecturer2.add_cour_lect("Полет верхом на секире")
lecturer_list = []
lecturer_list.append(lecturer1)
lecturer_list.append(lecturer2)


student1.rate_lect(lecturer1, "Радужный мост", 9)
student1.rate_lect(lecturer2, "Полет верхом на секире", 10)
student2.rate_lect(lecturer1, "Радужный мост", 8)
student2.rate_lect(lecturer2, "Полет верхом на секире", 10)

lecturer1.__eq__(lecturer2)
lecturer2.__eq__(lecturer1)
reviewer1 = Reviewer('Вонг', 'Маг')
reviewer2 = Reviewer('Доктор', 'Стренж')
reviewer2.add_cour_attached('Владение молотом')
reviewer1.add_cour_attached('Владение секирой')
reviewer1.rate_hw(student1, "Владение секирой", 10)
reviewer1.rate_hw(student2, "Владение секирой", 9)
reviewer2.rate_hw(student1, "Владение молотом", 6)
reviewer2.rate_hw(student2, "Владение молотом", 7)
student1.__eq__(student2)
student2.__eq__(student1)


print(lecturer1.__eq__(lecturer2))
print(student1.__eq__(student2))

print(reviewer1.__str__())
print(reviewer2.__str__())
print(lecturer1.__str__())
print(lecturer2.__str__())


print(student1.__str__())
print(student2.__str__())