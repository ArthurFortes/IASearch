__author__ = 'ArthurFortes'


class Classroom(object):
    def __init__(self, id_classroom, schedule_matrix):
        self.id_classroom = id_classroom
        self.schedule_matrix = schedule_matrix

    def is_empty(self, day, position):
        if self.schedule_matrix[day][position] == -1:
            return True
        else:
            return False

    def schedule_is_full(self):
        for i in range(len(self.schedule_matrix)):
            for j in range(len(self.schedule_matrix[0])):
                if self.schedule_matrix[i][j] == -1:
                    return False
        return True