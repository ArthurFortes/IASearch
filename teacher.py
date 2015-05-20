__author__ = 'ArthurFortes'


class Teacher(object):
    def __init__(self, id_teacher, list_subjects, list_days):
        self.id_teacher = id_teacher
        self.list_subjects = list_subjects
        self.list_days = list_days

    def in_other_class(self, list_class):
        for day in range(5):
            for pos in range(4):
                cont = 0
                for subject in self.list_subjects:
                    for classroom in list_class:
                        if subject == classroom.schedule_matrix[day][pos]:
                            cont += 1
                if cont > 1:
                    return True

        return False