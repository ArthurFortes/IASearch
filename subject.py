__author__ = 'ArthurFortes'


class Subject(object):
    def __init__(self, id_subject, id_teacher, lessons_quantity):
        self.id_subject = id_subject
        self.id_teacher = id_teacher
        self.lessons_quantity = lessons_quantity

    def in_other_class(self, list_class):
        for day in range(5):
            for pos in range(4):
                cont = 0
                for classroom in list_class:
                    if self.id_subject == classroom.schedule_matrix[day][pos]:
                            cont += 1
                if cont > 1:
                    return True

        return False

    def more_three_times(self, classroom_list):
        if self.in_other_class(classroom_list):
            print("A subject is taking place in two rooms at once.")
            return True

        for day in range(5):
            cont = 0
            for classroom in classroom_list:
                for pos in range(4):
                    if self.id_subject == classroom[day][pos]:
                        cont += 1
            if cont > 2:
                return True

        return False

    def is_not_consecutive(self, classroom_list):
        if self.more_three_times(classroom_list):
            print("The subject is occurring more than 2 times in one day")
            return False

        for day in range(5):
            position = list()
            for classroom in classroom_list:
                for pos in range(4):
                    if self.id_subject == classroom[day][pos]:
                        position.append(pos)

            if len(position) > 1:
                if not (position[0]+1 == position[1] or position[0]-1 == position[1]):
                    return True

        return True