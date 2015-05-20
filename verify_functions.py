__author__ = 'ArthurFortes'


def return_teacher_consistency(classroom_list, subjects_list, day, pos):
    teachers_list = list()

    for classroom in classroom_list:
        for subject in subjects_list:
            if classroom.schedule_matrix[day][pos] == subject.id_subject:
                teachers_list.append(subject.id_teacher)

    if len([x for x in teachers_list if teachers_list.count(x) >= 2]) > 0:
        return False

    return True


def verify_subject(classroom_list):
    for classroom in classroom_list:
        for i in range(len(classroom.schedule_matrix)):
            list_position = list()
            for j in range(len(classroom.schedule_matrix[0])):
                list_position.append(classroom.schedule_matrix[i][j])

            for subject in list_position:
                if not subject == -1:
                    if list_position.count(subject) > 2:
                        return False
                    elif list_position.count(subject) == 2:
                        if subject in list_position[:2] and subject in list_position[2:]:
                            return False
    return True


def is_consistency(classroom_list, subjects_list):
    for classroom in classroom_list:
        for i in range(len(classroom.schedule_matrix)):
            for j in range(len(classroom.schedule_matrix[0])):
                if classroom.schedule_matrix[i][j] != -1:
                    if not (return_teacher_consistency(classroom_list, subjects_list, i, j)) or not (verify_subject(
                            classroom_list)):
                        return False
    return True
