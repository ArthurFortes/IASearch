from classroom import Classroom
from subject import Subject
from teacher import Teacher

__author__ = 'ArthurFortes'


"""
    Days of week:
        - Mon = 0
        - Thus = 1
        - When = 2
        - Tue = 3
        - Fry = 4

    Schedule:

                Mon     Thus    When    Tue     Fry
    Class 1
    Class 2
    Class 3
    Class 4

"""


def main():
    # insert teacher

    teacher0 = Teacher(0, [7], [0, 2, 4])
    teacher1 = Teacher(1, [0, 4], [])
    teacher2 = Teacher(2, [1, 5, 8], [1, 2, 3])
    teacher3 = Teacher(3, [2, 3], [0])
    teacher4 = Teacher(4, [6, 9], [0, 1, 3, 6])

    teachers_list = [teacher0, teacher1, teacher2, teacher3, teacher4]

    # insert subject

    subject0 = Subject(0, 1, 2)
    subject1 = Subject(1, 2, 2)
    subject2 = Subject(2, 3, 2)
    subject3 = Subject(3, 3, 2)
    subject4 = Subject(4, 1, 4)
    subject5 = Subject(5, 2, 4)
    subject6 = Subject(6, 4, 4)
    subject7 = Subject(7, 0, 6)
    subject8 = Subject(8, 2, 6)
    subject9 = Subject(9, 4, 6)

    subjects_list = [subject0, subject1, subject2, subject3, subject4, subject5, subject6, subject7, subject8, subject9]

    # insert classroom

    class0 = Classroom(0, [[-1 for _ in range(4)] for _ in range(5)])
    class1 = Classroom(1, [[-1 for _ in range(4)] for _ in range(5)])
    class2 = Classroom(2, [[-1 for _ in range(4)] for _ in range(5)])

    classroom_list = [class0, class1, class2]

if __name__ == "__main__":
    main()



