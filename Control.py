import model.Teacher as Teacher
import model.Student as Student
def menu ():
    chooseOption = int(input("WELLCOME!/nHow can we help you?/n1.register/n2.log in to your profile"))
    return chooseOption

id=0
all_id = [0]
teacherInClass = []
def teachers_reagester ():
    global id
    global teacherInClass
    print("answer the questions below to complete youre registeration : ")
    name = input("name = ")
    last_name = input("last name = ")
    age = input("age = ")
    idt += 1
    all_id.append(id)
    teacherInClass = id
    clac = input("clac = ")
    qualificalion = input("qualification = ")

    teacherInClass[id] = Teacher(name,last_name,age,id,clac,qualificalion)
    print ("you have been registerd with these information : ")
    print(teacherInClass)

def students_register() :
    global id
    global InClass
    print("answer the questions below to complete youre registeration : ")
    name = input("name = ")
    last_name = input("last name = ")
    id +=1 
    all_id.append(id)
    clac = input("clac = ")
    fatherName = input("fatherName = ")
    GP = input("GP = ")
    addres = input("addres = ")
    PC = input("PC = ")
    telephoneNum = input("telephoneNum = ")
    DH = input("DH = ")

    studentInClass[id] = Student(name,last_name,id,clac,fatherName,GP,addres,PC,telephoneNum,DH)
    print ("you have been registerd with these information : ")
    print(studentInClass)