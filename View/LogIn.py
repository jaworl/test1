import Control.Exam
import Control.Student
import Control.Teacher
def LogIn() :
        global teacherInClass
        global studentInClass
        global all_members
        TorS = int(input("1.teacher 2.student"))
        if TorS == 1 :
            name1 = input("enter your name: ")
            last_name1 = input("enter your lastname: ")
            if (name1 + last_name1) in teacherInClass :
                ID1 = input("enter your ID: ")
                Index1 = all_members.index(name1 + last_name1)
                if ID1 == Index1 :
                   examine = input("you loged in. you have 2 options: a) add exam - b) student list")
                        if examine == "a" :
                                Control.Exam.TakeExam()
                        elif examine == "b" :
                                Control.Student.show()

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