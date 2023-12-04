import Model.Teacher
import Model.Student

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
    qualificalion = input("qualification = ")
    age = input("age = ")
    teachExp = input("teaching experiences = ")
    teacherInClass.append(name + last_name)
    all_members.append(name + last_name)
    id = all_members.index(name + last_name)
    info = Model.Teacher.Teacher(name,last_name,lesson,telephone,qualificalion,age,teachExp , id)
    print ("you have been registerd with these information : ")
    print(teacherInClass)

ids=0
studentInClass = [0]
def SignUpStu() :
     global all_members
     global id
     global studentInClass
     global all_id
     print("answer the questions below to complete youre registeration : ")
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
     info = Model.Student.Student(name,lastname,classroom,address,postcode,telephone,dishis,moadel,fathername , id)
     print ("you have been registerd with these information : ")
     print(studentInClass)

def LogIn() :
        global teacherInClass
        global studentInClass
        TorS = int(input("1.teacher 2.student"))
        if TorS == 1 :
            name1 = input("enter your name: ")
            last_name1 = input("enter your lastname: ")
            if (name1 + last_name1) in teacherInClass :
                ID1 = input("enter your ID: ")
                Index1 = all_members.index(name1 + last_name1)
                if ID1 == Index1 :
                    print("you loged in")
                else :
                    print("wrong id.try again")
            else :
                print("error")

        if TorS == 2 :
            name2 = input("enter your name: ")
            last_name2 = input("enter your lastname: ")
            if (name2 + last_name2) in studentInClass :
                ID2 = input("enter your ID: ")
                Index2 = all_members.index(name2 + last_name2)
                if ID2 == Index2 :
                    print("you loged in")
                else :
                    print("wrong id.try again")
            else :
                print("error")

        elif TorS == 0 :
           print("welcome dear ADMIN")

def menu():
    choose = int(input("1.sign up / 2.log in"))
    if choose == 1 :
        TorS = int(input("1.teacher 2.student"))
        if TorS == 1 :
            SignUpTea()
        if TorS == 2 :
            SignUpStu()
    if choose == 2 :
        LogIn()
        #:)
        
            

            
