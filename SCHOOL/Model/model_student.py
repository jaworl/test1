class Student:
    students = []
    ID = 1

    def __init__(self, name, lastname, classroom, address, postcode, telephone, dishis, moadel, fatherName):
        self.name = name
        self.lastname = lastname
        self.classroom = classroom
        self.address = address
        self.postcode = postcode
        self.telephone = telephone
        self.dishis = dishis
        self.moadel = moadel
        self.fatherName = fatherName
        self.id = Student.ID
        Student.ID += 1
        Student.students.append(self)

    def get_name(self):
        return self.name

    def get_lastname(self):
        return self.lastname

    def get_id(self):
        return self.id

    def get_classroom(self):
        return self.classroom

    def get_address(self):
        return self.address

    def get_postcode(self):
        return self.postcode

    def get_telephone(self):
        return self.telephone

    def get_dishis(self):
        return self.dishis

    def get_moadel(self):
        return self.moadel

    def get_fatherName(self):
        return self.fatherName

    def set_name(self, name):
        self.name = name

    def set_lastname(self, lastname):
        self.lastname = lastname

    def set_id(self, id):
        self.id = id

    def set_classroom(self, classroom):
        self.classroom = classroom

    def set_address(self, address):
        self.address = address

    def set_postcode(self, postcode):
        self.postcode = postcode

    def set_telephone(self, telephone):
        self.telephone = telephone

    def set_dishis(self, dishis):
        self.dishis = dishis

    def set_moadel(self, moadel):
        self.moadel = moadel

    def set_fatherName(self, fatherName):
        self.fatherName = fatherName

    def findNameStudentByID(id):
        for s in Student.students:
            if s.ID == id:
                return s.split()
            return None

    def findIdStudentByLastname(lastname):
        for nemidonam in range len(Student.students)
            if lastname in nemidonam.split():
                return Student.students[nemidonam]
            return None
