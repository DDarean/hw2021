from sqlalchemy import (Column, DateTime, ForeignKey, Integer,
                        String, create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///origin.db')

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer(), primary_key=True)
    last_name = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    solutions = relationship('HomeworkResult')


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer(), primary_key=True)
    last_name = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)


class Homework(Base):
    __tablename__ = 'homeworks'
    id = Column(Integer(), primary_key=True)
    text = Column(String(50), nullable=False)
    created = Column(DateTime())
    deadline = Column(DateTime())


class HomeworkResult(Base):
    __tablename__ = 'solutions'
    id = Column(Integer(), primary_key=True)
    homework = Column(Integer, ForeignKey('homeworks.id'))
    author = Column(Integer, ForeignKey('students.id'))
    created = Column(DateTime())


Base.metadata.create_all(engine)
