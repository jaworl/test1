class Teacher:
    teachers = []
    ID = 1

    def __init__(self, teacherName, teacherLName, lesson, telephone, degree, age, teachExp):
        self.teacherName = teacherName
        self.teacherLName = teacherLName
        self.lesson = lesson
        self.telephone = telephone
        self.degree = degree
        self.age = age
        self.teachExp = teachExp
        self.id = Teacher.ID
        Teacher.ID += 1
        Teacher.teachers.append(self)

    def get_teachername(self):
        return self.teacherName

    def get_tacherLName(self):
        return self.teacherLName

    def get_lesson(self):
        return self.lesson

    def get_telephone(self):
        return self.telephone

    def get_age(self):
        return self.age

    def get_teachExp(self):
        return self.teachExp

    def get_id(self):
        return self.id

    def set_teacherName(self, teacherName):
        self.teacherName = teacherName

    def set_teacherLName(self, teacherLName):
        self.teacherLName = teacherLName

    def set_lesson(self, lesson):
        self.lesson = lesson

    def set_telephone(self, telephone):
        self.telephone = telephone

    def set_age(self, age):
        self.age = age

    def set_teachExp(self, teachExp):
        self.teachExp = teachExp

    def set_id(self, id):
        self.id = id

chemidonam = t.split()
def findTeacherByID(id):
    for t in Teacher.teachers:
        if t.ID == id:
            return chemidonam[0] , chemidonam[1]
        return None

def findIdTeacherByLastname(teacherLName):
        for nemidonam in range len(Teacher.teachers)
            if lastname in nemidonam.split():
                return Teacher.teachers[nemidonam]
            return None
