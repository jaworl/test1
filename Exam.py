import Model.Student as Student
class Exam :
    ID = 1
    exam = []
    def __init__(self,name,lName,lesson_name,date,grade,rank):
        self.name = name
        self.lName = lName
        self.lesson_name = lesson_name
        self.date = date
        self.grade = grade
        self.rank = rank
        self.id = Exam.ID
        Exam.ID +=1 
        Exam.exam.append(self)
    
    def set_name(self,name):
        self.name = name
    def set_lName(self,lName):
        self.lName = lName
    def set_lesson_name(self,lesson_name):
        self.lesson_name = lesson_name
    def set_date(self,date):
        self.date = date
    def set_grade(self,grade):
        self.grade = grade
    def set_rank(self,rank):
        self.rank = rank
    def set_ID(self,id):
        self.id = id

    def get_name(self):
        return self.name 
    def get_lName(self):
        return self.lName 
    def get_lesson_name(self):
        return self.lesson_name 
    def get_date(self):
        return self.date 
    def get_grade(self):
        return self.grade 
    def get_rank(self):
        return self.rank 
    def get_ID(self):
        return self.id

    