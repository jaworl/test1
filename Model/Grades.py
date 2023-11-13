import Model.Exam
class Grades :
    def __init__ (self) :
        # self.examResults = []
        self.math = []
        self.biology = []
        self.physics = []
        self.chemistry = []
        self.geology = []
        self.arabic = []
        self.history = []
        self.english = []
        self.dini = []

    def get_math(self) :
        return self.math
    def get_biology(self) :
        return self.biology
    def get_physics(self) :
        return self.physics
    def get_chemistry(self) :
        return self.chemistry
    def get_geology(self) :
        return self.chemistry
    def get_arabic(self) :
        #continuio
    def addToExam(exam) :
        if exam == "math" :
            
    def add_exam_result(self , examRes) :
        self.examResults.append(examRes)