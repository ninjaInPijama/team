class TeacherList:
    def __init__(self, teachers):
        self.teachers = teachers

    def get_teacher_by_name(self, name):
        for teacher in self.teachers:
            if teacher.username == name:
                return teacher
        return None
