"""
Write a function that gets file path as an argument.
Read the first line of the file.
If first line is a number return true if number in an interval [1, 3)*
and false otherwise.
In case of any error, a ValueError should be thrown.

Write a test for that function using pytest library.

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - tests do a cleanup and remove remove files generated by tests

* https://en.wikipedia.org/wiki/Interval_(mathematics)#Terminology
** https://docs.python.org/3/library/os.path.html
*** https://docs.python.org/3/tutorial/errors.html#handling-exceptions
**** https://docs.python.org/3/tutorial/errors.html#raising-exceptions
"""


def read_magic_number(path: str) -> bool:
    with open(path) as file:
        try:
            line = file.readline()
            if 1 <= int(line) < 3:
                return True
            else:
                return False
        except ValueError:
            raise ValueError
