import Model.model_teacher
import Model.model_student
import Control.control_signup

ids=0
studentInClass = [0]
def SignUpStu():
    global all_members
    global id
    global studentInClass
    global all_id
    global name

    print("answer the questions below to complete your registeration : ")
    name = input("enter student's name: ")
    lastname = input("lastname: ")
    classroom = input("classroom: ")
    address = input("address: ")
    postcode = input("postcode: ")
    telephone = input("telephone: ")
    dishis = input("diseases history: ")
    moadel = input("moadel: ")
    fathername = input("father's name: ")
    studentInClass.append(name + lastname)
    all_members.append(name + lastname)
    id = all_members.index(name + lastname)
    student = Model.model_student.Student(name, lastname, classroom, address, postcode, telephone, dishis, moadel ,   fathername, id)
    Control.control_signup.saveSignUpStudent(student)

all_id = [0]
teacherInClass = [0]
all_members = [0]

def SignUpTea():
    global all_members
    global id
    global teacherInClass
    global all_id
    print("answer the questions below to complete your registeration : ")
    name = input("name = ")
    last_name = input("last name = ")
    lesson = input("lesson = ")
    telephone = input("telephone = ")
    qualification = input("qualification = ")
    age = input("age = ")
    teachExp = input("teaching experiences = ")
    teacherInClass.append(name + last_name)
    all_members.append(name + last_name)
    id = all_members.index(name + last_name)
    teacher = Model.model_teacher.Teacher(name,last_name,lesson,telephone,qualification,age,teachExp , id)
    print("you have been registerd ")
    Control.control_signup.saveSignUpTeacher(teacher)
