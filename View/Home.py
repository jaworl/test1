import Model.Teacher
import Model.Student
import Control.Teacher
import Control.Student
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
            Control.Teacher.SignUpTea()
        if TorS == 2 :
            Control.Student.SignUpStu()
    if choose == 2 :
        LogIn()
        #:)
        
            

            
