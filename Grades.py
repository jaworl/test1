import Model.Student as Student
import Model.Exam as Exam

class grades :
    def __init__ (self,name,lName):
        self.name = name
        self.lName = lName

        self.hesaban =  []
        self.amar = []
        self.hendeseh   = []
        self.fizik = []
        self.shimi = []
        self.tarikh =  []
        self.arabi = []
        self.adabiat = []
        self.dini = []
        self.zaban = []

    def get_hessaban(self):
        return self.hesaban
    def get_lName(self):
        return self.amar
    def get_lesson_name(self):
        return self.hendeseh
    def get_date(self):
        return self.fizik
    def get_grade(self):
        return self.shimi 
    def get_rank(self):
        return self.tarikh
    def get_ID(self):
        return self.arabi
    def get_rank(self):
        return self.adabiat
    def get_ID(self):
        return self.dini
    def get_ID(self):
        return self.zaban
    def get_name(self):
        return self.name
    def get_lName(self):
        return self.lName
    
    def set_name(self,hesaban):
        self.hesaban = hesaban
    def set_lName(self,lName):
        self.lName = lName


    