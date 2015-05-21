__author__ = 'ArthurFortes'


# def return_teacher_consistency(classroom_list, subjects_list, day, pos):
#     teachers_list = list()
#
#     for classroom in classroom_list:
#         for subject in subjects_list:
#             if classroom.schedule_matrix[day][pos] == subject.id_subject:
#                 teachers_list.append(subject.id_teacher)
#
#     if len([x for x in teachers_list if teachers_list.count(x) >= 2]) > 0:
#         return False
#
#     return True
#
#
# def verify_subject(classroom_list):
#     for classroom in classroom_list:
#         for i in range(len(classroom.schedule_matrix)):
#             list_position = list()
#             for j in range(len(classroom.schedule_matrix[0])):
#                 list_position.append(classroom.schedule_matrix[i][j])
#
#             for subject in list_position:
#                 if not subject == -1:
#                     if list_position.count(subject) > 2:
#                         return False
#                     elif list_position.count(subject) == 2:
#                         if subject in list_position[:2] and subject in list_position[2:]:
#                             return False
#     return True
#
#
# def is_consistency(classroom_list, subjects_list):
#     for classroom in classroom_list:
#         for i in range(len(classroom.schedule_matrix)):
#             for j in range(len(classroom.schedule_matrix[0])):
#                 if classroom.schedule_matrix[i][j] != -1:
#                     if not (return_teacher_consistency(classroom_list, subjects_list, i, j)) or not (verify_subject(
#                             classroom_list)):
#                         return False
#         break
#     return True

def return_teacher_consistency(classroom_list, subjects_list):
    line_length = len(classroom_list[0].schedule_matrix)
    column_length = len(classroom_list[0].schedule_matrix[0])

    for i in range(line_length):
        for j in range(column_length):
            teachers_list = list()
            for classroom in classroom_list:
                teachers_list.append(classroom.schedule_matrix[i][j])

            new_teacher_list = list()
            for item in teachers_list:
                for sub in subjects_list:
                    if item == sub:
                        new_teacher_list.append(sub.id_teacher)

            if len([x for x in new_teacher_list if new_teacher_list.count(x) >= 2]) > 0:
                return False

    return True


def verify_subject(class_matrix):
    for i in range(len(class_matrix)):
        list_position = list()
        for j in range(len(class_matrix[0])):
            list_position.append(class_matrix[i][j])

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
        if not verify_subject(classroom.schedule_matrix):
            return False

    if not return_teacher_consistency(classroom_list, subjects_list):
        print('wee')
        return False

    return True


def check_local_consistency(classroom_list, class_id, day, pos, id_subject, id_teacher, subjects_list):

    classroom_list[class_id].schedule_matrix[day][pos] = id_subject

    for classroom in classroom_list:

        if classroom.id_classroom == class_id:
            list_position = list()
            for j in range(len(classroom.schedule_matrix[0])):
                list_position.append(classroom.schedule_matrix[day][j])

            for subject in list_position:
                if not subject == -1:
                    if list_position.count(subject) > 2:
                        classroom_list[class_id].schedule_matrix[day][pos] = -1
                        return 0
                    elif list_position.count(subject) == 2:
                        if subject in list_position[:2] and subject in list_position[2:]:
                            classroom_list[class_id].schedule_matrix[day][pos] = -1
                            return 0
            pass
        else:
            sub_id = classroom.schedule_matrix[day][pos]
            if sub_id != -1:
                for sub_selected in subjects_list:
                    if sub_selected.id_subject == sub_id:
                        if sub_selected.id_teacher == id_teacher:
                            classroom_list[class_id].schedule_matrix[day][pos] = -1
                            return 0

    classroom_list[class_id].schedule_matrix[day][pos] = -1

    return 1


def teacher_preferences(teacher_list, teacher_id, day):
    for teacher in teacher_list:
        if teacher.id_teacher == teacher_id:
            if day in teacher.list_days:
                return 2
    return 0


def double_class_preferences(class_matrix, day, pos, id_subject):
    list_subjects = list()

    for sub in class_matrix[day]:
        list_subjects.append(sub)

    if pos > 1:
        if id_subject in list_subjects[2:]:
            return 3
    else:
        if id_subject in list_subjects[:2]:
            return 3

    return 0