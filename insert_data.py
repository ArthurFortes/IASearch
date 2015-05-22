import time
import os
from classroom import Classroom
from subject import Subject
from teacher import Teacher
from blind_search import blind_search
from heuristic_search import heuristic_search
from restriction_search import restriction_search

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


def menu(classroom_list, subjects_list, teachers_list):
    number_nodes = 0
    start_time = 0

    print('===== Menu ======')

    print(u'The allocation of classrooms (scheduling) is a problem in which the objective is to organize a set of '
          u'materials of different workloads on a set of classrooms available.')
    print(u'This issue is implemented for*:')
    print(u'- 10 subjects')
    print(u'- 5 teachers')
    print(u'- 3 classrooms')

    print(u'* To change this setting change the source code of this file.\n')
    print(u'Choose one of the searches below to solve the problem:')

    print('1 - Blind Search')
    print('2 - Heuristic Search')
    print('3 - Restriction Search')
    print('4 - Exit')
    print('\n')

    try:
        user_option = int(input('What is your name:'))
        if user_option == 1:
            # Blind Search
            start_time = time.time()
            return_success, number_nodes = blind_search(classroom_list, subjects_list, number_nodes)

        elif user_option == 2:
            # Heuristic Search
            start_time = time.time()
            return_success, number_nodes = heuristic_search(classroom_list, subjects_list, teachers_list, number_nodes)

        elif user_option == 3:
            # Restriction Search
            start_time = time.time()
            return_success, number_nodes = restriction_search(classroom_list, subjects_list, teachers_list,
                                                              number_nodes)

        elif user_option == 4:
            exit()

        else:
            print('Invalid option, choice must be (1-3). Try Again!')
            menu(classroom_list, subjects_list, teachers_list)

        print('\n')
        print("Runtime: %s seconds" % (time.time() - start_time))
        print("Number of nodes visited: %s  \n" % number_nodes)

        print("--- Schedules ---")
        print('[--Monday--] [--Tuesday--] [--Wednesday--] [--Thursday--] [--Friday--]')
        for class_option in classroom_list:
            print(class_option.schedule_matrix)

    except ValueError:
        os.system("cls")
        print('Number must be a integer')
        menu(classroom_list, subjects_list, teachers_list)


def main():
    # initialize objects

    # insert teacher
    teacher0 = Teacher(0, [7], [0, 2, 4])
    teacher1 = Teacher(1, [0, 4], [])
    teacher2 = Teacher(2, [1, 5, 8], [1, 2, 3])
    teacher3 = Teacher(3, [2, 3], [0])
    teacher4 = Teacher(4, [6, 9], [0, 1, 3, 6])

    # Put teachers in a list
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

    # Put subjects in a list
    subjects_list = [subject0, subject1, subject2, subject3, subject4, subject5, subject6, subject7, subject8, subject9]

    # subject0 = Subject(0, 1, 2)
    # subject1 = Subject(1, 2, 2)
    # subject2 = Subject(2, 1, 4)
    #
    # # Put subjects in a list
    # subjects_list = [subject0, subject1, subject2]

    # insert classroom
    class0 = Classroom(0, [[-1 for _ in range(4)] for _ in range(5)])
    class1 = Classroom(1, [[-1 for _ in range(4)] for _ in range(5)])
    class2 = Classroom(2, [[-1 for _ in range(4)] for _ in range(5)])

    # Put classes in a list
    classroom_list = [class0, class1, class2]

    # class0.schedule_matrix[0][3] = 1
    # class0.schedule_matrix[0][2] = 1
    # class0.schedule_matrix[0][1] = 3
    # class0.schedule_matrix[0][0] = 3
    #
    # class1.schedule_matrix[0][3] = 6
    # class1.schedule_matrix[0][2] = 6
    # class1.schedule_matrix[0][1] = 4
    # class1.schedule_matrix[0][0] = 4
    #
    # class2.schedule_matrix[2][3] = 2
    # class2.schedule_matrix[2][2] = 2
    # class2.schedule_matrix[2][1] = 7
    # class2.schedule_matrix[2][0] = 7
    #
    # print(class0.schedule_matrix)
    # print(class1.schedule_matrix)
    # print(class2.schedule_matrix)
    #
    # print(is_consistency(classroom_list, subjects_list))

    menu(classroom_list, subjects_list, teachers_list)


if __name__ == "__main__":
    main()