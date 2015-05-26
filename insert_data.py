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
    print('\n IA Search \n')

    print(u'The allocation of classrooms (scheduling) is a problem in which the objective is to organize a set of '
          u'materials of different workloads on a set of classrooms available.')
    print(u'This issue is implemented for*:')
    print(u'- ', len(subjects_list), ' subjects')
    print(u'- ', len(teachers_list), ' teachers')
    print(u'- ', len(classroom_list), ' classrooms')

    print(u'* To change this setting change the source code of this file.\n')
    print(u'Choose one of the searches below to solve the problem:')

    print('1 - Blind Search')
    print('2 - Heuristic Search')
    print('3 - Restriction Search')
    print('4 - Show subjects')
    print('5 - Insert subjects')
    print('6 - Exit')
    print('\n')

    number_nodes = 0
    start_time = 0

    try:
        user_option = int(input('What is your choice: '))

        if user_option == 1:
            # Blind Search
            print('This search may take a long time to display the result. Be patient!')
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
            print("\n_________________________________________________")
            print("|   Subject ID   |   Teacher ID   |   Workload   |")
            print("_________________________________________________")
            for subject in subjects_list:
                print("|       ", subject.id_subject, "      |      ", subject.id_teacher, "      |      ",
                      subject.lessons_quantity, "      |")

                print("_________________________________________________")

        elif user_option == 5:
            exit()

        else:
            print('Invalid option, choice must be (1-3). Try Again!')
            main()

        if user_option in [1, 2, 3]:
            print('\n')
            print("Runtime: %s seconds" % (time.time() - start_time))
            print("Number of nodes visited: %s  \n" % number_nodes)

            print("--- Schedules ---")
            print('[Classroom/ Day][--Monday--] [--Tuesday--] [--Wednesday--] [--Thursday--] [--Friday--]')
            for class_option in classroom_list:
                print('Classroom ', class_option.id_classroom, ' ', class_option.schedule_matrix)

        option = input('\nReturn to menu (Y or N)? ')
        if option == 'y' or option == 'Y':
            os.system("cls")
            main()
        else:
            exit()

    except ValueError:
        os.system("cls")
        print('Number must be a integer')
        main()


def main():    # initialize objects

    # insert teacher
    # Teacher(id, subject_id, list_days)
    teacher0 = Teacher(0, [7], [0, 2, 4])
    teacher1 = Teacher(1, [0, 4], [])
    teacher2 = Teacher(2, [1, 5, 8], [1, 2, 3])
    teacher3 = Teacher(3, [2, 3], [0])
    teacher4 = Teacher(4, [6, 9], [0, 1, 3])

    # Put teachers in a list
    teachers_list = [teacher0, teacher1, teacher2, teacher3, teacher4]

    # insert subject
    # Subject(id, teacher_id, lessons_quantity)
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

    # insert classroom
    # Classroom(id, schedule_matrix)
    class0 = Classroom(0, [[-1 for _ in range(4)] for _ in range(5)])
    class1 = Classroom(1, [[-1 for _ in range(4)] for _ in range(5)])
    class2 = Classroom(2, [[-1 for _ in range(4)] for _ in range(5)])

    # Put classes in a list
    classroom_list = [class0, class1, class2]
    menu(classroom_list, subjects_list, teachers_list)


if __name__ == "__main__":
    main()
