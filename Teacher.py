class Teacher :
    teachers = []
    ID =1
    def __init__(self,name,lName,grade,lesson,qualification,age,num):
        self.name = name
        self.lName = lName
        self.age = age
        self.classGrade = grade
        self.lesson = lesson
        self.qualification = qualification
        self.number = num
        self.id = Teacher.ID
        Teacher.ID +=1 
        Teacher.teachers.append(self)

    #def __str__(self):
    #    return f"Teacher {self.name}{self.lName}'s profile /n ID : {self.ID} ,age :{self.age} /n class : {self.clac}/n qualification : {self.qualification}"
    
    def get_name(self):
        return self.name
    def get_lName(self):
        return self.lName
    def get_age(self):
        return self.age
    def get_ID(self):
        return self.id
    def get_classGrade(self):
        return self.classGrade
    def get_lesson(self):
        return self.lesson
    def get_num(self):
        return self.number
    def get_qualification(self):
        return self.qualification
    
    def set_name(self,name):
        self.name = name
    def set_lName(self,lName):
        self.lName = lName
    def set_age(self,age):
        self.age = age
    def set_ID(self,id):
        self.id = id
    def set_classGrede(self,grade):
        self.classGrade = grade
    def set_lesson(self,lesson):
        self.lesson = lesson
    def set_num(self,num):
        self.number = num
    def set_qualification(self,qua):
        self.qualification = qua

    def findTeacherByID(id) :
        for i in Teacher.teachers :
            if i.ID == id :
                return i
        return None