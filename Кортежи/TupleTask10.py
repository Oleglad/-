from collections import namedtuple
Student = namedtuple('Student', ['name', 'age', 'grade', 'city'])
students = (
    Student(name='Иван', age=20, grade=4.5, city='Москва'),
    Student(name='Мария', age=21, grade=3.8, city='Санкт-Петербург'),
    Student(name='Алексей', age=22, grade=4.2, city='Екатеринбург'),
    Student(name='Анна', age=19, grade=4.8, city='Казань'),
    Student(name='Дмитрий', age=23, grade=3.5, city='Новосибирск'),
    Student(name='Елена', age=20, grade=4.9, city='Челябинск'),
    Student(name='Сергей', age=21, grade=4.1, city='Краснодар')
)
def good_students(students):
    total_grades = sum(student.grade for student in students)
    average_grade = total_grades / len(students)
    good_students_list = [student.name for student in students if student.grade >= average_grade]
    if good_students_list:
        print(f'Ученики {", ".join(good_students_list)} в этом семестре хорошо учатся!')
    else:
        print('Нет студентов, которые учились бы хорошо в этом семестре.')
good_students(students)