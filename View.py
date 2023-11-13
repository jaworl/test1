from Control import menu
from Control import teachers_reagester
from Control import students_register
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