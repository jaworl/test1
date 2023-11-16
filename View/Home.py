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
id=0
all_id = [0]
teacherInClass = [0]

def teachers_reagester ():
    global id
    global teacherInClass
    print("answer the questions below to complete youre registeration : ")
    name = input("name = ")
    last_name = input("last name = ")
    lesson = input("lesson = ")
    telephone = input("tele = ")
    qualificalion = input("qualification = ")
    age = input("age = ")
    teachExt = input("teaching experiences = ")
    idt += 1
    all_id.append(id)
    teacherInClass.append(name + last_name)

    teacherInClass[id] = Teacher(name,last_name,age,id,clac,qualificalion)
    print ("you have been registerd with these information : ")
    print(teacherInClass)

 def SignUp() :
     name = input("enter student's name: ")
     lastname = input("lastname: ")
     id = input("id: ")
     classroom = input("classroom: ")
     address = input("address: ")
     postcode = input("postcode: ")
     telephone = input("telephone: ")
     dishis = input("diseases history: ")
     moadel = input("moadel: ")
     fathername = input("father's name: ")
SignUp()

 def LogIn() :
     
        name = input("enter your name: ")
        last_name = input("enter your lastname: ")
        if (name + last_name) in teacherInClass :
            ID = input("enter your ID: ")
        Index = teacherInClass.index(name+last_name)
        if ID == Index :
            print("you loged in")
        else :
            print("wrong id.try again")
                
        
            

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
