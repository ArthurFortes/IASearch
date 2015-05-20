from random import shuffle
from verify_functions import is_consistency

__author__ = 'ArthurFortes'


def blind_search(classroom_list, subjects_list, number_nodes):
    id_list = list()

    for subject in subjects_list:
        id_list.append(subject.id_subject)

    possible_movements = list()

    for classroom in classroom_list:
        for i in range(len(classroom.schedule_matrix)):
            for j in range(len(classroom.schedule_matrix[0])):

                if classroom.schedule_matrix[i][j] == -1:

                    new_list_subject = list()
                    shuffle(id_list)

                    for id_number in id_list:
                        new_list_subject.append(subjects_list[id_number])

                    for subject in new_list_subject:
                            if subject.lessons_quantity > 0:
                                possible_movements.append([classroom.id_classroom, i, j, subject.id_subject, 0])

    for possible_choice in possible_movements:
        subjects_list[possible_choice[3]].lessons_quantity -= 1
        classroom_list[possible_choice[0]].schedule_matrix[possible_choice[1]][possible_choice[2]] = possible_choice[3]
        number_nodes += 1

        backtracking, number_nodes = blind_search(classroom_list, subjects_list, number_nodes)

        if backtracking:
            break
        else:
            subjects_list[possible_choice[3]].lessons_quantity += 1
            classroom_list[possible_choice[0]].schedule_matrix[possible_choice[1]][possible_choice[2]] = -1

    if is_consistency(classroom_list, subjects_list):
        return True, number_nodes
    else:
        return False, number_nodes

