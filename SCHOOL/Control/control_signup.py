
def saveSignUpStudent (student):
    f = open("C:/Users/user/Documents/SCHOOL/save/studentinfo.txt", "w")
    f.write("Name: " + student.name + "\n")
    f.write("Lastname: " + student.slastname + "\n")
    f.write("Classroom: " + student.classroom + "\n")
    f.write("Address: " + student.address + "\n")
    f.write("PostCode: " + student.postcode + "\n")
    f.write("Telephone: " + student.telephone + "\n")
    f.write("Diseases History: " + student.dishis + "\n")
    f.write("Moadel: " + student.moadel + "\n")
    f.write("Father's Name: " + student.fathername + "\n")
    f.write("ID: " + student.id + "\n")
    f.close()

def saveSignUpTeacher (teacher):
    f = open("C:/Users/user/Documents/SCHOOL/save/teacherinfo.txt", "w")
    f.write("Name: " + teacher.name + "\n")
    f.write("Lastname: " + teacher.last_name + "\n")
    f.write("Lesson: " + teacher.lesson + "\n")
    f.write("Telephone: " + teacher.telephone + "\n")
    f.write("Qualification: " + teacher.qualification + "\n")
    f.write("Age: " + teacher.age + "\n")
    f.write("Teaching Experiences: " + teacher.teachExp + "\n")
    f.write("ID: " + teacher.id + "\n")
    f.close()