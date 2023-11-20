# import Control.Exam
# import Control.Student
# def menu() :
#     while True :
#         choise = int(input("Choose one item: 1- SignUp | 2- Take Exam | 3- Show Informations"))
#         if choise == 1 :
#             Control.Student
#         elif choise == 2 :
#             Control.Exam
#         else :
#             Control.Student.show()
idt=0
all_id = [0]
teacherInClass = [0]

def SignUpTea():
    global id
    global teacherInClass
    global all_id
    print("answer the questions below to complete youre registeration : ")
    name = input("name = ")
    last_name = input("last name = ")
    lesson = input("lesson = ")
    telephone = input("telephone = ")
    qualificalion = input("qualification = ")
    age = input("age = ")
    teachExt = input("teaching experiences = ")
    idt += 1
    all_id.append(idt)
    teacherInClass.append(name + last_name)

    teacherInClass[idt] = Teacher(name,last_name,lesson,telephone,qualificalion,age,teachExp)
    print ("you have been registerd with these information : ")
    print(teacherInClass)

ids=0
studentInClass = [0]
 def SignUpStu() :
     global id
     global studentInClass
     global all_id
     name = input("enter student's name: ")
     lastname = input("lastname: ")
     classroom = input("classroom: ")
     address = input("address: ")
     postcode = input("postcode: ")
     telephone = input("telephone: ")
     dishis = input("diseases history: ")
     moadel = input("moadel: ")
     fathername = input("father's name: ")
     ids += 1
     all_id.append(ids)
     studentInClass.append(name + lastname)

     studentInClass[ids] = Student(name,lastname,classroom,address,postcode,telephone,dishis,moadel,fathername)
     print ("you have been registerd with these information : ")
     print(studentInClass)


 def LogIn() :
        TorS = int(input("1.teacher 2.student"))
        if TorS == 1 :
            name = input("enter your name: ")
            last_name = input("enter your lastname: ")
            if (name + last_name) in teacherInClass :
                ID = input("enter your ID: ")
                Index = teacherInClass.index(name+last_name)
                if ID == Index :
                    print("you loged in")
                else :
                    print("wrong id.try again")
            else :
                print("error")
       
        if (name + last_name) in teacherInClass :
            ID = input("enter your ID: ")
        Index = teacherInClass.index(name+last_name)
        if ID == Index :
            print("you loged in")
        else :
            print("wrong id.try again")


def menu():
    choos = int(input("1.sign up /n2.log in")
    if menu() == 1 :
        TorS = int(input("1.teacher 2.student"))
        if TorS == 1 :
            SignUpTea()
        if TorS == 2 :
            SignUpStu()
    if menu() == 2 :
        
            

def show ():
    menu () 
    if menu() == 1 :
        TorS = int(input("1.you are a teacher 2.you are a student"))
        if TorS == 1 :
            teachers_reagester()
        if TorS == 2 :
            students_register()
    if menu() == 2 :
        get_id = int(input("enter your id to log in : "))
        if get_id in all_id :
            print()
show()
