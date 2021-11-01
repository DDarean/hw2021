from datetime import datetime, timedelta

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from create import Homework, HomeworkResult, Student, Teacher

engine = create_engine(r"sqlite:///new_migrate.db")

session = Session(bind=engine)

c1 = Student(id=1, last_name='Trriiksa', first_name='Vasiliy')
c2 = Teacher(id=1, last_name='Petrov', first_name='Alex')
c3 = Homework(id=2, text='solution', created=datetime.now(),
              deadline=datetime.now() + timedelta(days=5))
c4 = HomeworkResult(id=1, homework=1, author=1, created=datetime.now())
session.add_all([c1, c2, c3, c4])
session.commit()
