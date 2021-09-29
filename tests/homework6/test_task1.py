import pytest

from homework6.task1 import DeadlineError, HomeworkResult, Student, Teacher


def test_homework_result_incorrect_input():
    good_student = Student('Lev', 'Sokolov')
    with pytest.raises(ValueError):
        HomeworkResult(good_student, "fff", "Solution")


def test_do_homework_deadline_error():
    good_student = Student('Lev', 'Sokolov')
    opp_teacher = Teacher('Daniil', 'Shadrin')
    oop_hw = opp_teacher.create_homework('Learn OOP', 0)
    with pytest.raises(DeadlineError):
        good_student.do_homework(oop_hw, 'I have done this hw')


def test_student_parent_class():
    good_student = Student('Lev', 'Sokolov')
    assert good_student.first_name == 'Lev'


def test_check_homework_done():
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')
    good_student = Student('Lev', 'Sokolov')
    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done
    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2


def test_check_homework_negative():
    opp_teacher = Teacher('Daniil', 'Shadrin')
    lazy_student = Student('Roman', 'Petrov')
    docs_hw = opp_teacher.create_homework('Read docs', 5)
    result = lazy_student.do_homework(docs_hw, 'done')
    assert not opp_teacher.check_homework(result)
