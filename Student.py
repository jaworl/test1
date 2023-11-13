import Model.Exam as Exam
import Model.Grades as Grades
class Student :
    students = []
    ID =1
    def __init__(self,name,lName,grade,fatherName,GP,addres,PC,telephoneNum,DH,examResults):
        self.name = name
        self.lName = lName
        self.grade = grade
        self.fatherName = fatherName
        self.GP = GP
        self.addres = addres
        self.PC = PC
        self.telephoneNum = telephoneNum
        self.DH = DH
        self.id = Student.ID
        Student.ID +=1 
        Student.students.append(self)

    #def __str__(self):
    #    return f"Student {self.name}{self.lName}'s profile/n ID : {self.ID} ,father name :{self.fatherName} /n class : {self.clac}/n GP : {self.GP} /n addres: {self.addres} /n PC : {self.PC}/n telephone number: {self.telephoneNum} /n DH : {self.DH}"
    def get_name(self):
        return self.name
    def get_lName(self):
        return self.lName
    def get_fName(self):
        return self.fatherName
    def get_ID(self):
        return self.id
    def get_grade(self):
        return self.grade
    def get_PC(self):
        return self.PC
    def get_addres(self):
        return self.addres
    def get_DH(self):
        return self.DH
    def get_num(self):
        return self.telephoneNum
    def get_GP(self):
        return self.GP
    
    def set_name(self,name):
        self.name = name
    def set_lName(self,lName):
        self.lName = lName
    def set_fName(self,fatherName):
        self.fatherName = fatherName
    def set_ID(self,id):
        self.id = id
    def set_GP(self,GP):
        self.GP = GP
    def set_addres(self,addres):
        self.addres = addres
    def set_PC(self,PC):
        self.PC = PC
    def set_telephoneNum(self,telephoneNum):
        self.qualification = telephoneNum
    def set_grade(self,grade):
        self.PC = grade
    def set_telephoneNum(self,DH):
        self.DH = DH