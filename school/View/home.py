import View.view_signup
import View.view_login
def menu():

    choose = int(input("1.sign up / 2.log in"))
    if choose == 1 :
        TorS = int(input("1.teacher 2.student"))
        if TorS == 1 :
            View.view_signup.SignUpTea()
        if TorS == 2 :
            View.view_signup.SignUpStu()
    if choose == 2 :
        View.view_login.LogIn()
        #:)

#ye file dige nemikhad?

