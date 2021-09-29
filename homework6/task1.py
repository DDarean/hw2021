"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""


from collections import defaultdict
from datetime import datetime, timedelta


class DeadlineError(Exception):
    pass


class Homework:
    def __init__(self, text, days):
        self.text = text
        self.created = datetime.now()
        self.deadline = timedelta(days)

    def is_active(self):
        current_datetime = datetime.now()
        return not current_datetime >= self.created + self.deadline


class HomeworkResult:
    def __init__(self, student, homework, solution):
        if not isinstance(homework, Homework):
            raise ValueError('You gave a not Homework object')
        self.homework = homework
        self.solution = solution
        self.author = student
        self.created = datetime.now()


class Human:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Student(Human):
    def do_homework(self, homework, solution):
        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        else:
            raise DeadlineError("You are late!")


class Teacher(Human):
    homework_done = defaultdict()

    @staticmethod
    def create_homework(text, days):
        return Homework(text, days)

    @staticmethod
    def check_homework(result):
        if not isinstance(result, HomeworkResult):
            raise ValueError('You gave a not HomeworkResult object')
        if len(result.solution) >= 5:
            Teacher.homework_done[result.homework] = result
            return True
        else:
            return False

    @staticmethod
    def reset_results(homework=None):
        if homework is None:
            Teacher.homework_done.clear()
        else:
            Teacher.homework_done.pop(homework)
