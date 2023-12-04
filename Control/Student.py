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

    
def show() :
    f = open("C:/Users/ASUS/Desktop/Programs/26mordad/13mehr/studentinfo.txt" , "w")
    lines = f.readlines()
    f.close()
    print(lines)
    for line in lines :
        print(line)
