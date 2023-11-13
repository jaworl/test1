import Model.Student
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

# student = Model.Student(name , lastname , id , classroom , address , postcode , telephone , dishis , moadel , fathername)
# f = open("C:/Users/ASUS/Desktop/Programs/26mordad/13mehr/studentinfo.txt" , "w")
# f.write("Student's Name: " + name + "\n")
# f.write("Student's Lastname: " + lastname + "\n")
# f.write("ID: " + id + "\n")
# f.write("Classroom: " + classroom + "\n")
# f.write("Address: " + address + "\n")
# f.write("PostCode: " + postcode + "\n")
# f.write("Telephone: " + telephone + "\n")
# f.write("Diseases History: " + dishis + "\n")
# f.write("Moadel: " + moadel + "\n")
# f.write("Father's Name: " + fathername + "\n")
# f.close()
    
def show() :
    f = open("C:/Users/ASUS/Desktop/Programs/26mordad/13mehr/studentinfo.txt" , "w")
    lines = f.readlines()
    f.close()
    print(lines)
    for line in lines :
        print(line)
