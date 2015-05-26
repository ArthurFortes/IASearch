from verify_functions import is_consistency, check_local_consistency, teacher_preferences, double_class_preferences

__author__ = 'ArthurFortes'


def restriction_search(classroom_list, subjects_list, teachers_list, number_nodes):
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

                    for sub in subjects_list:
                        if sub.lessons_quantity > 0:
                            new_list_subject.append(sub)

                    # select all possible movements
                    for subject in new_list_subject:

                        # check local consistency
                        score = check_local_consistency(classroom_list, classroom.id_classroom, i, j,
                                                        subject.id_subject, subject.id_teacher, subjects_list)

                        if score == 1:
                            score += teacher_preferences(teachers_list, subject.id_teacher, i)
                            score += double_class_preferences(classroom.schedule_matrix, i, j, subject.id_subject)
                            score += float(subject.lessons_quantity)/len(subjects_list)

                            # this list receives: class id | day | class hour | subject id | score
                            possible_movements.append([classroom.id_classroom, i, j, subject.id_subject, score])

    possible_movements = sorted(possible_movements, key=lambda x: -x[4])

    for possible_choice in possible_movements:
        subjects_list[possible_choice[3]].lessons_quantity -= 1
        classroom_list[possible_choice[0]].schedule_matrix[possible_choice[1]][possible_choice[2]] = possible_choice[3]
        number_nodes += 1

        # call backtracking
        backtracking, number_nodes = restriction_search(classroom_list, subjects_list, teachers_list, number_nodes)

        if backtracking:
            break
        else:
            subjects_list[possible_choice[3]].lessons_quantity += 1
            classroom_list[possible_choice[0]].schedule_matrix[possible_choice[1]][possible_choice[2]] = -1

    if is_consistency(classroom_list, subjects_list):
        return True, number_nodes
    else:
        return False, number_nodes
