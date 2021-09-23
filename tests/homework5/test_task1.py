from homework5.task1 import Homework, Student, Teacher


def test_teacher_name():
    teacher = Teacher('Daniil', 'Shadrin')
    assert teacher.last_name == 'Shadrin'


def test_student_name():
    student = Student('Roman', 'Petrov')
    assert student.first_name == 'Roman'


def test_expired_homework():
    teacher = Teacher('Daniil', 'Shadrin')
    student = Student('Roman', 'Petrov')
    expired_homework = teacher.create_homework('Learn functions', 0)
    assert student.do_homework(expired_homework) == 'You are late'


def test_active_homework():
    teacher = Teacher('Daniil', 'Shadrin')
    student = Student('Roman', 'Petrov')
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    assert isinstance(student.do_homework(oop_homework), Homework)
