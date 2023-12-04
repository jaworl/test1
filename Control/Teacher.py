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

def SaveTea():
    f = open("C:/Users/ASUS/Desktop/Programs/26mordad/13mehr/teacherinfo.txt" , "w")
    f.write("Name: " + name + "\n")
    f.write("Lastname: " + last_name + "\n")
    f.write("Lesson: " + telephone + "\n")
    f.write("Telephone: " + qualification + "\n")
    f.write("Qualification: " + rank + "\n")
    f.write("Age: " + age + "\n")
    f.write("Teaching Experiences: " + teachExp + "\n")
    f.write("ID: " + id + "\n")
    f.close()
