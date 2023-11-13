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



# def SignUp() :
#     name = input("enter student's name: ")
#     lastname = input("lastname: ")
#     id = input("id: ")
#     classroom = input("classroom: ")
#     address = input("address: ")
#     postcode = input("postcode: ")
#     telephone = input("telephone: ")
#     dishis = input("diseases history: ")
#     moadel = input("moadel: ")
#     fathername = input("father's name: ")
# SignUp()

from Control import all_id

def show ():
    menu () 
    if menu() == 1 :
        TorS = int(input("1.you are a teacher/n2.you are a student"))
        if TorS == 1 :
            teachers_reagester()
        if TorS == 2 :
            students_register()
    if menu() == 2 :
        get_id = int(input("enter your id to log in : "))
        if get_id in all_id :
            print()
show()
