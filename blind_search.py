from random import shuffle
from verify_functions import is_consistency

__author__ = 'ArthurFortes'


def blind_search(classroom_list, subjects_list, number_nodes, flag='normal'):
    id_list = list()

    # create a list with objects ids
    for subject in subjects_list:
        id_list.append(subject.id_subject)

    possible_movements = list()

    for classroom in classroom_list:
        for i in range(len(classroom.schedule_matrix)):
            for j in range(len(classroom.schedule_matrix[0])):

                if classroom.schedule_matrix[i][j] == -1:

                    new_list_subject = list()

                    if flag == 'random':

                        # Shuffle list of ids to build different lists of objects
                        shuffle(id_list)

                        for id_number in id_list:
                            # verify subject was full alloc in classrooms
                            if subjects_list[id_number].lessons_quantity > 0:
                                new_list_subject.append(subjects_list[id_number])

                    elif flag == 'normal':
                        for sub in subjects_list:
                            if sub.lessons_quantity > 0:
                                new_list_subject.append(sub)

                    # select all possible movements
                    for subject in new_list_subject:
                        # this list receives: class id | day | class hour | subject id
                        possible_movements.append([classroom.id_classroom, i, j, subject.id_subject])

    for possible_choice in possible_movements:
        subject_selected = ''
        classroom_selected = ''

        for subject in subjects_list:
            if subject.id_subject == possible_choice[3]:
                subject_selected = subject

        for classroom in classroom_list:
            if classroom.id_classroom == possible_choice[0]:
                classroom_selected = classroom

        subjects_list[subjects_list.index(subject_selected)].lessons_quantity -= 1
        classroom_list[classroom_list.index(classroom_selected)].schedule_matrix[possible_choice[1]][
            possible_choice[2]] = possible_choice[3]
        number_nodes += 1

        # call backtracking
        backtracking, number_nodes = blind_search(classroom_list, subjects_list, number_nodes)

        if backtracking:
            return True, number_nodes
        else:
            subjects_list[subjects_list.index(subject_selected)].lessons_quantity += 1
            classroom_list[classroom_list.index(classroom_selected)].schedule_matrix[possible_choice[1]][
                possible_choice[2]] = -1

    if is_consistency(classroom_list, subjects_list):
        return True, number_nodes
    else:
        return False, number_nodes
