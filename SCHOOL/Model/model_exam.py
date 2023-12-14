#import Model.model_student


class Exam:
    exams = []
    ID = 1

    def __init__(self, studentId, examID, date, score, rank, teacherId):
        self.studentId = studentId
        self.examID = examID
        self.date = date
        self.score = score
        self.rank = rank
        self.teacherId = teacherId
        self.ID = Exam.ID
        Exam.ID += 1
        Exam.exams.append(self)

    def get_studentName(self):
        return self.studentName

    def get_examID(self):
        return self.examID

    def get_date(self):
        return self.date

    def get_score(self):
        return self.score

    def get_rank(self):
        return self.rank

    def get_tacherName(self):
        return self.teacherName

    def set_studentName(self, studentname):
        self.studentName = studentname

    def set_examID(self, examID):
        self.examID = examID

    def set_date(self, date):
        self.date = date

    def set_score(self, score):
        self.score = score

    def set_rank(self, rank):
        self.rank = rank

    def set_teacherName(self, teacherName):
        self.teacherName = teacherName
